count=1
while count>0:
    src=int(input("enter the source"))
    dest=int(input("enter the destination"))
    km=dest-src
    print(km)
    print("\n1.Mini\n2.macro\n3.prime\n")
    print("enter your choice:")
    n=int(input())
   
        print("kilometers:",km)
        price=km*10
        print("price:",price)
        count=1
        continue
    elif n==2:
        print("kilometers:",km)
        price=km*20
        print("price:",price)
        count=1
        continue
    elif (n==3):
      print("kilometers",km)
      price=km*30
      print("price:",price)
      continue
    else:
     print("invalid option")
     count=1
     continue
else:
    exit()
