# demo6.py - forms
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

@server.route("/login", ["POST",'GET'])
def login_form(request):
    print(request.method)
    if request.method == 'GET':
        return render_template("login.html")
    if request.method == 'POST':    
        username = request.form.get("username", None)
        password = request.form.get("password", None)

        if username == "kevin" and password == "password":
            return render_template('default.html', content = f"<h1>Welcome back, {username}</h1>")
        else:
            return render_template('default.html', content = "Invalid username or password")

@server.catchall()
def my_catchall(request):
  return "No matching route", 404

server.run()