# demo6.py - using includes to build multi-part pages
# Kevin McAleer
# 28 Aug 2022

from phew import logging, server, connect_to_wifi
from phew.template import render_template
from secret import ssid, password

connect_to_wifi(ssid, password)

@server.route("/")
def index(request):
    return render_template("index2.html", name="Kevin", title="Kev's Personal Blog")

@server.route("/about")
def about(request):
    return render_template("about.html", name="Kevin", title="About this Site")

@server.catchall()
def my_catchall(request):
  return "No matching route", 404

server.run()