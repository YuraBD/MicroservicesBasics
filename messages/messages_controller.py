from fastapi import FastAPI, APIRouter
import uvicorn

localhost = "127.0.0.1"
logging_port = 8002

class MessageController:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/", self.get_req, methods=["GET"])

    def get_req(self):
        return "Not implemented yet"

if __name__ == "__main__":
    app = FastAPI() 
    messages_controller = MessageController()
    app.include_router(messages_controller.router) 
    uvicorn.run(app, host=localhost, port=logging_port)