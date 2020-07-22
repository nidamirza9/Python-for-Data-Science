##Learn python.org
#Nida Mirza
#5CE-1-->30
#Learn the Basic:
##1.Hello, World!
print('\n---------------------------\n')
print('Nida Mirza')
print('5CE-1')
x=1
if x==1:
   print("Enroll-no:180630107030")
print('\n---------------------------\n')   
   
print('---------------------------\n')
print('\nA:')
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)
print('\nB:')
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)
print('\nC:')
# change this code
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
print('\n---------------------------\n')
##List:
print('---------------------------\n')
print('\nA:')
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

# prints out 1,2,3
for x in mylist:
    print(x)
print('\nB:')
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("Nida ")
strings.append("Mirza ")

second_name = names[1]

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)
print('\n---------------------------\n')
print('---------------------------\n')
print('\nA:')
remainder = 11 % 3
print(remainder)
print('\nB:')
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)
print('\nC:')
lotsofhellos = "Nida " * 3
print(lotsofhellos)
print('\nD:')
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5]
all_numbers = odd_numbers + even_numbers
print(all_numbers)
print('\nE:')
print([1,2,] * 2)
print('\nF:')
x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
print('\n---------------------------\n')
print('---------------------------\n')
print('String formatting--> ')
print('\nA:')
name = "Nida"
age = 20
print("%s is %d years old." % (name, age))
print('\nB:')
data = ("Nida", "Mirza", 57.9)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)
print('\n---------------------------\n')
print('---------------------------\n')
print("A:")
n='Nida Mirza'
print(len(n))
print('\nB:')
k="Nidaaa"
print('String index: %s',%k)
print(k.index("a"))
print('\nC:')
k="Nidaaaa"
print('String count of %s'%k)
print(k.count("a"))
print('\nD:')
astring = "Nida Mirza!"
print(astring[3:7])
print(astring[3:7:1])
