from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
from models import db, User, FavoriteRace
import f1_data

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return jsonify({"message": "F1 API backend is running!"})

@app.route('/api/schedule/<int:year>')
def api_schedule(year):
    return jsonify(f1_data.get_season_schedule(year))

@app.route('/api/results/<int:year>/<int:round_num>')
def api_results(year, round_num):
    return jsonify(f1_data.get_race_results(year, round_num))

@app.route('/api/standings/<int:year>')
def api_standings(year):
    return jsonify(f1_data.get_driver_standings(year))

@app.route('/api/lapstats/<int:year>/<int:round_num>')
def api_lap_stats(year, round_num):
    return jsonify(f1_data.get_race_data(year, round_num))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
