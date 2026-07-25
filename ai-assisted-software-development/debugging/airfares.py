import itertools

graph = {}

with open('airfares.txt', 'r') as file:
    for line in file:
        parts = [part.strip() for part in line.strip().split('|')]

        if len(parts) != 3:
            print(f"Skipping bad line: {line}")
            continue

        origin, destination, airfare = parts
        airfare = float(airfare)

        origin = origin.lower()
        destination = destination.lower()

        if origin not in graph:
            graph[origin] = []
        graph[origin].append((destination, airfare))

def calculate_path_cost(path):
    total_cost = 0.0
    for i in range(len(path) - 1):
        origin, destination = path[i], path[i + 1]
        found = False

        for dest, cost in graph.get(origin, []):
            if dest == destination:
                total_cost += cost
                found = True
                break

        if not found:
            return float('inf')

    return total_cost

def find_optimal_tour(start_city):
    all_cities = list(graph.keys())

    if start_city not in all_cities:
        return None, None

    all_cities.remove(start_city)
    optimal_tour = None
    min_cost = float('inf')

    for permuted_cities in itertools.permutations(all_cities):
        tour = [start_city] + list(permuted_cities) + [start_city]
        tour_cost = calculate_path_cost(tour)

        if tour_cost < min_cost:
            min_cost = tour_cost
            optimal_tour = tour

    return optimal_tour, min_cost

print("Available starting cities:")
for city in sorted(graph.keys()):
    print(city.title())

start_city = input("Enter the city you're starting in: ").strip().lower()

if start_city in graph:
    optimal_tour, total_cost = find_optimal_tour(start_city)

    if optimal_tour is None or total_cost == float('inf'):
        print("No complete tour found.")
    else:
        print("Optimal Tour:")
        for city in optimal_tour:
            print(f"City: {city.title()}")
        print(f"Total Cost: ${total_cost:.2f}")
else:
    print("City not found in the data.")
