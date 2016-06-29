def find_floor(drop):
    highest_safe_floor = 0
    known_unsafe_floor = 100
    first_egg_interval = 14
    eggs_left = 2

    while eggs_left == 2:
        floor_to_drop_at = highest_safe_floor + first_egg_interval
        does_break = drop(floor_to_drop_at)
        if does_break:
            known_unsafe_floor = floor_to_drop_at
            eggs_left -= 1
        else:
            highest_safe_floor = highest_safe_floor + first_egg_interval
            first_egg_interval -= 1

    while eggs_left == 1:
        floor_to_drop_at = highest_safe_floor + 1
        if floor_to_drop_at == known_unsafe_floor:
            return highest_safe_floor

        does_break = drop(floor_to_drop_at)
        if does_break:
            eggs_left -= 1
        else:
            highest_safe_floor = floor_to_drop_at

    return highest_safe_floor
