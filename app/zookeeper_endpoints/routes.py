import os
import sys
import json
from flask import Blueprint
from flask import request, jsonify, abort

mod = Blueprint('zookeeper', __name__)

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
from services import response_service as resp_service



