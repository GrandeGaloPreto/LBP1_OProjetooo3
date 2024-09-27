from flask import Flask, Blueprint
from controllers.controller import blueprintrota

app = Flask(__name__)
app.register_blueprint(blueprintrota)

if __name__ == "__main__":
    app.run(debug=True)