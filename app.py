from flask import Flask, render_template            #flask imports
from views import my_view                           #local imports

app = Flask(__name__)
app.register_blueprint(my_view)                     #Sets the blueprint

@app.errorhandler(404)                              #Error handling belongs in the app.py
def page_not_found(e):                              #Function for error handling. e is the variable for the error message. It is built into flask.
    return render_template("404.html", e=e)         #Redirects to our 404.html

if __name__ == "__main__":
    app.run(debug=True, port=8000)