from flask import Flask, render_template

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

@app.route("/restaurants")
def restaurants():
    return render_template("restaurants.html")

@app.route("/recipes")
def recipes():
    return render_template("homemade.html")

@app.route("/fun-facts")
def funfacts():
    return render_template("fun_facts.html")

@app.route("/history")
def history():
    return render_template("history.html")

if __name__=='__main__':
    app.run(debug=True)