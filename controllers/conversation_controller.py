import app_state

class conversation_controller:
    def __init__(self):
        pass

    def create_chat(self):
        print("[CONVERSATION CONTROLLER]: create chat")

    def send_message(self, new_message):
        print("[CONVERSATION CONTROLLER]: send message")
        app_state.watcher.message_input = ""
        updated_messages = app_state.watcher.cc_messages.copy()
        updated_messages[new_message.msg_id] = new_message
        app_state.watcher.cc_messages = updated_messages

conversation_ctrl = conversation_controller()