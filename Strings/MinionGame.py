def minion_game(s):
    v= ['A','E','I','O','U']
    kev = 0
    stu = 0
    for i in range(len(s)):
        if s[i] in v:
            kev += (len(s) - i)
        else:
            stu += (len(s) - i)

    if kev > stu:
        print("Kevin", kev)

    elif kev < stu:
        print("Stuart", stu)

    else:
        print("Draw")
