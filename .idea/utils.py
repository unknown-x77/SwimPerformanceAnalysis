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


def get_num_of_50s(distance): # Number of 50s in a event
    length = {
        50: 1,
        100: 2,
        200: 4,
        400: 8,
        500: 10,
        800: 16,
        1000: 20,
        1500: 30,
        1650: 33
    }
    return length.get(distance)


def parse_swim_line(line: str) -> dict:
    # Cut into 4 pieces; the last piece keeps all the splits together
    pieces = line.strip().split(" ", 3)
    if len(pieces) != 4:
        raise ValueError(f"Expected 'distance stroke course splits', got: {line!r}")

    distance = int(pieces[0])
    stroke = pieces[1]
    course = pieces[2]

    # Split the last piece on commas, convert each to seconds
    splits = [time_to_seconds(s) for s in pieces[3].split(",")]

    # Make sure the number of splits matches the distance
    expected = get_num_of_50s(distance)
    if expected is None:
        raise ValueError(f"Unknown distance: {distance}")
    if len(splits) != expected:
        raise ValueError(
            f"A {distance} should have {expected} splits, but found {len(splits)}: {line!r}"
        )

    return {
        "distance": distance,
        "stroke": stroke,
        "course": course,
        "splits": splits,
    }


if __name__ == "__main__":
    with open("testtimes.txt", "r") as file:
        for line in file:
            if line.strip() == "":
                continue  # skip blank lines
            print(parse_swim_line(line))