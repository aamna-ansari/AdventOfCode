def read_input(file_path):
    """Reads the input file and returns the topographic map as a list of lists."""
    with open(file_path, 'r') as f:
        return [list(map(int, line.strip())) for line in f.readlines()]

def find_trailheads(topographic_map):
    """Find all trailhead positions in the map (positions with height 0)."""
    return [(i, j) for i, row in enumerate(topographic_map) for j, value in enumerate(row) if value == 0]

def dfs_count_trails(map_, x, y, height, visited):
    """Recursive DFS to count distinct hiking trails."""
    # Check bounds and validity
    if not (0 <= x < len(map_) and 0 <= y < len(map_[0])):
        return 0
    if map_[x][y] != height or visited[x][y]:
        return 0

    # Mark current position as visited
    visited[x][y] = True

    # If the current height is 9, count this trail and stop
    if height == 9:
        visited[x][y] = False  # Backtrack for other trails
        return 1

    # Explore neighbors
    total_trails = 0
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        total_trails += dfs_count_trails(map_, x + dx, y + dy, height + 1, visited)

    # Backtrack to allow other trails to reuse this cell
    visited[x][y] = False
    return total_trails

def calculate_total_ratings(map_):
    """Calculate the total rating of all trailheads."""
    trailheads = find_trailheads(map_)
    visited = [[False] * len(map_[0]) for _ in range(len(map_))]
    total_rating = 0

    for x, y in trailheads:
        if not visited[x][y]:  # Only start DFS if not already part of another trail
            total_rating += dfs_count_trails(map_, x, y, 0, visited)

    return total_rating

def main():
    fn ='D:/AdventOFCode/Day_10/input.txt'
    topographic_map = read_input(fn)
    total_rating = calculate_total_ratings(topographic_map)
    print(f"Total rating of all trailheads: {total_rating}")

if __name__ == "__main__":
    main()
