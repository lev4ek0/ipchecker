from flask import Blueprint, request, json, render_template, url_for, redirect, flash, session

route_gate = Blueprint('route_gate', __name__)


@route_gate.route('/', methods=['GET'])
def index():
    return 'hello'
