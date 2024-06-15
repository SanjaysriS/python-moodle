n= int(input())
input_lines = [input() for i in range(n)]
lines_split = [input_lines[i].split(" ") for i in range(len(input_lines))]

student_names = []

for i in range(len(lines_split)):
    student_names.append(lines_split[i][0])

test_mark = []
assignment_mark = []
lab_mark = []

for i in range(len(lines_split)):
    test_mark.append(int(lines_split[i][1]))
    assignment_mark.append(int(lines_split[i][2]))
    lab_mark.append(int(lines_split[i][3]))
average = []
for i in range(len(lines_split)):
    average.append((test_mark[i]+assignment_mark[i]+lab_mark[i])//3)

max_average = max(average)
max_assignment = max(assignment_mark)
min_lab_mark = min(lab_mark)
min_average = min(average)

index_max_average = []
index_max_assignment = []
index_min_lab_mark = []
index_min_average = []

for i in range(len(average)):
    if average[i] == max_average:
        index_max_average.append(i)
    if average[i] == min_average:
        index_min_average.append(i)

for i in range(len(assignment_mark)):
    if assignment_mark[i] == max_assignment:
        index_max_assignment.append(i)
for i in range(len(lab_mark)):
    if lab_mark[i] == m
