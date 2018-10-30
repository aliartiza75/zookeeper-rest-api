import os
import sys
import json
from flask import Blueprint
from flask import request, jsonify, abort

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
from services import response_service as resp_service


@mod.route('/zookeeper/healthcheck', methods=['GET'])
def health_check():
    '''
    It will be used to verify the status of api
    '''
    response = {}
    response['message'] = 'Api is in healthy state'
    return jsonify(response)
