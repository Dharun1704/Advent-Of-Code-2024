import os

import datetime as dt
day = (dt.datetime.now()).day
year = dt.datetime.now().year

prefix = f"day_{str(day).zfill(2)}"

if not prefix in os.listdir():
    os.mkdir(prefix)
    os.chdir(prefix)
    with open(f"./{prefix}_p1.py", "w") as fout:
        fout.write(f"""with open("./{prefix}/{prefix}.txt") as fin:
    lines = fin.readlines()

""")
    with open(f"./{prefix}_p2.py", "w") as fout:
        fout.write(f"""with open("./{prefix}/{prefix}.txt") as fin:
    lines = fin.readlines()

""")
    open(f"./{prefix}.txt", "w")
