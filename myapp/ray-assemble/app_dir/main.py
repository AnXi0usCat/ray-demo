from starlette.requests import Request
from starlette.responses import JSONResponse

from ray import serve

from transformers import pipeline


@serve.deployment(num_replicas=2, ray_actor_options={"num_cpus": 1.0, "num_gpus": 0})
class Translator:
    def __init__(self):
        # Load model
        self.model = pipeline("translation_en_to_fr", model="t5-small")

    async def translate(self, text: str) -> str:
        # Run inference
        model_output = self.model(text)

        # Post-process output to return only the translation text
        translation = model_output[0]["translation_text"]

        return translation

    async def __call__(self, http_request: Request) -> JSONResponse:
        english_text: str = await http_request.json()
        output = await self.translate(english_text["text"])
        return JSONResponse({"message": output})


translator_app = Translator.bind()
serve.run(translator_app)
