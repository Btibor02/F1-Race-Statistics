from app.f1_data import get_driver_standings, get_drivers, get_constructors, get_team_standings
from app.models import DriverStanding, Driver, Team, TeamStanding
from app import db

def save_drivers(year):
    drivers = get_drivers(year)
    if drivers:
        for driver in drivers:
            driver_id = driver['driverId']
            first_name = driver['givenName']
            last_name = driver['familyName']
            dob = driver['dateOfBirth']
            nationality = driver['nationality']
            code = driver['code']

            existing_driver = Driver.query.filter_by(driver_id=driver_id).first()
            if existing_driver:
                existing_driver.first_name = first_name
                existing_driver.last_name = last_name
                existing_driver.dob = dob
                existing_driver.nationality
                existing_driver.code = code
            else:
                new_driver = Driver(
                    driver_id=driver_id,
                    first_name=first_name,
                    last_name=last_name,
                    dob=dob,
                    nationality = nationality,
                    code = code
                )
                db.session.add(new_driver)
        db.session.commit()
    else:
        print(f"No driver data found for {year}")

def save_teams(year):
    constructors = get_constructors(year)
    if constructors:
        for constructor in constructors:
            constructor_id = constructor['constructorId']
            name = constructor['name']
            nationality = constructor['nationality']

            existing_team = Team.query.filter_by(team_id=constructor_id).first()
            if existing_team:
                existing_team.name = name
                existing_team.nationality = nationality
            else:
                new_team = Team(
                    team_id=constructor_id,
                    name=name,
                    nationality = nationality
                )
                db.session.add(new_team)
        db.session.commit()
    else:
        print(f"No constructor data found for {year}")

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

def save_team_standings(year):
    standings = get_team_standings(year)
    round = int(standings[0].get('round', 1))
    if standings:
        for standing in standings:
            team_id = standing['Constructor']['constructorId']
            position = int(standing['position'])
            points = float(standing['points'])
            wins = int(standing['wins'])

            existing_standing = TeamStanding.query.filter_by(team_id=team_id).first()

            if existing_standing:
                existing_standing.position = position
                existing_standing.points = points
                existing_standing.wins = wins
            else:
                team_standing = TeamStanding(
                    season=year,
                    round=round,
                    team_id=team_id,
                    position=position,
                    points=points,
                    wins=wins
                )
                db.session.add(team_standing)
        db.session.commit()
    else:
        print(f"No standings data found for {year}")