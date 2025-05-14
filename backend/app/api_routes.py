from flask import Blueprint, jsonify
import app.f1_data as f1_data

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/<int:year>/drivers')
def api_drivers(year):
    return jsonify(f1_data.get_drivers(year))

@api_bp.route('/api/<int:year>/constructors')
def api_constructors(year):
    return jsonify(f1_data.get_constructors(year))

@api_bp.route('/api/schedule/<int:year>')
def api_schedule(year):
    return jsonify(f1_data.get_season_schedule(year))

@api_bp.route('/api/results/<int:year>/<int:round_num>')
def api_results(year, round_num):
    return jsonify(f1_data.get_race_results(year, round_num))

@api_bp.route('/api/standings/<int:year>')
def api_standings(year):
    return jsonify(f1_data.get_driver_standings(year))

@api_bp.route('/api/<int:year>/constructorStandings/')
def api_team_standings(year):
    return jsonify(f1_data.get_team_standings(year))

@api_bp.route('/api/lapstats/<int:year>/<int:round_num>')
def api_lap_stats(year, round_num):
    return jsonify(f1_data.get_race_data(year, round_num))