class LoggingRepository:
    def __init__(self, ):
        self.map = dict()
    
    def add_message(self, msg):
        self.map[msg.uuid] = msg.msg

    def get_logs(self):
        return ", ".join(self.map.values())