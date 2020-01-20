import sys
from math import pi

# theory (to be proven): it's never quicker to travel 
# down a street (towards the circle center), along a 
# canal, then back up another street.

# it is always better to take canals closer to the
# city center than farther out

# one of these two assumptions has failed, as evidenced by a failure on sample input 2 (where traveling along the radius is way quicker than around the circumference) Needs revision.

class Amsterdam:
	"""A model of Amsterdam"""
	def __init__(self, segs, rings, radius):
		self.segs = segs
		self.rings = rings
		self.radius = radius

	def thetalen(self, depth, width=1):
		"""Gets the length of a curved segment. `depth` is how many half-circles away from the center of the city the calculation is being done at. `width` is how many segments are being counted. """
		if not 0 <= depth <= self.rings or not 0 <= width <= self.segs:
			raise ValueError("Coords not within Amsterdam")

		r = self.radius * depth / self.rings
		return pi * r * width / self.segs

	def radlen(self, depth=1):
		"""Gets the length of a curved segment. `depth` is how many segments are being counted. """
		return self.radius * depth / self.rings

	def pathlen(self, start, end):
		try: start, end = self._to_coords(start), self._to_coords(end)
		except:
			raise ValueError("Arguments not in proper format")

		if any(not 0 <= i.t <= self.segs for i in (start, end)) \
		or any(not 0 <= i.r <= self.rings for i in (start, end)):
			raise ValueError("Coords not within Amsterdam")

		path = 0.

		# first, navigate to the lower radial coord (could already be there)
		path += self.radlen(abs(start.r - min(start.r, end.r)))

		# then, navigate around the half-circle
		path += self.thetalen(min(start.r, end.r), abs(start.t - end.t))

		# lastly, move up to the end point (if not already there)
		path += self.radlen(abs(end.r - min(start.r, end.r)))

		return path

	def _to_coords(self, coord):
		"""Convert a 2-tuple to a coordinate object with r (radial) and t (theta) properties"""
		return type("Coordinates", (), {"t":int(coord[0]), "r":int(coord[1])})

segs, rings, rad = sys.stdin.readline().split()
am = Amsterdam(int(segs), int(rings), float(rad))

st, sr, et, er = sys.stdin.readline().split()


print(am.pathlen((st, sr), (et, er)))