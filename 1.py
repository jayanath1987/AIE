input=input()

try:
    marks = int(input)
    if marks not in range(0, 101):
       print("ERROR! Please enter a numerical value between 0 to 100")
    else:
        if marks < 45:
            if marks < 30:
                grade="D-"
            elif  marks < 35:
                grade = "D"
            elif  marks < 40:
                grade = "D+"
            else :
                grade = "C-"
            print("Student is FAIL, Grade",grade)
        else:
            if marks < 50:
                grade="C"
            elif  marks < 55:
                grade = "C+"
            elif  marks < 60:
                grade = "B-"
            elif  marks < 65:
                grade = "B"
            elif  marks < 75:
                grade = "B+"
            elif  marks < 80:
                grade = "A-"
            elif  marks < 90:
                grade = "A"
            else :
                grade = "A+"
            print("Student is PASS, Grade", grade)



except ValueError:
   print("ERROR! Please enter a numerical value between 0 to 100")
