print("Welcome to the Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

#Bill value
bill = 0

if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2

if size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3

if size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill += 3

#Cheese
if extra_cheese == "Y":
    bill += 1

#bill
print(f"Your final bill is ${bill}!")        


#FinalGreetings
print("Thanks for your business!!")
print("🍕Your pizza is being prepared!🍕")    