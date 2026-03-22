from skyfield.api import load, utc
import datetime as dt

# Create a timescale and ask the current time.
ts = load.timescale()
t = ts.from_datetime(dt.datetime(1531, 12, 12, 6, 45, tzinfo=utc) - dt.timedelta(hours=6))

# Load the JPL ephemeris DE421 (covers 1900-2050).
planets = load('de421.bsp')
earth, mars = planets['earth'], planets['mars']

# What's the position of Mars, viewed from Earth?
astrometric = earth.at(t).observe(mars)
ra, dec, distance = astrometric.radec()

print(ra)
print(dec)
print(distance)