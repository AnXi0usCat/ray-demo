FROM rayproject/ray:2.5.0

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /serve_app

COPY src/serve.py /serve_app/serve.py
