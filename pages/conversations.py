from slimgui import imgui
import app_state
from models.Message import Message

def init_conversations(width, height, window):

    avail_width = imgui.get_content_region_avail()[0]

    imgui.begin_child("Chats", (200, 450), imgui.ChildFlags.BORDERS)
    
    imgui.text("ROOMS")
    imgui.separator()

    if imgui.button("Create Room", (184, 0)):
        print("New room process started")

    # ------------------------------------- Iteratable code for incoming data 

    if imgui.selectable("Chat Name")[0]:
        app_state.watcher.current_chat = "Chat Name"
        print(f"selected '{app_state.watcher.current_chat}'")

    # ------------------------------------- Iteratable code for incoming data 
        
    imgui.end_child() # Chats

    imgui.same_line()

    imgui.begin_child("Chat Box", (avail_width - 220, 450), imgui.ChildFlags.BORDERS)

    # ------------------------------------- Iteratable code for incoming data 
    # psuedo:
    # for message in messages:
    #   if message['sender'] != me:
    #       run the code below ->
    imgui.begin_table(
        str_id="Chat Row",
        column=2,
        flags=imgui.TableFlags.BORDERS,
        outer_size=(avail_width - 235, 0)
    )

    imgui.table_next_column()
    imgui.table_set_column_index(0)
    imgui.spacing()
    imgui.text_wrapped("Username:")
    imgui.same_line()
    imgui.text_wrapped("Column 1 on the left side for received messages.")
    imgui.spacing()

    imgui.table_next_column()
    imgui.table_set_column_index(1)
    imgui.spacing()
    imgui.text_wrapped("Username:")
    imgui.same_line()
    imgui.text_wrapped("Column 2 on the right side for sent messages.")
    imgui.spacing()

    imgui.end_table()

    imgui.end_child() # Chat Box
    # ------------------------------------- Iteratable code for incoming data 

    imgui.begin_child("Connections", (200, -1), imgui.ChildFlags.BORDERS)

    imgui.text("CONNECTIONS")
    imgui.separator()

    if imgui.button("Add Connection", (184, 0)):
        print("New room process started")

    # ------------------------------------- Iteratable code for incoming data 

    if imgui.selectable("Connection's Name")[0]:
        app_state.watcher.current_chat = "Connection's Name"
        print(f"selected user '{app_state.watcher.current_chat}'")

    # ------------------------------------- Iteratable code for incoming data 

    imgui.end_child() # Connections
    imgui.same_line()
    
    imgui.begin_child("Input Text", (avail_width - 220, 127), imgui.ChildFlags.BORDERS)

    changed, input = imgui.input_text_multiline(
        label=" ",
        text="",
        size=(avail_width - 330, 0),
        flags=imgui.InputTextFlags.NONE
    )

    if changed:
        app_state.watcher.message_input = input

    imgui.same_line()

    if imgui.button("SEND", (70, 110)):
        print("send message triggered")
        new_message = Message(text=app_state.watcher.message_input, sent=1)
        input = ""
        app_state.watcher.message_input = ""
        updated_messages = app_state.watcher.cc_messages.copy()
        updated_messages[new_message.msg_id] = new_message
        app_state.watcher.cc_messages = updated_messages
        

    imgui.end_child() # Input Text

    
