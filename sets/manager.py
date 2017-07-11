import os


def Get_Sets():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sf_path = os.path.join(base_dir, 'sets', 'static', 'sets.txt')
    sf = open(sf_path, 'r')
    sets = sf.readlines()
    return sets
