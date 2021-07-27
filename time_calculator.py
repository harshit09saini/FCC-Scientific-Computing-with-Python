def add_time(start, duration, day=None):
    DAYS = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

    # Splits the given times into hours and minutes
    start_time, am_pm = start.split()
    start_hours, start_minutes = start_time.split(":")
    hours_to_add, minutes_to_add = duration.split(":")

    # Convert to 24 hour time
    if am_pm == "PM":
        start_hours_24 = int(start_hours) + 12
    else:
        start_hours_24 = int(start_hours)

    # Add minutes
    new_minutes = int(start_minutes) + int(minutes_to_add)
    # print(new_minutes)

    # Line to calculate the overflow hours and limit minutes between 0 to 59
    minutes_added = new_minutes % 60
    # print(minutes_added)
    overflow_hours = int(new_minutes / 60)
    # print(overflow_hours)

    # Add Hours
    new_hours = start_hours_24 + int(hours_to_add) + overflow_hours
    # print(new_hours)
    hours_added = int(new_hours % 24)
    # print(hours_added, minutes_added)
    days_passed = int(new_hours / 24)

    # Converting back to 12 hour clock
    # 24 hour clock
    # If less than 12, then AM. If greater or equal to 12, then PM and subtract to get 12 hour clock
    if hours_added < 12:
        am_pm = "AM"
    if hours_added >= 12:
        am_pm = "PM"
        hours_added -= 12
    if hours_added == 0:
        hours_added += 12

    # Get day of the week after adding
    new_day = None
    if day:
        current_day = day.title()
        if current_day in DAYS:
            current_day_index = DAYS.index(current_day)
            new_index = (current_day_index + days_passed) % 7
            new_day = DAYS[new_index]

    # Get sting formatted
    if day:
        if days_passed == 0:
            new_time = f"{hours_added}:{minutes_added:02d} {am_pm}, {new_day}"
        elif days_passed == 1:
            day_string = "(next day)"
            new_time = f"{hours_added}:{minutes_added:02d} {am_pm}, {new_day} {day_string}"
        else:
            day_string = f"({days_passed} days later)"
            new_time = f"{hours_added}:{minutes_added:02d} {am_pm}, {new_day} {day_string}"
    else:
        if days_passed == 0:
            new_time = f"{hours_added}:{minutes_added:02d} {am_pm}"
        elif days_passed == 1:
            day_string = "(next day)"
            new_time = f"{hours_added}:{minutes_added:02d} {am_pm} {day_string}"
        else:
            day_string = f"({days_passed} days later)"
            new_time = f"{hours_added}:{minutes_added:02d} {am_pm} {day_string}"

    return new_time
