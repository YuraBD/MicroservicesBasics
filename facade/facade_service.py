from fastapi import FastAPI, APIRouter
import requests
import json


class FacadeService:
    def log_message(self, msg, url):
        response = requests.post(url, json=json.loads(msg.json()))
        return response

    def get_logged_messages(self, url):
        response = requests.get(url)
        return response