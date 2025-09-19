# Traveling Salesman Problem solver for any n x n matrix
import sys

# Example distance matrix (can be replaced with any n x n matrix)
distances = [
    [0, 10, 15, 20, 25, 30],  # A
    [10, 0, 35, 25, 17, 28],  # B
    [15, 35, 0, 30, 28, 40],  # C
    [20, 25, 30, 0, 22, 16],  # D
    [25, 17, 28, 22, 0, 35],  # E
    [30, 28, 40, 16, 35, 0]   # F
]

# distances = [
#     [0, 29, 20, 21, 16, 31, 100, 12, 4, 31, 18, 23],   # A
#     [29, 0, 15, 29, 28, 40, 72, 21, 29, 41, 12, 25],   # B
#     [20, 15, 0, 15, 14, 25, 81, 9, 23, 27, 13, 17],    # C
#     [21, 29, 15, 0, 4, 12, 92, 12, 25, 13, 16, 28],    # D
#     [16, 28, 14, 4, 0, 16, 94, 9, 20, 16, 22, 27],     # E
#     [31, 40, 25, 12, 16, 0, 95, 24, 36, 3, 15, 19],    # F
#     [100, 72, 81, 92, 94, 95, 0, 90, 101, 99, 85, 77], # G
#     [12, 21, 9, 12, 9, 24, 90, 0, 15, 25, 19, 14],     # H
#     [4, 29, 23, 25, 20, 36, 101, 15, 0, 35, 18, 21],   # I
#     [31, 41, 27, 13, 16, 3, 99, 25, 35, 0, 20, 26],    # J
#     [18, 12, 13, 16, 22, 15, 85, 19, 18, 20, 0, 11],   # K
#     [23, 25, 17, 28, 27, 19, 77, 14, 21, 26, 11, 0]    # L
# ]

# City names (adjust to match matrix size)
cities = ['A', 'B', 'C', 'D', 'E', 'F']
# cities = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']

def validate_matrix(distances):
    n = len(distances)
    # Check if matrix is square
    for row in distances:
        if len(row) != n:
            raise ValueError("Distance matrix must be square")
    # Check symmetry and zero diagonal
    for i in range(n):
        if distances[i][i] != 0:
            raise ValueError("Diagonal elements must be zero")
        for j in range(n):
            if distances[i][j] != distances[j][i]:
                raise ValueError("Distance matrix must be symmetric")
            if distances[i][j] < 0:
                raise ValueError("Distances must be non-negative")
    return n

# Number of cities
try:
    n = validate_matrix(distances)
except ValueError as e:
    print(f"Error: {e}")
    sys.exit(1)

# Ensure cities list matches matrix size
if len(cities) != n:
    cities = [str(i) for i in range(n)]  # Use indices if cities list is invalid

# Initialize DP and path tables
dp = [[-1] * (1 << n) for _ in range(n)]
path = [[-1] * (1 << n) for _ in range(n)]

def tsp(pos, mask):
    # Base case: all cities visited
    if mask == (1 << n) - 1:
        return distances[pos][0]  # Return to city 0
    
    # If state already computed
    if dp[pos][mask] != -1:
        return dp[pos][mask]
    
    # Try visiting each unvisited city
    min_cost = sys.maxsize
    next_city = -1
    for city in range(n):
        if city != pos and not (mask & (1 << city)):
            cost = distances[pos][city] + tsp(city, mask | (1 << city))
            if cost < min_cost:
                min_cost = cost
                next_city = city
    
    dp[pos][mask] = min_cost
    path[pos][mask] = next_city
    return min_cost

def reconstruct_path():
    pos = 0
    mask = 1  # Start with city 0
    route = [0]
    while len(route) < n:
        next_city = path[pos][mask]
        if next_city == -1:
            break
        route.append(next_city)
        mask |= (1 << next_city)
        pos = next_city
    route.append(0)  # Return to city 0
    return route

def solve_tsp():
    # Compute minimum distance
    min_distance = tsp(0, 1)
    
    # Reconstruct route
    route_indices = reconstruct_path()
    route_cities = [cities[i] for i in route_indices]
    
    # Print results
    print("Shortest route:", " → ".join(route_cities))
    print("Total distance:", min_distance, "km")

# Run the solver
if __name__ == "__main__":
    solve_tsp()