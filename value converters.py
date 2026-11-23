
def main():
    while True:
        try:
            x = int(input("Put in a number:"))
            break
        except ValueError:
            print("Please put in an actual number!!")
    
    
   
    while True:
        if x >= 0:
            y = input("Are we converting decimal value to binary,octal or hexadecimal? ").strip().lower()
            if y not in ["binary","octal","hexadecimal"]:
                print("Invalid request!!")
                break

            

        else:
            print("That is not a number!!")
        if y == "binary":
            binary_values(x)
            break
        elif y == "octal":
            octal_values(x)
            break
        else:
            hexadecimal_values(x)
            break
    
def binary_values(x):
    b = []    #we add the binary values to this list
    while True:
        if x >= 2:
            a = x % 2  #gives a 0 or 1
            b.append(a)
            x = int(x/2)
        elif x==1 or x==0:
            a = x
            b.append(a) 
            break
    b.reverse()
    print(b)


def octal_values(x):
    b = []    #we add the binary values to this list
    while True:
        if x > 2:
            a = x % 8  #gives a 0 or 1
            b.append(a)
            x = int(x/8)
        elif x==1:
            a = x 
            b.append(a)
            break

    
    b.reverse()
    print(b)

def hexadecimal_values(x):
    b = []    #we add the binary values to this list
    while True:
        if x > 0:
            a = x % 16  #gives a 0 or 1
            if a>=10 and a<=15:
                hex_values = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
                a = hex_values[a]
            b.append(a)
            x = int(x/16)
        else:
            break
       

    b.reverse()
    print(b)
while True:
    main()
