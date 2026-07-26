import pytz
from datetime import datetime
from pytz.exceptions import UnknownTimeZoneError

def convert_timezone(input_time, from_timezone, to_timezone):
    try:
        from_timezone_obj = pytz.timezone(from_timezone)
        to_timezone_obj = pytz.timezone(to_timezone)
    except UnknownTimeZoneError:
        return "Invalid timezone"

    # If input_time is a string, parse it
    if isinstance(input_time, str):
        try:
            input_time = datetime.strptime(input_time, "%Y-%m-%d %H:%M")
        except ValueError:
            return "Invalid input time"

    # If datetime is naive, localize; if aware, leave as is
    if input_time.tzinfo is None:
        input_time = from_timezone_obj.localize(input_time)

    converted = input_time.astimezone(to_timezone_obj)
    return converted.strftime("%Y-%m-%d %H:%M")

# Example usage:
if __name__ == "__main__":
    # Input time in 'from_timezone' (UTC)
    input_time = datetime(2023, 9, 18, 12, 0, 0)  # Replace with your desired time

    # Convert from UTC to US/Pacific time zone
    from_timezone = 'UTC'
    to_timezone = 'US/Pacific'

    converted_time = convert_timezone(input_time, from_timezone, to_timezone)
    print(f"Converted time: {converted_time}")
