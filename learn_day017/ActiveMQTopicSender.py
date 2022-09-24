import stomp

host = "localhost"
port = 61613

conn = stomp.Connection(host_and_ports = [(host, port)])
conn.connect()

for i in range(1,11):
    message = "This is my {} Message from Python".format(i)
    conn.send(destination="/topic/h2k_event_topic", body=message, persistent='true' )
conn.disconnect()