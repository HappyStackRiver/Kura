learnerGrades = open('grades.txt', 'r+')
failing = open('fail.txt', 'r+')
passing = open('pass.txt', 'r+')
for line in learnerGrades:
        line_split = line.split()
        if line_split[2] == 'fail':
            print(line_split[0], file=failing)
        if line_split[2] == 'pass':
            print(line_split[0], file=passing)
learnerGrades.close()
failing.close()
passing.close()