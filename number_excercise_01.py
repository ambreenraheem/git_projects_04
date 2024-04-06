#first work on python.
print("Hello! dear friends.")
print("I am Ambreen.")
print("Working on Python, for the first time.")
print("This is very easy language.")
print("Every one should learn python,becuase it makes programming easy for you.")
x=34+4*9-10
print(x)
print(x+2)
print(x+3)
print(x+4)

# second work on python(number excercise)

# Question :1

print('''
      1. you have a football field that is 92 meter long and 48.8 meter wide.
        find out total area and length using python and print it.''')

length=92
width=48.8
area=(length*width)/1000
print("The length of the football field is",length,"meter")

length=92
width=48.8
area=(length*width)
print("the area of football field is:",area)

# Question :2

print('''
      2.you bought 9 packets of potato chips from a store.
        Each packet costs:1.49 dollars and you gave shopkeeper 20 dollars.
        find out using python ,how many dollar is the shopkeeper going to give you back?''')

num_packets=9
cost_per_packet=1.49
total_cost=num_packets*cost_per_packet
money_paid=20
cash_back=money_paid-total_cost
print("cash back:",cash_back)

# Question :3 suggested code

print('''
      3.A snail is at the bottom of a 25 meter high cliff.
      It starts crawling up at a rate of 4 cm per minute .
      Find out how much time does the snail need to reach the top of the cliff ? ''')
bottom_high_cliff=25
speed_snail=4           #cm/minute
total_time=(bottom_high_cliff/speed_snail)
print(" The total time of snail need to reach the top of the cliff is:",total_time)

# Question: 4
print('''
      4.You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length. 
      If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles.
      Calculate and print the cost using python (Hint: Use power operator ** to find area of a square''')
tile_price=500            #rs/square foot
length_bathroom=5.5         #feet
total_area= length_bathroom**2   #square feet
total_cost=total_area*tile_price
print("The total cost to replace all the tiles in the bathroom is:",total_cost,"Rs")
# the whole solution was suggested by python

# Question: 5
print('''
      5.print binary representation of number 17''')

num=17
print("Binary of 17 is:",format(num,'b'))
