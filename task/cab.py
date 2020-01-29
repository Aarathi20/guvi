def taxi():

    while True:
        src=int(input("enter the source"))
        dest=int(input("enter the destination"))
        km=dest-src
        print(km)
        print("\n1.Mini\n2.macro\n3.prime\n")
        print("enter your choice:")
        n=int(input())
        if n==1:
            mini(km)
        elif n==2:
             macro(km)
        elif n==3:
             prime(km)
        else:
             print("invalid option")
        continue
    return true

def mini(km):
    print("kilometers:",km)
    price=km*10
    print("price:",price)
    taxi()
    return true
def macro(km):
    print("kilometers:",km)
    price=km*20
    print("price:",price)
    taxi()
    return true
       
def prime(km): 
      print("kilometers",km)
      price=km*30
      print("price:",price)
      taxi()
      return true

print("welcome")
taxi()
