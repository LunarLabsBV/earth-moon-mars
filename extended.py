pip install skyfield

from skyfield.api import load, Topos
from datetime import datetime

def calculate_positions(current_time):
    # Load the solar system ephemeris
    eph = load('de421.bsp')

    # Select Earth, Moon, and Mars from the ephemeris
    earth, moon, mars = eph['earth'], eph['moon'], eph['mars']

    # Calculate the positions of Earth, Moon, and Mars at the given time
    ts = load.timescale()
    t = ts.utc(current_time.year, current_time.month, current_time.day,
               current_time.hour, current_time.minute, current_time.second)
    earth_pos = earth.at(t).position.km
    moon_pos = moon.at(t).position.km
    mars_pos = mars.at(t).position.km

    return earth_pos, moon_pos, mars_pos

def main():
    current_time = datetime(2024, 2, 29, 12, 0, 0)  # Example time (year, month, day, hour, minute, second)
    earth_pos, moon_pos, mars_pos = calculate_positions(current_time)
    
    print("Earth's position (km):", earth_pos)
    print("Moon's position (km):", moon_pos)
    print("Mars's position (km):", mars_pos)

if __name__ == "__main__":
    main()
