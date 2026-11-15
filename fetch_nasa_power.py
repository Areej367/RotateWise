"""Fetch NASA POWER long-term monthly climatology (temperature, rainfall) for the
regions used by RotateWise and print lines ready to paste into the `R` object
in index.html.  Requires: pip install requests
"""
import requests

PLACES = {
    "sindh":  ("Sindh, Pakistan", 25.39, 68.37),
    "punjab": ("Punjab plains, Pakistan", 31.42, 73.08),
    "poth":   ("Pothohar plateau, Pakistan (rainfed)", 32.93, 72.86),
    "india":  ("Maharashtra, India", 21.15, 79.09),
    "kenya":  ("Rift Valley highlands, Kenya", -0.30, 36.08),
    "spain":  ("Murcia, Spain (Mediterranean)", 37.98, -1.13),
    "iowa":   ("Iowa, USA (Midwest)", 41.59, -93.62),
    "brazil": ("Goias, Brazil (Cerrado)", -16.68, -49.25),
}
MONTHS = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
DAYS = [31, 28.25, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
URL = "https://power.larc.nasa.gov/api/temporal/climatology/point"

for key, (name, lat, lon) in PLACES.items():
    r = requests.get(URL, params={
        "parameters": "T2M,PRECTOTCORR", "community": "AG",
        "latitude": lat, "longitude": lon, "format": "JSON"}, timeout=60)
    r.raise_for_status()
    p = r.json()["properties"]["parameter"]
    t = [round(p["T2M"][m], 1) for m in MONTHS]
    rain = [round(p["PRECTOTCORR"][m] * d) for m, d in zip(MONTHS, DAYS)]  # mm/day -> mm/month
    if min(t) < -900 or min(rain) < 0:
        print("WARNING: missing data for", key)
    print(f'{key}:{{n:"{name}",t:{t},r:{rain}}},')
