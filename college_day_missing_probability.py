def calculate_attendance(current="", consecutive_missed=0, current_day=0, total_days=10, miss_flag=False, total_ways=0, last_day_missed_count=0):
    if consecutive_missed >= 4 or miss_flag:
        return total_ways, last_day_missed_count

    if current_day == total_days:
        if current[-1] == 'A':
            last_day_missed_count += 1
        total_ways += 1
        return total_ways, last_day_missed_count

    total_ways, last_day_missed_count = calculate_attendance(current + 'P', 0, current_day + 1, total_days, miss_flag, total_ways, last_day_missed_count)
    total_ways, last_day_missed_count = calculate_attendance(current + 'A', consecutive_missed + 1, current_day + 1, total_days, miss_flag, total_ways, last_day_missed_count)
    return total_ways, last_day_missed_count


days = 10
total_ways, last_day_missed_count = calculate_attendance("", 0, 0, days, False, 0, 0)
print(f"{last_day_missed_count}/{total_ways}")
