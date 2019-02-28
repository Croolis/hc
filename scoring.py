def interest_factor(tags_set1, tags_set2):
	common = list(set(tags_set1).intersection(tags_set2))
	in_set1 = list(set(list1).difference(list2))
	in_set2 = list(set(list2).difference(list1))
	
	return min(len(common), len(in_set1), len(in_set2))

def score(slideshow_tagsets):
	score = 0
	if len(slideshow_tagsets) == 1:
		return score
	for i in range(len(slideshow_tagsets)):
		score += interest_factor(slideshow_tagsets[i], slideshow_tagsets[i+1])
	return score