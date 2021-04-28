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

@app.route("/fried")
def fried():
    return render_template("fried.html")

@app.route("/fun-facts")
def funfacts():
    return render_template("fun_facts.html")

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

if __name__=='__main__':
    app.run(debug=True)