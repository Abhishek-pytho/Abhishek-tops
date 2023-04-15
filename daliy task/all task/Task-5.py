#WAP enter five subject mark and find percentage and totalor grade.

print("Enter the marks of five subjects:")
sub1 = float (input ())
sub2 = float (input ())
sub3 = float (input ())
sub4 = float (input ())
sub5 = float (input ())
total, average, percentage, grade = None, None, None, None
total = sub1 + sub2 + sub3 + sub4 + sub5
average=total/5
percentage = (total / 500.0) * 100
if average >= 90:
    grade = 'A'
elif average >= 80 and average < 90:
    grade = 'B'
elif average >= 70 and average < 80:
    grade = 'C'
elif average >= 60 and average < 70:
    grade = 'D'
else:
    grade = 'E'

print ("\nThe Total marks is:   \t", total, "/ 500.00")

print ("\nThe Percentage is:    \t", percentage, "%")
print ("\nThe Grade is:         \t", grade)
