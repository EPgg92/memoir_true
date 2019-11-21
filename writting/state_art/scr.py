from pprint import pprint

a = [(len(line.split()), len(line), i, line)
     for i, line in enumerate(open("state_art.tex", "r").readlines())]
a = sorted(a)

pprint(a)
