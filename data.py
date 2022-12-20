print("Welcome to school management software vo1")
teachers = []
teacher1 = {'name':'batman',
            'dob':'01-jan-1975',
            'addr':'bangalore,karnataka',
            'subjects':['maths','english','kannada'],
            'sections':[1,2,3]
            }
teachers.append(teacher1)
teacher2 = {'name':'superman',
            'dob':'01-jan-1970',
            'addr':'chennai,tamilnadu',
            'subjects':['physics','english','tamil'],
            'sections':[3,4,5]
            }
teachers.append(teacher2)
#print("\nTotal number of teachers in school: ",len(teachers))
#print("\nDetails of all teaachers: ")
#print(teachers)
students = []
new_student = {'name':'sachin',
            'dob':'01-jan-1980',
            'addr':'chennai,tamilnadu',
            'section':3,
            'marks':{'physics':75,'english':86,'tamil':67},
            'grade':'',
            'totalmarks':''
            }
students.append(new_student)

new_student = {'name':'dravid',
            'dob':'01-jan-1981',
            'addr':'bangalore,karnataka',
            'section':4,
            'marks':{'chemistry':45,'english':86,'kannada':67},
            'grade':'',
            'totalmarks':''
            }
students.append(new_student)

new_student = {'name':'dhoni',
            'dob':'01-jan-1982',
            'addr':'maduai,tamilnadu',
            'section':[3,4,5],
            'marks':{'biology':67,'english':86,'maths':67},
            'grade':'',
            'totalmarks':''
            }
students.append(new_student)
#print(students)

def update_grade_totalmarks(s):
   # print(s)
   #print(type(s))
    m = s['marks'].values()
    d = 0
    for i in m:
        d = d + i
    print(d)

def assign_grade(m):
    t = 0
    for i, j in m.items():
        t = t+j
    print("total marks: ", t)
    if t >= 200:
        print("A grade")
    elif 100 <= t < 200:
        print("B Grade")
    elif t < 100:
        print("C grade")


# greater than or equal 200, A rade
# greater than or equal 100 and less than 200, B grade
# less than 100, C grade
