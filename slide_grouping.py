from random import score, freeze_answer
from solution import read_file

from time import time

def group(photos):
	used = [0] * len(photos)
	current_photo = photos[0]
	used[0] = 1

	final_slides = [current_photo]

	total_score = 0

	counter = 1
	while counter < len(photos):
		counter += 1
		max_score = -1

		if counter % 1000 == 0:
			print(counter)

		for i in range(len(photos)):
			if used[i] == 1:
				continue
			unused_photo = photos[i]

			current_score = score(current_photo, unused_photo)
			if current_score > max_score:
				max_score = current_score
				used_photo_index = i

		final_slides.append(photos[used_photo_index])
		used[used_photo_index] = 1
		total_score += max_score

		current_photo = photos[used_photo_index]
		if counter % 1000 == 0:
			print(time())

	print(total_score)
	return final_slides


photos = read_file('data/b_lovely_landscapes.txt')
slides = []
for i in range(10):
	slides += group(photos[8000 * i:8000 * (i + 1)])
freeze_answer(slides, 'bibib2.txt')
