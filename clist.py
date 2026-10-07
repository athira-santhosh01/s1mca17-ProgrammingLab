clist1=set()
clist2=set()
n1=int(input("Enter the number of colors in List1:"))
print("Enter the colors of List1:")
for x in range(n1):
    color=input()
    clist1.add(color)
n2=int(input("Enter the number of colors in List2:"))
print("Enter the colors of List2:")
for x in range(n2):
    color=input()
    clist2.add(color)
diff=clist1.difference(clist2)
print("Colors in List1 Not in Lst2:",diff)
    
