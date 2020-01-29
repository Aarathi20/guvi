count=1
while count>0:
  num1=int(input("enter the first number"))
  num2=int(input("enter the second number"))
  sum=num1+num2
  print(sum)
  print("Do You Want To Continue? [y/n]:")
  r=input()
  if (r=='y'):
    count=1
    continue
  else:
    count=0
    exit()
