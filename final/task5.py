def getAvg(l):
    return sum([i[1] for i in l]) / (len(l) * 1.0)


def getMax(l):
    mx = l[0][1]
    for i in l:
        mx = max(mx, i[1])
    return mx


def getMin(l):
    mx = l[0][1]
    for i in l:
        mx = min(mx, i[1])
    return mx


def checkName(name: str, l):
    for i in l:
        if name == i[0]:
            return i[1]
    return None


file = open('exam.txt', 'r')
lines = [(student.strip().split(' ')[0].strip(), int(student.strip().split(' ')[-1].strip())) for student in
         file.readlines()]
file.close()
print("Average Score:", getAvg(lines))
print("Max score:", getMax(lines))
print("Min score:", getMin(lines))
name = input("Input a name: ")
score = checkName(name, lines)
if score is None:
    print("Name not found")
else:
    print("Score found. Score is", score)
