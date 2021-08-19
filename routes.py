from flask import Blueprint, request, json, render_template, url_for, redirect, flash, session
import requests

route_gate = Blueprint('route_gate', __name__)


def getting_ip(row):
    """This function calls the api and return the response"""
    url = f"https://freegeoip.app/json/{row}"       # getting records from getting ip address
    headers = {
        'accept': "application/json",
        'content-type': "application/json"
        }
    response = requests.request("GET", url, headers=headers)
    respond = json.loads(response.text)
    return respond


@route_gate.route('/', methods=['GET'])
def index():
    ip = request.environ['REMOTE_ADDR']
    print('Страна:', getting_ip(ip).get('country_name'))
    return 'hello'
