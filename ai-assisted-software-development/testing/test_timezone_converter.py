import pytz
from pytz.exceptions import UnknownTimeZoneError
from datetime import datetime

def convert_timezone(input_time, from_timezone, to_timezone):
    try:
        from_timezone_obj = pytz.timezone(from_timezone)
        to_timezone_obj = pytz.timezone(to_timezone)
    except UnknownTimeZoneError:
        return "Invalid time zone provided"  # match test string exactly

    # If input_time is a string, parse it
    if isinstance(input_time, str):
        try:
            input_time = datetime.strptime(input_time, "%Y-%m-%d %H:%M")
        except ValueError:
            return "Invalid input time"      # adjust if tests expect different text

    # If datetime is naive, localize; if aware, leave as is
    if input_time.tzinfo is None:
        input_time = from_timezone_obj.localize(input_time)

    converted = input_time.astimezone(to_timezone_obj)
    return converted  # datetime, not string
