# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

def bold(str):
    return '\033[1m' + str + '\033[0m'

# YOUR CODE HERE
class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        self.name = name
        super().__init__(lat, lon)
    
    # def print_waypoint(self):
    #     print(f'"{self.name}", {self.lat}, {self.lon}')

    def __str__(self):
        s = "--------------------Waypoint\n" + bold("Name: ") + self.name + "\n" + bold("Latitiude: ") + str(self.lat) + "\n" + bold("Longitude: ") + str(self.lon) + "\n----------------------------"
        
        # for value in dir(self):
        #     if not value.startswith("__"):
        #         s += (f"{value}: " + str(getattr(self, value)) + "\n")
        # 
        # Output: 
        # lat: 41.70505
        # lon: -121.51521
        # name: Catacombs

        return s

# TESTING
# w = Waypoint('North Pole', 90, 0)
# print(w.name)
# print(w.lat)
# print(w.lon)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?



# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        self.difficulty = difficulty
        self.size = size
        super().__init__(name, lat, lon)

    def __str__(self):
        s = "--------------------Geocache\n" + bold("Name: ") + self.name + "\n" + bold("Difficulty: ") + str(self.difficulty) + "\n" + bold("Size: ") + str(self.size) + "\n" + bold("Latitiude: ") + str(self.lat) + "\n" + bold("Longitude: ") + str(self.lon) + "\n----------------------------"
        return s
        
# TESTING
# g = Geocache('North Pole', "near impossible", "bigger than a loaf of bread", 90, 0)
# print(g.name)
# print(g.difficulty)
# print(g.size)
# print(g.lat)
# print(g.lon)

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
waypoint = Waypoint("Catacombs", 41.70505, -121.51521)
print(f'"{waypoint.name}", {waypoint.lat}, {waypoint.lon}')

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(geocache)
