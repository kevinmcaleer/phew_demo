# demo5.py - templates site
# Kevin McAleer
# 28 Aug 2022

from phew import logging, server, connect_to_wifi
from phew.template import render_template
from secret import ssid, password

connect_to_wifi(ssid, password)

@server.route("/")
def index(request):
    return render_template("index.html", name="Kevin")

server.run()