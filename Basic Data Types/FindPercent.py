if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))  #list for storing values of marks
        student_marks[name] = scores     #add to the dictionary
    query_name = input()
res = student_marks[query_name]
print("{0:.2f}".format(sum(res) / 3))
