# top level choices: select layout type and input km from destination
# requires 1 choice from list and one variable input

relocationquote = input ("please input the layout of your current apartment: ")
layout_choice = ['1R', '2R', '1LDK', '2LDK', '3LDK']

#Type the layout choice
if layout_choice == '1R':
# code for 1R 
    a = 1 #rooms
    c = a*10+8000 #cost
#Type km from destination)
x = input("Input Km from destination")
km_destination = int (x)

if x < 20:
   y = c+20000
elif x in range (31, 51):
     print (y+40000)
elif x in range (51, 70):
    print (y+40000)*.9
    input("10% discount applied")
elif x > 70:
    print ("tbd.Long distance package discount; contact for pricing and special rate")
if layout_choice == '2R':
   print ("Quote for 2R relocation")
a = 2 #rooms
c = a*10*100+8000 #cost
if x < 20:
   y = c+20000
elif x in range (31, 51):
    print (y+40000)
elif x in range (51, 70):
     print (y+40000)*.9
     print ("10% discount applied")
elif x > 70:
     print ("tbd")
     print ("long distance package discount; contact for pricing and special rate")
if layout_choice == '1LDK':
   print ("Quote for 1LDK relocation")
a = 3 #rooms
c = a*10+8000 #cost   
if x < 20:
   y = c+20000
elif x in range (31, 51):
     print (y+40000)
elif x in range (51, 70):
     print (y+40000)*.9
     print ("10% discount applied")
elif x > 70:
     print ("tbd. Long distance package discount; contact for pricing and special rate") 
if layout_choice == '2LDK':
# code for 2LDK
    print("Quote for 2LDK relocation")
    a = 4 #rooms
    c = a*10*100+8000 #cost
    print("Input Km from destination")
    print ("Cost: (JPN)")
    if x < 20:
        y = c+20000
    elif km_destination in range (31, 51):
        print (y+40000)
    elif km_destination in range (51, 70):
        print (y+40000)*.9
        print ("10% discount applied")
    elif x > 70:
        print ("tbd")
        print ("long distance package discount; contact for pricing and special rate") 
if layout_choice == '3LDK':
# code for 2LDK
    print ("Quote for 3LDK relocation")
    a = 5 #rooms
    c = a*10*100+8000 #cost
    print ("Input Km from destination:")
    print ("Cost: (JPN)")
    if x < 20:
        y = c+20000
    elif x in range (31, 51):
        print (y+40000)
    elif x in range (51, 70):
        print (y+40000)*.9
        print ("10% discount applied")
    elif x > 70:
        print("tbd")
        print ("long distance package discount; contact for pricing and special rate") 
if layout_choice == 'Others':
    print ("contact for pricing and special rate")

print ("Thank you for choosing VM Kanto Relocation :)")
