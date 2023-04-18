from flask import Blueprint, request, jsonify

blueprint = Blueprint('api', __name__)

from . import extract