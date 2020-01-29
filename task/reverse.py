n=1234567890
rev=0
while n>0:
    r=n%10
    rev=(rev*10)+r
    n=n//10
print("\n reverse is = %d" %rev)
