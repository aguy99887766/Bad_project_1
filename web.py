from flask import Flask, render_template, request, redirect, url_for, session
from messanger import message, load_messages, get_messages


app = Flask(__name__)
app.secret_key = 'abc'

@app.route("/", methods=['GET', 'POST'])
def main_page() -> render_template:
	
	directories = {
		"create": "/create",
	}

	if request.method == "POST":
		value = request.form.get('action')
		redirection = directories.get(value)
		return redirect(redirection)
	return render_template("home.html")
		

@app.route("/message", methods=['GET', 'POST'])
def message_users() -> render_template:
	loaded_messages = get_messages()
	print(loaded_messages)

	if request.method == "POST":	
		value = request.form.get('action')
		if value == "send_message":
			print(f"Value triggered")
			send = request.form.get("content")
			print(send)
			message(session['username'], send)

	return render_template("chat.html", username=session['username'], messages=loaded_messages)

@app.route("/create", methods=['GET', 'POST'])
def create() -> render_template: 
	if request.method == "POST":
		username = request.form.get("username")
		session['username'] = username
		print(f"[+] {username} has been created")
		return redirect("/message")

	return render_template("login.html")	


app.run(debug=True)
