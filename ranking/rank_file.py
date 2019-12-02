import os.path
from os import path
# import re
import sorting
import csv
import pandas as pd

def rank_fun(rep, url):
    if path.exists('rank_file.txt'):
        f = open('rank_file.txt', 'r')
        fl = f.readlines()
        f.close()
        new_line1 = "%s " % rep + " %s \n" % url
        flset = list(set(fl))
        if new_line1 not in flset:
            f = open("rank_file.txt", "a")
            f.write(new_line1)
        f.close()
    else:
        fo = open('rank_file.txt', 'w+')
        fo.write("%s " % rep + " %s \n" % url)
        fo.close()
    with open('rank_file.txt', 'r') as f1:
        content = f1.readlines()
        content.sort(key=sorting.nat_keys, reverse=True)

    with open('rank_file.txt', 'w') as f2:
        for l1 in content:
            f2.write('%s\n' % l1)


    with open('rank_file.txt', 'r') as in_file:
        stripped = (line.strip() for line in in_file)
        lines = (line.split(",") for line in stripped if line)
        with open('log.csv', 'w+') as out_file:
            writer = csv.writer(out_file)
            writer.writerow(('rep', 'url'))
            writer.writerows(lines)

    data = pd.read_csv("log.csv")
    data["Rank"] = data["rep"].rank(ascending=0)
    data.sort_values("rep", inplace=True)
    print(data)


