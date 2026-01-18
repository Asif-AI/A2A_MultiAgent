
FAKE_AVAILABILITY={
    "2025-11-09": "Available from 10:00 AM to 4:00 PM",
    "2025-11-11": "Available from 1:00 PM to 5:00 PM",
    "2025-11-15": "Available from 9:00 AM to 12:00 PM",
    "2025-11-20": "Available from 2:00 PM to 6:00 PM",
    "2025-11-25": "Busy throughout the day",
}

def get_availability(date_str: str) -> dict[str, str]:
    """Simulates checking Jeff's availability on a specific date.
    Args:
        date (str): The date to check availability for in 'YYYY-MM-DD' format.
    Returns:
        dict[str, str]: A dictionary containing availability information.   
    """
    if not date_str:
        return "Invalid date format. Please provide a date in 'YYYY-MM-DD' format."
    availability=FAKE_AVAILABILITY.get(date_str)
    if availability:
        return f"Jeff's availability on {date_str}: {availability}"
    return f"Jeff has no availability information for {date_str}."

  


    

    return FAKE_AVAILABILITY.get(date, "No availability information for this date.")
