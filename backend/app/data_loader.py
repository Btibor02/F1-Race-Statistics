from app.f1_data import get_driver_standings
from app.models import DriverStanding
from app import db

def save_driver_standings(year):
    standings = get_driver_standings(year)
    round = int(standings[0].get('round', 1))
    if standings:
        for standing in standings:
            driver_id = standing['Driver']['driverId']
            position = int(standing['position'])
            points = float(standing['points'])
            wins = int(standing['wins'])

            existing_standing = DriverStanding.query.filter_by(driver_id=driver_id).first()

            if existing_standing:
                existing_standing.position = position
                existing_standing.points = points
                existing_standing.wins = wins
            else:
                driver_standing = DriverStanding(
                    season=year,
                    round=round,
                    driver_id=driver_id,
                    position=position,
                    points=points,
                    wins=wins
                )
                db.session.add(driver_standing)
        db.session.commit()
    else:
        print(f"No standings data found for {year}")