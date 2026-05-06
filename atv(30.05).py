from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "olá, mundo!"

@app.template("/")
def template():
    return render_template('login')

if __name__ == "__main__":
    app.run(debug=True)

#HTML-login#

