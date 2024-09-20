from flask import Flask

app = Flask(__name__)


@app.route("/")
def greeting():
    return "Hello, Flask!"


@app.route("/user/<name>")
def greeting_user(name):
    return f"Hello {name}"


if __name__ == "__main__":
    app.run()
