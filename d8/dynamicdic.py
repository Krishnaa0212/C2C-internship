mydic = {}
count  = int(input("How many records?"))

for  i in range(0,count):
    mykey = input("Enter key:0")
    mydic[mykey] = input("Enter your record:")

print(mydic)