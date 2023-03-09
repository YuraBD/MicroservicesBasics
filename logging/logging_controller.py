import uvicorn
from fastapi import FastAPI, APIRouter
from logging_service import LoggingService
from logging_repository import LoggingRepository
import json
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from message import Message


localhost = "127.0.0.1"
logging_port = 8001


class LoggingController:
    def __init__(self, logging_service: LoggingService):
        self.router = APIRouter()
        self.router.add_api_route("/", self.get_req, methods=["GET"])
        self.router.add_api_route("/", self.post_req, methods=["POST"])
        self.logging_service = logging_service

    async def get_req(self):
        print("Getting logs...")
        msg_list = self.logging_service.get_logs()
        return msg_list

    async def post_req(self, msg: Message):
        if not msg.msg:
            return "Empty message"
        print(f"Got message: {msg.msg}")
        result = self.logging_service.add_message(msg)
        return result

if __name__ == "__main__":
    logging_repository = LoggingRepository()
    logging_service = LoggingService(logging_repository)
    app = FastAPI() 
    logging_controller = LoggingController(logging_service) 
    app.include_router(logging_controller.router) 
    uvicorn.run(app, host=localhost, port=logging_port)