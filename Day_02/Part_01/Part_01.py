# Red-Nosed Reports

# Function to check if a report is safe
def is_safe(r):
    is_inc = True
    is_dec = True
    for i in range(len(r) - 1):
        diff = r[i + 1] - r[i]
        if not (1 <= abs(diff) <= 3):
            return False  # Differences must be valid
        if diff <= 0:
            is_inc = False
        if diff >= 0:
            is_dec = False
    return is_inc or is_dec  # Either increasing or decreasing

def main():
    with open("D:/AdventOFCode/Day_02/Part_01/input.txt", "r") as f:
        reports = [list(map(int, line.split())) for line in f.read().strip().split("\n")]

    safe_count = sum(is_safe(r) for r in reports)
    print(f"Number of safe reports: {safe_count}")

if __name__ == "__main__":
    main()
