import numpy as np
from time import time

from solution import Photo, read_file


def score(photo1: Photo, photo2: Photo):
    s1 = photo1.get_tags()
    s2 = photo2.get_tags()
    a1 = len(s1 - s2)
    a2 = len(s2 - s1)
    a3 = len(s1 & s2)

    return min(a3, min(a1, a2))


def freeze_answer(photos, res, filename=None):
    if filename is None:
        filename = str(int(time()))

    out = open(filename, 'w')
    out.write(str(res) + '\n')
    for photo in photos:
        out.write(photo.get_id() + '\n')


def random_solution(photos, best_res=None, tries=10):
    if not best_res:
        best_res = 0

    for _ in range(tries):
        res = 0

        for i in range(len(photos) - 1):
            res += score(photos[i], photos[i + 1])

        if res > best_res:
            print(res)
            best_res = res
            freeze_answer(photos, best_res, 'bibib1')

        np.random.shuffle(photos)


photos = read_file('data/a_example.txt')
random_solution(photos)
