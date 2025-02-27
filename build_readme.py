import os

solution_files = os.listdir("./leetcode")
headers = []
names = []
for f in solution_files:
    with open("./leetcode/" + f) as fi:
        headers.append(fi.readline()[1:].strip())
        names.append(fi.name[11:])

def cmp(x):
    x = x[1]
    n = 0
    for i in range(len(x)):
        if x[i] == "_":
            break
        n = n * 10 + int(x[i])
    return n
z = zip(headers, names)
z = sorted(list(z), key=cmp)

url = "https://github.com/rjmags1/cp/blob/main/leetcode/"
with open("./README.md", "w") as readme:
    for h, n in z:
        anchor = f"<h6><a href={url + n}>{h}</a></h6>"
        readme.write(anchor)
