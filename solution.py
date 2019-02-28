import sys

class Photo:
	def __init__(self, is_vertical, tags, id):
		self._is_vertical = is_vertical
		self._tags = set(tags)
		self._id = id

	def get_tags(self):
		return self._tags

	def get_is_vertical(self):
		return self._is_vertical

	def get_id(self):
		return self._id

def read_file():
	filename = sys.argv[1]
	f = open(filename, 'r')
	# считывание количества линий
	f.readline()
	photos = []
	id = 0
	for line in f:
		splittedLine = line.split(' ')
		isVertical = splittedLine[0] == 'V'
		tags = splittedLine[2:]
		tags[-1] = tags[-1].replace("\n", "")
		photos.append(Photo(isVertical, tags, id))
		id += 1

	return photos
