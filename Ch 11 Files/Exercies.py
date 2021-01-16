# 11.9.1 prints out the names of students that have more than six quiz scores
def studentdata():

    f = open('studentdata.txt', 'r')

    for line in f:
        xs = line.split()
        if len(xs[1:]) > 6:
            print(xs[0].capitalize())

    f.close()


# 11.9.2 average grade for each student in file
def ave_grade():
    f = open('studentdata.txt', 'r')

    for line in f:
        xs = line.split()
        summ = 0
        for ch in xs[1:]:
            summ = summ + int(ch)
        print(xs[0], summ)

    f.close()

# 11.9.3 minimum and maximum score for each student
def scores():
    f = open('studentdata.txt', 'r')

    for line in f:
        xs = line.split()
        maxx = int(xs[1:][0])
        minn = int(xs[1:][0])
        for value in xs[1:]:
            value = int(value)
            if value > maxx:
                maxx = value
            if value < minn:
                minn = value

        print(xs[0], 'max value: ', maxx, 'min value: ', minn)

    f.close()




