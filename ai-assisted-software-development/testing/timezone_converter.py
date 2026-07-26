import pytz
from datetime import datetime

def convert_timezone(input_time, from_timezone, to_timezone):
    from_timezone_obj = pytz.timezone(from_timezone)
    to_timezone_obj = pytz.timezone(to_timezone)

    # If input_time is a string, parse it to a naive datetime first
    if isinstance(input_time, str):
        # Use the exact format your tests expect, e.g. "2024-01-01 12:00"
        input_time = datetime.strptime(input_time, "%Y-%m-%d %H:%M")

    # If it is already timezone-aware, don't re-localize
    if input_time.tzinfo is None:
        input_time = from_timezone_obj.localize(input_time)

    converted_time = input_time.astimezone(to_timezone_obj)
    return converted_time.strftime("%Y-%m-%d %H:%M")

# Example usage:
if __name__ == "__main__":
    # Input time in 'from_timezone' (UTC)
    input_time = datetime(2023, 9, 18, 12, 0, 0)  # Replace with your desired time

    # Convert from UTC to US/Pacific time zone
    from_timezone = 'UTC'
    to_timezone = 'US/Pacific'

    converted_time = convert_timezone(input_time, from_timezone, to_timezone)
    print(f"Converted time: {converted_time}")
