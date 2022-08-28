# demo4.py - a simple site
# Kevin McAleer
# 28 Aug 2022

from phew import logging, server, connect_to_wifi
from secret import ssid, password

connect_to_wifi(ssid, password)

#server.add_route("/", index, methods=["GET"])

@server.route("/")
def index(request):
    response = "Hello world"
    return response

logging.info("Starting Web Server")
server.run()