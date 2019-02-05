"""
a = []
while True:
        n = input("Add a number or press enter: ")
        if n != "":
                a.append(n)
                for i in range(len(a)):
                    a[i] = int(a[i])
        else:
                print("Printing out the numbers...")
                break

print(a)

for i in a:
        print("|"*(i//2) + str(i) + "|"*(i//2) + "\n")

"""
                
def graph():
        global a
        a = []
        while True:
                n = input("Add a number or press enter: ")
                if n != "":
                        a.append(n)
                        for i in range(len(a)):
                                a[i] = int(a[i])
                else:
                        print(" ")
                        print("Forging out the lines below... ")
                        print(" ")
                        break
        a.sort()
        for i in a:
                print("Index " + str(i) + ": " + "|"*(i))
                print(" ")
                if i > 50 and i < 100:
                        m = i
                        m = "+"
                        print("Index " + str(i) + ": " + m*i)
                        print(" ")
                elif i > 100:
                        m = i
                        m = "-"
                        print("Index " + str(i) + ": " + m*i)
                        print(" ")        
                        

        

graph()
print(a)
        