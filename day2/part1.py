# Answer: 332

def is_report_safe(numbers):
    is_ascending = False
    is_descending = False
    max_index = len(numbers) - 1

    for i in range(max_index):
        diff = int(numbers[i + 1]) - int(numbers[i])

        if diff > 0:
            is_ascending = True
        else:
            is_descending = True
        if is_ascending and is_descending:
            return False

        abs_diff = abs(diff)
        if abs_diff < 1 or abs_diff > 3:
            return False
    return True

if __name__ == "__main__":
    safe_reports = 0
    with open("input.txt") as file:
        for line in file:
            numbers = line.split()

            if is_report_safe(numbers) == True:
                safe_reports += 1

    print(safe_reports)
