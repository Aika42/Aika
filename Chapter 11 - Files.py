# 11.9.1
def studentdata():

    f = open('studentdata.txt', 'r')

    for line in f:
        xs = line.split()
        if len(xs[1:]) > 6:
            print(xs[0].capitalize())

    f.close()


# 11.9.2
def ave_grade():
    f = open('studentdata.txt', 'r')

    for line in f:
        xs = line.split()
        print(xs)
        #print(','.join(line[1:]))

        #print(xs[0], 'average grade: ', xs[1:]) #sum(xs[1:]))
        #a = ','.join(xs[1:])
        #print(a)

    f.close()

ave_grade()

