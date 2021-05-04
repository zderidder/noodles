from email_validator import validate_email
from flask import Flask, render_template, request
from forms import FunFactForm, ContactUs, RestaurantForm, HomemadeForm
import sqlite3 as sql

app = Flask(__name__)
app.secret_key = 'developer_key'


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about-us")
def aboutus():
    return render_template("about.html")


@app.route("/fried")
def fried():
    return render_template("fried.html")


@app.route("/history")
def history():
    return render_template("history.html")


@app.route("/homemade", methods=['GET', 'POST'])
def homemade(invalid=None):
    form = HomemadeForm(request.form)
    print(form.validate())

    con = sql.connect("database.db")
    con.row_factory = sql.Row

    if request.method == 'POST':
        try:
            email = request.form['email'].strip()
            recipe = request.form['recipe'].strip()
            link = request.form['link'].strip()

            if len(email) != 0 and len(recipe) != 0 and len(link) != 0:
                with sql.connect("database.db") as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO recipes(email, name, location) VALUES (?,?,?)", (email, recipe, link))
                    con.commit()
                    return render_template("submitted.html")
            else:
                print("Not added")
                return render_template("homemade.html", invalid=True)
        except:
            con.rollback()
    con.close()

    return render_template("homemade.html")


@app.route("/pasta")
def pasta():
    return render_template("pasta.html")


@app.route("/restaurants", methods=['GET', 'POST'])
def restaurants(invalid=None):
    form = RestaurantForm(request.form)
    print(form.validate())

    con = sql.connect("database.db")
    con.row_factory = sql.Row

    if request.method == 'POST':
        try:
            email = request.form['email'].strip()
            restaurant = request.form['restaurant'].strip()
            address = request.form['address'].strip()

            if len(email) != 0 and len(restaurant) != 0 and len(address) != 0:
                with sql.connect("database.db") as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO restaurants(email, name, location) VALUES (?,?, ?)", (email, restaurant, address))
                    con.commit()
                    return render_template("submitted.html")
            else:
                print("Not added")
                return render_template("restaurants.html", invalid=True)
        except:
            con.rollback()

    con.close()

    return render_template("restaurants.html")


@app.route("/soup")
def soup():
    return render_template("soup.html")


@app.route("/contact-us", methods=['GET', 'POST'])
def contactus(invalid=False):
    form = ContactUs(request.form)
    print(form.validate())
    msg = ""

    con = sql.connect("database.db")
    con.row_factory = sql.Row

    if request.method == 'POST':
        try:
            name = request.form['name'].strip()
            email = request.form['email'].strip()
            problem = request.form['problem'].strip()
            description = request.form['description'].strip()

            if len(email) != 0 and len(name) != 0 and len(problem) != 0 and len(description) != 0:
                with sql.connect("database.db") as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO contact(name, email, problem, description) VALUES (?,?,?,?)", (name, email, problem, description))
                    con.commit()
                    msg = "Record successfully added"
            else:
                return render_template("contact_us.html", invalid=True, successful=False)
        except:
            con.rollback()
            msg = "Error in insert"
            return render_template("contact_us.html", invalid=True, successful=False)
        finally:
            return render_template("contact_us.html", invalid=False, successful=True)
    con.close()
    return render_template("contact_us.html", invalid=False, successful=False)

@app.route("/fun-facts", methods=['GET', 'POST'])
def funfacts(invalid=None):
    form = FunFactForm(request.form)
    print(form.validate())
    msg = ""

    con = sql.connect("database.db")
    con.row_factory = sql.Row

    if request.method == 'POST':
        try:
            name = request.form['name'].strip()
            fact = request.form['fact'].strip()

            if len(fact) != 0 and len(name) != 0:
                with sql.connect("database.db") as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO facts(name, fact) VALUES (?,?)", (name, fact))
                    con.commit()
                    msg = "Record successfully added"
                    return render_template("submitted.html")
            else:
                return render_template("fun_facts.html", invalid=True)
        except:
            con.rollback()
            msg = "Error in insert"

    cur = con.cursor()
    cur.execute("select * FROM facts ORDER BY RANDOM() LIMIT 1")

    fact = cur.fetchall()

    con.close()

    return render_template("fun_facts.html", fact=fact)

if __name__ == '__main__':
    app.run(debug=True)
