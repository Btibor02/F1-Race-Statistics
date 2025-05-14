import requests
import fastf1

ERGAST_BASE = "https://ergast.com/api/f1"

def get_drivers(year):
    url = f"{ERGAST_BASE}/{year}/drivers.json"
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()['MRData']['DriverTable']['Drivers']
    return []

def get_constructors(year):
    url = f"{ERGAST_BASE}/{year}/constructors.json"
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()['MRData']['ConstructorTable']['Constructors']
    return []

def get_season_schedule(year):
    url = f"{ERGAST_BASE}/{year}.json"
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()['MRData']['RaceTable']['Races']
    return []

def get_race_results(year, round_num):
    url = f"{ERGAST_BASE}/{year}/{round_num}/results.json"
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()['MRData']['RaceTable']['Races'][0]['Results']
    return []

def get_driver_standings(year):
    url = f"{ERGAST_BASE}/{year}/driverStandings.json"
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']
    return []

def get_race_data(season, round_num):
    try:
        session = fastf1.get_session(season, round_num, 'R')
        session.load()
        laps = session.laps.pick_quicklaps()
        fastest_laps = laps.groupby('Driver')['LapTime'].min().sort_values()
        return {
            "fastest_laps": {driver: str(time) for driver, time in fastest_laps.items()}
        }
    except Exception as e:
        return {"error": str(e)}
