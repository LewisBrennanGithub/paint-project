from flask import Flask, render_template

from controllers.paints_controller import paints_blueprint

app = Flask(__name__)

app.register_blueprint(paints_blueprint)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)