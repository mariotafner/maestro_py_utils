import pytz
import random
import string
from datetime import datetime, timedelta

def test():
    print("maestro_py_utils")
    
def random_id():
    return ''.join(random.choices('abcdef0123456789', k=16))

def random_string(length: int, chars: str = (string.ascii_letters + string.digits)):
    return ''.join(random.choices(chars, k=length))

def datetime(custom_tz=None):
    if custom_tz is not None:
        now = datetime.now()
        now = now + timedelta(hours=custom_tz)
        return now
    else:
        tz = pytz.timezone("America/Sao_Paulo") 
        return datetime.now(tz)
    
def dateCompare(date1, date2):
    if not isinstance(date1, datetime) or not isinstance(date1, datetime):
        raise TypeError("date1 and date2 must be datetime objects")
    if date1 > date2:
        return 1
    elif date1 < date2:
        return -1
    else:
        return 0

def unitToSeconds(value, unit): # unit: seconds, minutes, hours, days, weeks, months, years
    if unit == 'seconds':
        return value
    elif unit == 'minutes':
        return value * 60
    elif unit == 'hours':
        return value * 60 * 60
    elif unit == 'days':
        return value * 60 * 60 * 24
    elif unit == 'weeks':
        return value * 60 * 60 * 24 * 7
    elif unit == 'months':
        return value * 60 * 60 * 24 * 30
    elif unit == 'years':
        return value * 60 * 60 * 24 * 365
    else:
        raise ValueError("unit must be seconds, minutes, hours, days, weeks, months or years")
    
def secondsToUnit(seconds, unit):
    if unit == 'seconds':
        return seconds
    elif unit == 'minutes':
        return seconds / 60
    elif unit == 'hours':
        return seconds / 60 / 60
    elif unit == 'days':
        return seconds / 60 / 60 / 24
    elif unit == 'weeks':
        return seconds / 60 / 60 / 24 / 7
    elif unit == 'months':
        return seconds / 60 / 60 / 24 / 30
    elif unit == 'years':
        return seconds / 60 / 60 / 24 / 365
    else:
        raise ValueError("unit must be seconds, minutes, hours, days, weeks, months or years")
    
def dateAdd(date, value, unit): # unit: seconds, minutes, hours, days, weeks, months, years, datetime
    if not isinstance(date, datetime):
        raise TypeError("date must be a datetime object")
    if unit == 'datetime':
        return date + timedelta(seconds=value)
    else:
        return date + timedelta(seconds=Utils.unitToSeconds(value, unit))
    
def secondsBetween(date1, date2):
    if not isinstance(date1, datetime) or not isinstance(date1, datetime):
        raise TypeError("date1 and date2 must be datetime objects")
    
    return abs((date2 - date1).total_seconds())

def dateToJsDate(date):
    if not isinstance(date, datetime):
        return None
    return str(date).replace(' ', 'T')

def fill_zeros(value, length):
    return str(value).zfill(length)

def randomize_list(list):
    random.shuffle(list)
    return list

def random_int(min, max):
    return random.randint(min, max)

def seconds_to_duration(seconds):
    units = [
        (24 * 3600, "dia"),
        (3600, "hora"),
        (60, "minuto"),
        (1, "segundo"),
    ]
    result = []
    for divisor, unit in units:
        value, seconds = divmod(seconds, divisor)
        if value > 0:
            result.append(f"{value} {unit}{'s' if value > 1 else ''}")

    if len(result) > 1:
        return " e ".join([", ".join(result[:-1]), result[-1]])
    else:
        return result[0]
    
# Split an array or string into chunks
def split_chunks(array, chunk_size=1):
    return [array[i:i+chunk_size] for i in range(0, len(array), chunk_size)]

def random_choice(array):
    return random.choice(array)

def string_pad_left(string, length, char=' '):
    return char * (length - len(string)) + string

def string_pad_right(string, length, char=' '):
    return string + char * (length - len(string))

def remove_duplicated_spaces(text):
    return ' '.join(text.split())

def date_weekday(date):
    return [1,2,3,4,5,6,0][date.weekday()]

def datetime_set_time(datetime, time):
    hours, minutes, seconds = time.split(':')
    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)
    return datetime.replace(hour=hours, minute=minutes, second=seconds, microsecond=0)