from random import score, freeze_answer
from solution import read_file

def group(photos):
	current_photo = photos[0]
	final_slides = [current_photo]

	unused_photos = set(photos) - {current_photo}
	used_photos = {current_photo}
	total_score = 0

	while len(unused_photos) > 0:
		used_photo = None
		max_score = -1

		for unused_photo in unused_photos:
			current_score = score(current_photo, unused_photo)
			if current_score > max_score:
				max_score = current_score
				used_photo = unused_photo

		final_slides.append(used_photo)
		total_score += max_score
		unused_photos.remove(used_photo)
		used_photos = used_photos.union({used_photo})
		current_photo = used_photo

	print(total_score)
	return final_slides

photos = read_file('data/a_example.txt')
slides = group(photos)
freeze_answer(slides, 'bibib2.txt')
