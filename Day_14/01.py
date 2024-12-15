# Import necessary libraries
import numpy as np

# Define constants
GRID_WIDTH = 101
GRID_HEIGHT = 103
TIME_SECONDS = 100

# Function to parse input
def parse_input(file_path):
    robots = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            px, py = map(int, parts[0][2:].split(','))
            vx, vy = map(int, parts[1][2:].split(','))
            robots.append(((px, py), (vx, vy)))
    return robots

# Function to simulate motion
def simulate_motion(robots, time):
    final_positions = []
    for (px, py), (vx, vy) in robots:
        # Calculate final position after `time` seconds
        final_x = (px + vx * time) % GRID_WIDTH
        final_y = (py + vy * time) % GRID_HEIGHT
        final_positions.append((final_x, final_y))
    return final_positions

# Function to count robots in quadrants
def count_quadrants(positions):
    mid_x = GRID_WIDTH // 2
    mid_y = GRID_HEIGHT // 2
    quadrant_counts = [0, 0, 0, 0]  # Q1, Q2, Q3, Q4

    for x, y in positions:
        if x == mid_x or y == mid_y:
            continue  # Ignore robots on dividing lines
        if x > mid_x and y < mid_y:
            quadrant_counts[0] += 1  # Q1
        elif x < mid_x and y < mid_y:
            quadrant_counts[1] += 1  # Q2
        elif x < mid_x and y > mid_y:
            quadrant_counts[2] += 1  # Q3
        elif x > mid_x and y > mid_y:
            quadrant_counts[3] += 1  # Q4

    return quadrant_counts

# Main function
def main():
    # Parse the input file
    robots = parse_input('input.txt')

    # Simulate motion for 100 seconds
    final_positions = simulate_motion(robots, TIME_SECONDS)

    # Count robots in each quadrant
    quadrant_counts = count_quadrants(final_positions)

    # Calculate the safety factor
    safety_factor = np.prod(quadrant_counts)

    print("Quadrant Counts:", quadrant_counts)
    print("Safety Factor:", safety_factor)

# Run the main function
if __name__ == "__main__":
    main()