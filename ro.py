import math
from collections import defaultdict
import sys
from copy import deepcopy
source = sys.argv[1]
destination = sys.argv[2]
routing_option = sys.argv[3]
routing_algorithm= sys.argv[4]
print "Building a graph....this may take about half a minute"
city=  tuple([[y for index, y in enumerate(x.strip().split(" ")) if y] for x in open("./city-gps.txt") if x.strip() != ""])
road_seg = tuple([[y for index, y in enumerate(x.strip().split(" ")) if y] for x in open("./road-segments.txt") if x.strip() != ""])

class City(object):

	def __init__(self, name, latitude=None, longitude=None):
		self.name = name
		self.latitude = latitude
		self.longitude = longitude

	def __eq__(self, other):
		return self.name==other.name

	def __hash__(self):
		return hash(self.name)

class Highway(object):

	def __init__(self, name, city_one , city_two, distance, speed_limit):
		self.name = name
		self.city_one = city_one
		self.city_two = city_two
		self.distance = distance
		self.speed_limit = speed_limit

highway_map = defaultdict(set)
# appending highways objects
road_set = set()
speed_limit, highway_count = 0,0
for h in road_seg:
	if len(h)==5 and float(h[3]):
		road_set.add(Highway(h[4], h[0], h[1], float(h[2]), float(h[3])))
		speed_limit += float(h[3])
		highway_count +=1
average_speed_limit = speed_limit/highway_count
list_of_cities=[]
for row in road_seg:
	list_of_cities.append(row[0])
	list_of_cities.append(row[1])
list_of_cities=list(set(list_of_cities))
city = list(city)
