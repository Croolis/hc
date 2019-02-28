from random import score, freeze_answer
from solution import read_file

def group(photos):
	unused_photos = set(photos)
	final_slides = []
	used_photos = set()
	total_score = 0
	for photo in photos:
		if photo in used_photos:
			continue

		used_photo = None
		max_score = -1

		for unused_photo in unused_photos:
			current_score = score(photo, used_photo)
			if current_score > max_score:
				max_score = current_score
				used_photo = unused_photo

		final_slides.append(used_photo)
		total_score += max_score
		unused_photos.remove(used_photo)
		used_photos.append(used_photo)

	print(total_score)
	return final_slides

photos = read_file()
slides = group(photos)
freeze_answer(slides, 'bibib2.txt')
