
def is_safe(diffs):
    is_inc = all(d > 0 for d in diffs)
    is_dec = all(d < 0 for d in diffs)
    return is_inc or is_dec

def can_be_safe_with_removal(report):
    n = len(report)
    diffs = [report[i + 1] - report[i] for i in range(n - 1)]
    for i in range(n):
        if i == 0:
            new_diffs = diffs[1:]
        elif i == n - 1:
            new_diffs = diffs[:-1]
        else:
            new_diffs = diffs[:i - 1] + [report[i + 1] - report[i - 1]] + diffs[i + 1:]
        if all(1 <= abs(d) <= 3 for d in new_diffs) and is_safe(new_diffs):
            return True
    return False

def main():
    with open("D:\AdventOFCode\Day_02\Part_02\input.txt", "r") as file:
        reports = [list(map(int, line.split())) for line in file.read().strip().split("\n")]

    safe_count = 0
    for r in reports:
        diffs = [r[i + 1] - r[i] for i in range(len(r) - 1)]
        if all(1 <= abs(d) <= 3 for d in diffs) and is_safe(diffs):
            safe_count += 1
        elif can_be_safe_with_removal(r):
            safe_count += 1

    print(f"Number of safe reports with Problem Dampener: {safe_count}")

if __name__ == "__main__":
    main()
