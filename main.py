from flask import Flask, render_template, request, flash
from forms import FunFactForm
import sqlite3 as sql

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about-us")
def aboutus():
    return render_template("about.html")

@app.route("/contact-us")
def contactus():
    return render_template("contact_us.html")

@app.route("/fried")
def fried():
    return render_template("fried.html")

@app.route("/history")
def history():
    return render_template("history.html")

@app.route("/homemade")
def homemade():
    return render_template("homemade.html")

@app.route("/pasta")
def pasta():
    return render_template("pasta.html")

@app.route("/restaurants")
def restaurants():
    return render_template("restaurants.html")

@app.route("/soup")
def soup():
    return render_template("soup.html")

@app.route("/fun-facts", methods = ['GET', 'POST'])
def funfacts():

    #con = sql.connect("database.db")
    #con.row_factory = sql.Row

    #cur = con.cursor()
    #cur.execute("select * from facts")

    #rows = cur.fetchall()
    #return render_template("fun_facts.html", rows = rows)

    form = FunFactForm()
    msg = ""
    if request.method == 'POST':
        flash('All fields are required')
        return render_template('fun_facts.html', form=form)
    else:
        try:
            name = request.form['name']
            fact = request.form['fact']
            with sql.connect("fun_facts_database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO facts(name, fact) VALUES (?,?)",(name, fact))
                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "Error in insert"
        finally:
            return render_template("submitted.html", msg = msg)
            con.close()


if __name__=='__main__':
    app.run(debug=True)