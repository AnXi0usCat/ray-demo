import requests
import numpy as np


if __name__ == "__main__":
    print(requests.get("https://httpbin.org/ip").json())
    print(np.zeros(10))