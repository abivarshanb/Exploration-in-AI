name=input("Enter the name ")
n=int(input("Enter the number of subject"))
total=0
for i in range(1,n+1):
    mark=float(input("Enter the mark for the subject {i}"))
    total=total+mark
percentage=total/n

if percentage>=90:
    grade="A++"
    performance="outstanding"
elif percentage>=80:
    grade="A"
    performance="Excellent"
elif percentage>=70:
    garde="B"
    performance="Very Good"
elif percentage>=60:
    grade="C"
    performance="Good"
elif percentage>=50:
    grade="D"
    performance="Average"

else:
    garde="F"
    perfromance="Need Improvement"
print("\n--Academic Perfromance")
print("Student Name ",name)
print("Total Marks ",total)
print("Percentage :",round(percentage,2),"%")
print("Grade:",grade)
print("Performance:",performance)
