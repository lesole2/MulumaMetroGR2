import heapq

class Graph:
    def __init__(self):
        self.routes = {}

    def add_city(self, name):
        if name not in self.routes:
            self.routes[name] = []

    def add_route(self, city1, city2, distance):
        self.add_city(city1)
        self.add_city(city2)
        self.routes[city1].append((city2, distance))
        self.routes[city2].append((city1, distance)) 

    def load_routes_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) != 3:
                        continue
                    city1, city2, distance = parts
                    self.add_route(city1.strip(), city2.strip(), int(distance.strip()))
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")

    def find_route(self, start, end):
        visited = set()
        distances = {city: float('inf') for city in self.routes}
        previous = {city: None for city in self.routes}
        distances[start] = 0

        queue = [(0, start)]
        while queue:
            current_dist, current_city = heapq.heappop(queue)

            if current_city == end:
                break

            if current_city in visited:
                continue
            visited.add(current_city)

            for neighbor, weight in self.routes.get(current_city, []):
                new_distance = current_dist + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current_city
                    heapq.heappush(queue, (new_distance, neighbor))

        if distances[end] == float('inf'):
            return None, float('inf')
        
        path = []
        city = end
        while city:
            path.insert(0, city)
            city = previous[city]
        return path, distances[end]

def main():
    graph = Graph()
    graph.load_routes_from_file("routes.csv")  # Replace with "routes.csv" if you're using .csv

    if not graph.routes:
        print("No routes were loaded. Exiting.")
        return

    while True:
        print("\nSouth Africa Travel Route Planner")
        start = input("Enter starting city: ").strip()
        end = input("Enter destination city: ").strip()

        if start not in graph.routes or end not in graph.routes:
            print("One or both cities not found in the route map.")
            continue

        path, distance = graph.find_route(start, end)
        if path:
            print(f"Route: {' -> '.join(path)}\nTotal distance: {distance} km")
        else:
            print("No route found between the selected cities.")

        again = input("Do you want to plan another route? (y/n): ").strip().lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main()