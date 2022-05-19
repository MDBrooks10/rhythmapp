from flask import render_template, redirect, Blueprint, url_for

my_view = Blueprint('my_view', __name__)

@my_view.route("/")
def index():
    return render_template("index.html")

@my_view.route("/anthropology")
def anth():
    return render_template("anthropology.html")

@my_view.route("/composite")
def comp():
    return render_template("composite.html")

@my_view.route("/linguistics")
def ling():
    return render_template("linguistics.html")

@my_view.route("/terminology")
def term():
    return render_template("terminology.html")

@my_view.route("/admin")
def admin():
    return render_template("admin.html")

@my_view.route("/rhythm")
def index_redirect():
    return redirect(url_for("my_view.index"))