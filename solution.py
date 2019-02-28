import sys

class Photo:
	def __init__(self, isVertical, tags):
		self._isVertical = isVertical
		self._tags = set(tags)
	def get_tags(self):
		return self._tags
	def get_isVertical(self):
		return self._isVertical

def read_file():
	filename = sys.argv[1]
	f = open(filename, 'r')
	# считывание количества линий
	f.readline()
	photos = []
	for line in f:
		splittedLine = line.split(' ')
		isVertical = splittedLine[0] == 'V'
		tags = splittedLine[2:]
		tags[-1] = tags[-1].replace("\n", "")
		photos.append(Photo(isVertical, tags))

	return photos
