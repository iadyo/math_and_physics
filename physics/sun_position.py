# Nieskończone, pozycja słońca - Python
# Stworzone przez Adrian 'adyo'

from datetime import datetime
from time import sleep
from os import system
from math import *

def julday(year, month, day, hour, minutes, seconds, ms):
    L1 = year + 4716 - int((14 - month) / 12)
    M1 = (month + 9) % 12
    G = int(0.75 * int((L1 + 184) / 100)) - 38
    return (int(365.25 * L1) + int(30.6 * M1 + 0.4) + day - G - 1402) - 0.5 + hour / 24 + minutes / 24 / 60 + seconds / 24 / 3600 + ms / 24 / 3600 / 1000000

def is_leap_year(year):
    return ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))

def hhmmss(value):
    hh = value // 15
    mm = int((value / 15 - hh) * 60)
    ss = value / 15 * 3600 - hh * 3600 - mm * 60
    return hh + 1, mm, ss

def convert_time(x):
    return '{:02d}:{:02d}:{:02d}'.format(int(hhmmss(x)[0]), int(hhmmss(x)[1]), int(hhmmss(x)[2]))

def calc_sun_pos(lat, lon):
    dutc = datetime.utcnow()
    hour = dutc.hour + dutc.minute / 60 + dutc.second / 3600 + dutc.microsecond / 3600000000
    doy = dutc.timetuple().tm_yday

    if is_leap_year(dutc.year): gamma = ((2 * pi) / 366) * (doy - 1 + ((hour - 12) / 24))
    else: gamma = ((2 * pi) / 365) * (doy - 1 + ((hour - 12) / 24))

    eqtime = 229.18 * (0.000075 + 0.001868 * cos(gamma) - 0.032077 * sin(gamma) - 0.014615 * cos(2 * gamma) - 0.040849 * sin(2 * gamma))
    decl = degrees(0.006918 - 0.399912 * cos(gamma) + 0.070257 * sin(gamma) - 0.006758 * cos(2 * gamma) + 0.000907 * sin(2 * gamma) - 0.002697 * cos(3 * gamma) + 0.00148 * sin(3 * gamma))
    time_offset = eqtime + 4 * lon - 60 * 1
    tst = (dutc.hour + 1) * 60 + dutc.minute + dutc.second / 60 + dutc.microsecond / 3600000000 * 60 + time_offset
    ha = tst / 4 - 180
    alt = degrees(asin(sin(radians(decl)) * sin(radians(lat)) + cos(radians(decl)) * cos(radians(lat)) * cos(radians(ha))))
    ha = degrees(acos(cos(radians(90.833)) / (cos(radians(lat)) * cos(radians(decl))) - tan(radians(lat)) * tan(radians(decl))))
    sunrise = (720 - 4 * (lon + ha) - eqtime) / 60 * 15
    snoon = (720 - 4 * (lon - ha) - eqtime) / 60 * 15
    
    print('\n\tAltitude: {}'.format(alt))
    print('\tSunrise: {}'.format(convert_time(sunrise)))
    print('\tSnoon: {}'.format(convert_time(snoon)))

# def get_lunar_phase(julday):
    # D = (297.85 + 12.19074912 * (julday - 2451545)) % 360

    # x = ''.format(D)
    # if D >= 0: x += 'new moon'
    # elif D >= 90: x += 'first quarter'
    # elif D >= 180: x += 'full moon'
    # else: x += 'none'

    # return x

    # D = ((datetime(2000, 1, 6) - datetime.today()).days) / 1000
    # n = 29.53058770576
    # M = D / n
    # lunar_day = (D % n) * M

    # if 0 < lunar_day <= 1: return 'New Moon'
    # elif 1 < lunar_day <= 6.382647: return 'Waxing Crescent'
    # elif 6.382647 < lunar_day <= 8.382647: return 'First Quarter'
    # elif 8.382647 < lunar_day <= 13.765294: return 'Waxing Gibbous'
    # elif 13.765294 < lunar_day <= 15.765294: return 'Full Moon'
    # elif 15.765294 < lunar_day <= 21.147941: return 'Waning Gibbous'
    # elif 21.147941 < lunar_day <= 23.147941: return 'Last Quarter'
    # elif 23.147941 < lunar_day <= 28.530588: return 'Waning Crescent'
    # elif 28.530588 < lunar_day <= 29.530588: return 'New Moon'
    # else: return -1

if __name__ == '__main__':
    lat, lon = 51.110550, 17.025560   # Wrocław
    refresh = 0.01

    try:
        while True:
            system('cls')
            dutc = datetime.utcnow()
            dl = datetime.now()
            year, month, day = dutc.year, dutc.month, dutc.day
            hour, minutes, seconds, ms = dutc.hour, dutc.minute, dutc.second, dutc.microsecond
            jl = julday(year, month, day, hour, minutes, seconds, ms)

            print('\n\tLocal Time: {}'.format(dl))
            print('\tUniversal Time: {}'.format(dutc))
            print('\tJulian Day: {}'.format(jl))
            calc_sun_pos(lat, lon)
            # print('\n\tLunar phase: {}'.format(get_lunar_phase(jl)))

            if refresh == 0.: break
            else: sleep(1 * refresh)
    except KeyboardInterrupt:
        print('Zatrzymano przez użytkownika!')
