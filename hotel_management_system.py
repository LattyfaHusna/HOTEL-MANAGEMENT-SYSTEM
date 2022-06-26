from turtle import *

speed (0)
bgcolor("white")

penup()
goto(0,20)
pendown()
color("Yellow")
begin_fill()
circle(100)
end_fill()

# Bottom rectangle
penup()
goto(-200, -200)
pendown()
begin_fill()
for i in range(2):
    forward(400)
    left(90)
    forward(20)
    left(90)
end_fill()

# Second from bottom rectangle
penup()
goto(-175, -180)
pendown()
color("chocolate")
begin_fill()
for i in range(2):
    forward(350)
    left(90)
    forward(20)
    left(90)
end_fill()

# Main part of building
penup()
goto(-150, -160)
pendown()
color("sandybrown")
begin_fill()
for i in range(2):
    forward(300)
    left(90)
    forward(250)
    left(90)
end_fill()

# Second from top rectangle
penup()
goto(-175, 90)
pendown()
color("chocolate")
begin_fill()
for i in range(2):
    forward(350)
    left(90)
    forward(20)
    left(90)
end_fill()

# Top rectangle
penup()
goto(-150, 110)
pendown()
color("sienna")
begin_fill()
for i in range(2):
    forward(300)
    left(90)
    forward(20)
    left(90)
end_fill()

# Windows
x = -125
y = 30
color("khaki")

# Draw a single window_height
def window():
    global x # Ensures that x can be used inside of this function
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    for i in range(4):
        forward(40)
        left(90)
    end_fill()

    x = x + 70 # Moves the next window over 70 steps to the right

# Draw the windows
for i in range(3): # This loop will draw 3 rows of windows
    for i in range(4): # This loop will draw one row of 4 windows
        window()
    x = -125 # Ensures all rows of windows start from the same x-position
    y = y - 85 # Moves the next row of windows down lower than the previous

import turtle
t = turtle.Turtle()
t.penup()
t.goto(0,200)
t.pendown()
t.color("black")
style = ('Courier', 30 , 'italic')
t.write("Welcome To ALIPP HOTEL", font = style , align = 'center')
t.hideturtle()
hideturtle()

turtle.done()

class HotelManagement :
    room_no_count = 0
    def __init__(self, name="", address ="", phonenum ="", cindate ="", coutdate ="", pay = 0, price = 0, rn = " ", total_night_staying = 0):
        print ("------ WELCOME TO ALIPP HOTEL ------")
        self.name = name
        self.address = address
        self.phonenum = phonenum
        self.cindate = cindate
        self.coutdate = coutdate
        self.pay = pay
        self.price = price
        self.rn = rn
        self.total_night_staying = total_night_staying

    def booking(self):
        self.name = input("Enter your name : ")
        self.address = input("Enter your address : ")
        self.phonenum = input("Enter your phone number : ")
        self.cindate = input("Enter your check-in date : ")
        self.coutdate = input("Enter your check-out date : ")


    def book_room(self):
        import json
        import random
        roomno = [ ]

        print('{Hotel}{Info}'.format(   #string format
        Hotel = '   ------ HOTEL ALIPP',
        Info = ' INFORMATION ------   \n'))

    ## dictionaries
        room_info = [
          {"No":"1",'Types of Room': 'Honeymoon Suite', 'Bed Types': 'King bed', 'View': 'Sea view'},
          {"No":"2",'Types of Room': 'Double Deluxe', 'Bed Types': '2 single beds', 'View': 'Sea view'},
          {"No":"3",'Types of Room': 'Juniour Suite', 'Bed Types': 'Single bed', 'View': 'Sea view'}
        ]
    ## dumps() converts Python object into a JSON string
        print(json.dumps(room_info, sort_keys=False, indent=4))

        choice = int(input("\nEnter your choice : "))

        print("\n\t\t***ROOM BOOKED SUCCESSFULLY***\n")

        if choice == 1:
            print('Your choice is',choice,'(Honeymoon Suite)',"\nThe value for 1 night for Honeymoon Suite: RM 200")
        elif choice == 2:
            print('Your choice is',choice,'(Double Deluxe)',"\nThe value for 1 night for Double Deluxe: RM 150")
        elif choice == 3:
            print('Your choice is',choice,'(Juniour Suite)',"\nThe value for 1 night for Juniour Suite: RM 100")
        else:
            print("Invalid Input")

        nights = int(input("Total nights staying: "))

        if choice == 1:
            self.pay = 200*nights
            print("Total value need to pay: RM",self.pay)
        elif choice == 2:
            self.pay = 150*nights
            print("Total value need to pay: RM",self.pay)
        elif choice == 3:
            self.pay = 100*nights
            print("Total value need to pay: RM",self.pay)
        else:
            print("Invalid Input")

        # randomly generating room no
        self.rn = random.randrange(50)+200

        # checks if alloted room no
        while self.rn in roomno:
            self.rn = random.randrange(50)+200
            rc.append(0)

        print("Room No: ",self.rn)
        roomno.append(self.rn)

    #book_room()

    def Breakfast(self):
        #Inheritance class
            # parent class
            class Meal:
                # __init__ is known as the constructor
                def __init__(self, title):
                    self.title = title

                def display(self):
                    print(self.title)

                # child class
            class MealPackage( Meal ):
                def __init__(self, title, nametitle):
                    self.nametitle = nametitle

                        # invoking the __init__ of the parent class
                    Meal.__init__(self, title, nametitle)

            # creation of an object variable or an instance
            a = Meal('BREAKFAST  PACKAGE')

            # calling a function of the class Person using its instance
            a.display()

            print ("------------------")

            package = [("Couple-2 person", 1), ("Family-4 person",2), ("Super Family-6 person",3)]  # dictionaries and tuples
            self.price = [30,50,75]  # list

            for number, letter in package:      # iteration loop
                print(letter,number)

            print ("------------------")

            number = int(input("Enter number of choice: "))
            qtt = int(input("Enter number of quantitiy of package that you choose: "))

            if number == 1:
                self.price = qtt*self.price[0]
                print(package[0],"price = " ,self.price)

            elif number == 2:
                self.price = qtt*self.price[1]
                print(package[1],"price = ",self.price)

            elif number == 3:
                self.price = qtt*self.price[2]
                print(package[2],"price = ",self.price)

            else:
                print("invalid choice")

    #print(Breakfast())

    def display(self):
        print("----- CUSTOMER DETAILS -----")
        print(" Customer name : ", self.name)
        print(" Customer address : ", self.address)
        print(" Customer phonenum : ", self.phonenum)
        print(" Check in date : ", self.cindate)
        print(" Check out date : ", self.coutdate)
        print(" Room number : ",self.rn)
        print("\n  Amount: ",(self.pay+self.price))

    def Payment(self):
        print(" Payment")
        print(" --------------------------------")
        print("  MODE OF PAYMENT")

        print("  1- Credit/Debit Card")
        print("  2- TouchNGo eWallet")
        print("  3- QR Code")
        print("  4- Cash")
        x=int(input("Pay Method? "))
        print("\n  Amount: ",(self.pay+self.price))
        print("\n            Pay Now?")
        print("  (y/n)")
        ch=str(input("Y or N"))


        if ch=='y' or ch=='Y':
            print("\n\n --------------------------------")
            print("           Hotel ALIPP")
            print(" --------------------------------")
            print("              Bill")
            print(" --------------------------------")
            print(" Name: ",self.name,"\t\n Phone No.: ",self.phonenum,"\t\n Address: ",self.address,"\t")
            print("\n Check-In: ",self.cindate,"\t\n Check-Out: ",self.coutdate,"\t")
            print("\n Room Type: ",self.rn, "\t\n Room Charges: ",self.pay,"\t")
            print(" Restaurant Charges: \t",self.price)
            print(" --------------------------------")
            print("\n Total Amount: ",(self.pay+self.price),"\t")
            print(" --------------------------------")
            #print("          Thank You")
            #print("          Visit Again :)")
            print(" --------------------------------\n")

            #Write receipt file
            firstfile = open("Receipt.txt","w")
            firstfile.write("\n\n --------------------------------\n")
            firstfile.write("           Hotel ALIPP\n")
            firstfile.write(" --------------------------------\n")
            firstfile.write("              Bill\n")
            firstfile.write(" --------------------------------\n")
            firstfile.write(" Name: ")
            firstfile.write(self.name)
            firstfile.write("\n Phone No.:")
            firstfile.write(self.phonenum)
            firstfile.write("\n Address: ")
            firstfile.write(self.address)
            firstfile.write("\n Check-In: ")
            firstfile.write(self.cindate)
            firstfile.write("\n\n Check-Out: ")
            firstfile.write(self.coutdate)
            firstfile.write("\n --------------------------------")
            firstfile.write("\n          Already Paid ")
            firstfile.write("\n --------------------------------")
            firstfile.write("\n          Thank You\t")
            firstfile.write("\n          Visit Again :)\t")
            firstfile.write("\n --------------------------------\n")
            firstfile.close()

            #read file
            firstfile = open ("Receipt.txt","r")

            while True:
                linebyline = firstfile.readline()
                if len(linebyline) == 0:
                    break
                print(linebyline, end=" ")

            firstfile.close()

            print("\n")
            def myHotel(*args):
                for hotel in args:
                    print (hotel)

            myHotel('Thank you For choosing our hotel !','Please come again.')
            print("\n")

        else:

            print("Please Pay")



def main():


    rooms = []

    a = HotelManagement()

    while (1) :
        print("\n")
        def menu(arg1, arg2, arg3, arg4, arg5, arg6):
            print("1:", arg1)
            print("2:", arg2)
            print("3:", arg3)
            print("4:", arg4)
            print("5:", arg5)
            print("0:", arg6)

        # use **kwargs to pass arguments to this function :

        kwargs = {"arg1" : "Booking", "arg2" : "Rooms_Info", "arg3" : "Breakfast_choice", "arg4" : "Customer_details", "arg5" : "Payment", "arg6" : "Exit"}

        menu(**kwargs)

        me=int(input("Menu:"))

        if me == 1:
            print(" ")
            a.booking()

        elif me == 2:
            print(" ")
            a.book_room()

        elif me == 3:
            print(" ")
            a.Breakfast()

        elif me == 4:
            print(" ")
            a.display()


        elif me == 5:
            print(" ")
            a.Payment()

        else:
            exit()

main()

