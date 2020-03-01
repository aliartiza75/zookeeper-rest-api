import os
import sys
import json
from flask import Blueprint
from flask import request, jsonify, abort

zk_blueprint = Blueprint('zookeeper', __name__)

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
from services import response_service as resp_service


@zk_blueprint.route('/', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def default():
    '''
    It will be used to verify the status of api
    '''
    response = {}
    response['message'] = 'You are using Zookeeper REST API'
    return jsonify(response)


@zk_blueprint.route('/zookeeper/apihealthcheck', methods=['GET'])
def health_check():
    '''
    It will be used to verify the status of api
    '''
    response = {}
    response['message'] = 'Api is in healthy state'
    return jsonify(response)

@zk_blueprint.route('/zookeeper/servicehealthcheck', methods=['GET'])
def zk_service_health_check():
    '''
    It will be used to verify the status of api
    '''
    response = {}
    response['message'] = 'Service is running correctly'
    return jsonify(response)

