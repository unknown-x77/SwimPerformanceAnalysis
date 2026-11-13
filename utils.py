def time_to_seconds(time_string: str) -> float:
    parts = time_string.strip().split(":")

    if len(parts) == 1:
        return float(parts[0])
    if len(parts) == 2:
        minutes, seconds = parts
        seconds_value = float(seconds)
        if not 0 <= seconds_value < 60:
            raise ValueError("Seconds in a minutes:seconds time must be in [0, 60).")
        return int(minutes) * 60 + seconds_value

    raise ValueError("Time must be seconds or minutes:seconds.")