import sys

class Photo:
	def __init__(self, isVertical, tags):
		self._isVertical = isVertical
		self._tags = set(tags)
	def get_tags(self):
		return self._tags
	def get_isVertical(self):
		return self._isVertical