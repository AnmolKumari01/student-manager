students=[]
n=int(input("enter no. of students "))
highest=0
sum=0
for i in range (n):
    name=input("enter name ")
    marks=int(input("enter marks "))
    students.append([name,marks])
print("====students data====")
for i in students:
    print("name:",i[0] ,"\t","Marks:",i[1])
    if i[1]>highest:
        highest=i[1]
    sum+=i[1]
    avg=sum/n
print("Highest marks:",highest)
print("avg marks",avg)