import data
import student

#print(data.students[0])
#data.update_grade_totalmarks(data.students)
# for i in data.students:
#     #print(i)
#     data.update_grade_totalmarks(i)

#data.students[2]['grade'] = student.assign_grade(data.students[2])
for i in data.students:
    i['grade'] = student.assign_grade(i)
    i['totalmarks'] = student.update_grade_totalmarks(i)
print(data.students)
