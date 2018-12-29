#program that does my rotations and reflections geometry calulations for me

x = 0.0
y = 0.0
xmod = 0.0
ymod = 0.0
sf = 0
input1 = ""
input2 = ""
print("Welcome to Transformations geometry calculator")
print("by Kai Maffucci")

while input1 != "5":
    #gets from user what kind of transformation they would like to make
    print("Choose one of the options below: ")
    print("1. Translations")
    print("2. Reflections")
    print("3. Rotations")
    print("4. Dialations")
    print("5. Exit")
    input1 = input()

    if input1 != "5":
        #translations
        while input1 == "1":
            #gets input from user on what calculation to make
            print("Choose an option:")
            print("1. Translation")
            print("2. back")
            input2 = input()

            if input2 == "1":
                print("Input x value:")
                x = float(input())
                print("Input x translation:")
                xmod = float(input())
                print("Input y value:")
                y = float(input())
                print("Input y translation:")
                ymod = float(input())
                x += xmod
                y += ymod
                print("Your answer: (" + str(x) + ", " + str(y) + ")")
            if input2 == "2":
                input1 = "0"

        #reflections
        while input1 == "2":
            #gets input from user on what calculation to make
            print("Choose one of the options below:")
            print("1. x-axis")
            print("2. y-axis")
            print("3. y = x")
            print("4. y = -x")
            print("5. back")
            input2 = input()
            
            #gets input from user on what the values of the coords that will be modified
            if input2 != "5":
                print("Input x value: ")
                x = float(input())
                print("Input y value: ")
                y = float(input())
                
            if input2 == "1":
                y = y * -1
            if input2 == "2":
                x = x * -1
            if input2 == "3":
                x, y = y, x
            if input2 == "4":
                x, y = (y * -1), (x * -1)
            if input2 == "5":
                input1 = "0"
            #display output
            if input2 != "5":
                print("Your answer: (" + str(x) + ", " + str(y) + ")")
                input()

        #rotations
        while input1 == "3":
            #gets input from user on what calculation to make
            print("Choose one of the options below:")
            print("1. 90 degrees")
            print("2. -90 degrees")
            print("3. 180 degrees")
            print("4. back")
            input2 = input()

            #gets input from user on what the values of the coords that will be modified
            if input2 != "5":
                print("Input x value: ")
                x = float(input())
                print("Input y value: ")
                y = float(input())
            
            if input2 == "1":
                x, y = (y * -1), x
            if input2 == "2":
                x, y = y, (x * -1)
            if input2 == "3":
                x *= -1
                y *= -1
            if input2 == "4":
                input1 = "0"
            #display output
            if input2 != "4":
                print("Your answer: (" + str(x) + ", " + str(y) + ")")
                input()

        #dialations
        while input1 == "4":
            #gets input from user
            print("Choose one of the optons:")
            print("1. Dilations")
            print("2. back")
            input2 = input()

            if input2 == "1":
                print("Input x value:")
                x = float(input())
                print("Input y value:")
                y = float(input())
                print("Input center of dilation x:")
                xmod = float(input())
                print("Input center of dilation y:")
                ymod = float(input())
                print("Input scale factor:")
                sf = float(input())
                x = xmod + sf * (x - xmod)
                y = ymod + sf * (y - ymod)
                print("Your answer: (" + str(x) + ", " + str(y) + ")")

            if input2 == "2":
                input1 = 0

print("Thank you for using transformations geometry calculator")
input()
