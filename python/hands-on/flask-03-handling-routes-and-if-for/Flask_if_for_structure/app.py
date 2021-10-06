from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def head():
    first = 'Das ist meine erste Erfahrung über Zustand '
    return render_template('index.html', message=first)


@app.route('/mehmet')
def meineliste():
    namen = ["mehmet", "azra", "meryem", "hatice", "sibel", "esra"]
    return render_template('body.html', object=namen)


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=80)
