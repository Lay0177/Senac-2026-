from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/Calabresa')
def pizzaria():
    return render_template('Calabresa.html')

@app.route('/')
@app.route('/Frango')
def pizzaria():
    return render_template('Frango com catupiry.html')

if __name__ == '__main__':
    app.run(debug=True)