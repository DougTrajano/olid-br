import datetime

def get_time_shift(value: datetime.datetime) -> str:
    """
    Get the time shift between the current time and the given time.
    
    Args:
        value (datetime.datetime): The time to compare.
        format (str, optional): The format of the time. Defaults to '%Y-%m-%d %H:%M:%S'.
    
    Returns:
        str: Morning, afternoon, evening or night.
    """
    if value.hour < 6:
        return "night"
    elif value.hour < 12:
        return "morning"
    elif value.hour < 18:
        return "afternoon"
    elif value.hour < 22:
        return "evening"
    else:
        return "night"
