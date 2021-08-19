from flask import Blueprint, request, json, render_template, url_for, redirect, flash, session
import requests

route_gate = Blueprint('route_gate', __name__)


@route_gate.route('/', methods=['GET'])
def index():
    ip = request.environ['REMOTE_ADDR']
    url = 'http://freegeoip.net/json/' + ip
    r = requests.get(url)
    js = r.json()
    print(js['country_code'])
    return 'hello'
