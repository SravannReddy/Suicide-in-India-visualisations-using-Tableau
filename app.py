# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, redirect,url_for, render_template

# Flask constructor takes the name of
# current module (_name_) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route("/")

# ‘/’ URL is bound with hello_world() function.
def main():
	return render_template(r"index.html")

# main driver function
if __name__ == '_main_':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run(debug=False,port=5000)