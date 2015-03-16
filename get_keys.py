import os, shutil
from sys import argv
import xml.etree.ElementTree as ET
import itertools

string_names = open('string_names.txt', 'w')

def parse(_file):
    l = []
    tree = ET.parse(_file)
    root = tree.getroot()
    for string in root:
        l.append(string.get('name'))
    return l

def get_keys(path_to_res):
    big_l = []
    for root, dirs, files in os.walk(path_to_res):
        for f in files:
            little_l = parse(os.path.join(root, f))
            big_l.append(little_l)
    return big_l

def main(path_to_res):
    big_l = get_keys(path_to_res)
    combined = list(itertools.chain.from_iterable(big_l))
    for name in combined:
        name = str(name)
        string_names.write(name +'\n')
    string_names.close()

if __name__ == "__main__":
        main(argv[1])
