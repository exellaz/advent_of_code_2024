# Answer: 398

from part1 import is_report_safe

if __name__ == "__main__":
    safe_reports = 0
    with open("input.txt") as file:
        for line in file:
            numbers = line.split()

            if is_report_safe(numbers) == True:
                safe_reports += 1
            else:
                for i in range(len(numbers)):
                    temp_numbers = numbers.copy()
                    temp_numbers.pop(i)

                    if is_report_safe(temp_numbers) == True:
                        safe_reports += 1
                        break

    print(safe_reports)
