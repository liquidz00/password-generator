import random


def shuffle(pwd=None):
    list_shuffled = list(pwd)
    random.shuffle(list_shuffled)
    pwd = "".join(list_shuffled)
    return pwd
