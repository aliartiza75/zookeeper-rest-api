from zookeeper_endpoints.routes import zk_blueprint
from flask import Flask, Blueprint
from flask_api import FlaskAPI
app = Flask(__name__)

# registering application
app.register_blueprint(zk_blueprint)


