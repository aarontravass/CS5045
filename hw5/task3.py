# create a sample file
f = open("input.txt", "w")
for i in range(1, 100):
    f.write("This is a sample line with number - " + str(i) + "\n")
f.close()

f = open("input.txt", "r")
outfile = open("copyofinput.txt", "w")
cnt = 1
for line in f:
    if (cnt % 2 == 1):
        outfile.write("Line " + str(cnt) + ": " + line)
    cnt += 1
outfile.close()
