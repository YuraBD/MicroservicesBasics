localhost = "127.0.0.1"
facade_port = 8080
logging_port = 8001
messages_port = 8002

import requests

logging_url = f"http://{localhost}:{logging_port}"

response = requests.get(logging_url)
print(response)