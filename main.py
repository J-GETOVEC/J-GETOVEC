from config import app, Flask, render_template

from random import randint
from datetime import datetime
from models import Flat



@app.route("/cats/")
def index():
    cat_name="Barsik"
    return render_template("cats.html", cat_name=cat_name, )


@app.route("/nm/")
def index1():
    return render_template("names.html")


@app.route("/random/<first>/<second>")
def info(first, second):
    text = f"<h1>Привет вот твое число {randint(int(first), int(second))}</h1>"
    return text


@app.route("/time")
def info1():
    f = str(datetime.now())
    f = f[11:19]
    text = f"<h1>Привет вот настоящее время {f} </h2>"
    return text


@app.route("/flats")
def flats_view():
    flats = Flat.query.all()
    time = str(datetime.now())[0: 4]
    return render_template("flats.html", flats=flats, time=time)

@app.route("/flat/<flat_pk>")
def flat_view(flat_pk):
    flat = Flat.query.get(int(flat_pk))

    return render_template("flat.html", flat=flat)

@app.route("/flatsprod")
def flats_view1():
    flats = Flat.query.all()
    return render_template("flats1.html", flats=flats)

app.run(debug=True)
