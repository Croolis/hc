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
        return str(self._id)
    
    def __repr__(self):
        return 'id: ' + str(self._id) + ', tags: ' + repr(self._tags)


def read_file(filename=None):
    if filename is None:
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

def make_pairs(photos):
    vertical = list(filter(lambda x: x.get_is_vertical(), photos))
    res = []
    used = []
    for pair in itertools.combinations(vertical, 2):
        tags1 = pair[0].get_tags()
        tags2 = pair[1].get_tags()
        id1 = pair[0].get_id()
        id2 = pair[1].get_id()
        if id1 not in used and id2 not in used:
            total_n_of_tags = len(tags1.union(tags2))
            # типа, какая доля тегов мы бы хотели чтоб совпадала
            cool_percent = total_n_of_tags * 0.4
            mutual_n_of_tags = len(tags1.intersection(tags2))
            if mutual_n_of_tags <= cool_percent and mutual_n_of_tags >= 1:
                tags = tags1.union(tags2)
                id = ' '.join([id1, id2])
                res.append(Photo(False, tags, id))
                used.extend([id1, id2])
    return res