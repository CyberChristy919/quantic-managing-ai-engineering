# Define the graph as a dictionary where keys are cities and values are lists of (destination, airfare) tuples.
graph = {}

# Read the airfare data from a file and populate the graph.
with open('airfares.txt', 'r') as file:
    for line in file:
        origin, destination, airfare = map(str.strip, line.split(' | '))  # Strip leading/trailing spaces
        airfare = float(airfare)
        
        if origin not in graph:
            graph[origin] = []
        graph[origin].append((destination, airfare))

# Function to find the optimal tour using TSP with memoization.
def tsp_dp(city, visited_cities):
    if not visited_cities:
        return [(city, 0)]

    # Calculate the minimum cost and sequence of cities.
    min_cost = float('inf')
    min_path = None

    for neighbor, cost in graph[city]:
        if neighbor not in visited_cities:
            new_visited = visited_cities.copy()
            new_visited.add(neighbor)
            path = tsp_dp(neighbor, new_visited)
            
            if path is not None:  # Check for None here
                total_cost = cost + path[0][1]

                if total_cost < min_cost:
                    min_cost = total_cost
                    min_path = [(city, cost)] + path

    return min_path

# Main function
def find_optimal_tour(start_city):
    visited_cities = set()
    visited_cities.add(start_city)
    return tsp_dp(start_city, visited_cities)

# Ask the user for a starting city
start_city = input("Enter the city you're starting in: ").strip().lower()

if start_city in graph:
    optimal_tour = find_optimal_tour(start_city)

    total_cost = sum(cost for _, cost in optimal_tour)

    print("\nOptimal Tour:")
    for city, cost in optimal_tour:
        print(f"City: {city.title()}, Cost: ${cost:.2f}")

    print(f"\nTotal Cost: ${total_cost:.2f}")
else:
    print("\nCity not found in the data.")
    print("Available starting cities:")
    for city in sorted(graph.keys()):
        print(city.title())
