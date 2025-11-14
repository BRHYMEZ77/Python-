score = int (input("Please enter the student's score:"))

if score >= 80:
    print('Grade A')
elif score >= 70:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
elif score >= 50:
    print("Grade: D")
elif score >= 40:
    print("Grade: E")    
elif score < 40:
    print('Grade F')
elif score < 0 or score > 100:  
    print('The score is invalid.')
else:
    print('Score is Invalid.')
        