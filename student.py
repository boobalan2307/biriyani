import data


def update_grade_totalmarks(s):
   # print(s)
    # print(type(s))
    m = s['marks'].values()

    d = 0
    for i in m:
        d = d + i
    return d


def assign_grade(m):
    marks = m['marks']
    t = 0
    grade = ''
    for i, j in marks.items():
        t = t + j
    if t >= 200:
        grade = 'A'
    elif 100 <= t < 200:
        grade = 'B'
    elif t < 100:
        grade = 'C'
    return grade
