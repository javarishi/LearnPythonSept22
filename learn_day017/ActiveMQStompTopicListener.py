import stomp
import time

host = "localhost"
port = 61613

class SimpleListner:

    def on_error(self, message):
        print("Encounter an Error" , message)

    def on_message(self, message):
        print("Processing Message Now ", message)

# In Listeners / Subscribers we do not close the connection - becoz it will close the listener
try:
    conn = stomp.Connection(host_and_ports = [(host, port)])
    conn.set_listener('h2k_event_listener', SimpleListner())
    conn.connect()
    conn.subscribe(destination="/topic/h2k_event_topic", id="1", ack= "auto")
    print("Waiting for messages...")
    while True:
        time.sleep(5)

except Exception as ex:
    print(ex)