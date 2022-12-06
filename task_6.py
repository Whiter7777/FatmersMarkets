d = {}

with open("Export.csv", "r") as inf:
    for line in inf:
        line = line.strip().split(",")
        d[line[0]] = line[1:]
print(d)

city = "Danville"

for val in d.values():
   if val[7] == city:
       print(val[0], val[7], val[9], val[19], val[20])

