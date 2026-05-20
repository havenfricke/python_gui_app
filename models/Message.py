import uuid

class Message:
    def __init__(self, text: str, sent: int):
        self.msg_id = str(uuid.uuid4())
        self.text = text
        self.sent = sent