def roll_call_dwarves(dwarves):
    for i, name in enumerate(dwarves, start=1):
        print(f"{i}. {name}")

def summon_captain_planet(planeteer_calls=["earth", "wind", "fire", "water", "heart"]):
    capitalize_calls = [calls.capitalize() + '!' for calls in planeteer_calls]
    return capitalize_calls


def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(strings):
    soup = ["tomato soup", "cheddar", "oyster crackers", "gouda"]

    for string in strings:
        if string.lower() in soup:
            return string

    return None
