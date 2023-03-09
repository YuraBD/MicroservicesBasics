import uvicorn
from fastapi import FastAPI, APIRouter
from facade_service import FacadeService
import json
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from message import Message

localhost = "127.0.0.1"
facade_port = 8080
logging_port = 8001
messages_port = 8002

class FacadeController:
    def __init__(self, facade_service: FacadeService):
        self.router = APIRouter()
        self.router.add_api_route("/", self.get_req, methods=["GET"])
        self.router.add_api_route("/", self.post_req, methods=["POST"])
        self.facade_service = facade_service

    async def get_req(self):
        logging_url = f"http://{localhost}:{logging_port}"
        messages_url = f"http://{localhost}:{messages_port}"
        logging_response = self.facade_service.get_logged_messages(logging_url)
        messages_response = self.facade_service.get_logged_messages(messages_url)
        text = "Logged messages: " +  logging_response.json() + " | " + "Messages service response: "  + messages_response.json()
        return text

    async def post_req(self, msg: Message):
        if not msg.msg:
            return "Empty message"
        
        logging_url = f"http://{localhost}:{logging_port}"
        logging_response = self.facade_service.log_message(msg, logging_url)
        if logging_response.json() == "Empty message":
            return "Empty message"

        return f"Message: \"{msg.msg}\" sent"


if __name__ == "__main__":
    facade_service = FacadeService()
    app = FastAPI() 
    facade_controller = FacadeController(facade_service) 
    app.include_router(facade_controller.router) 
    uvicorn.run(app, host=localhost, port=facade_port)