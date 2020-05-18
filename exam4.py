class ColourError(Exception):
    pass


class NonColour(ColourError):
    def __init__(self, colour):
        self.message = str(colour) + " is not a colour"



class NonBaseColour(ColourError):
    def __init__(self):
        self.message = "Only base colours allowed"



def print_base_colour(c):
    colours = ["red", "green", "blue", "yellow", "brown", "purple"]
    if c in colours[:3]:
        print(c + " is printed")
    elif c in colours:
        raise NonBaseColour()
    else:
        raise NonColour(c)


def colour_interface():
    while True:
        try:
            print_base_colour(input("choose base colour"))
            break
        except NonColour as n:
            print(n.message)
            raise
        except NonBaseColour as nb:
            print(nb.message)
            print("try again")
        finally:
            print("printing colour request handled...")

colour_interface()

functions = []

def my_dec(function):
    def inner(*args):
        print(f'register function {function.__name__} returns :')
        functions.append(f'{function.__name__} {args}')
        return function(*args)

    return inner

def my_dec2(function):
    def inner(x=3,y=1000):
        print(f'register function {function.__name__} returns :')
        functions.append(f'{function.__name__} ({x},{y})')
        return function( x, y)
    return inner
@my_dec
def printer(str):
    print(str)

@my_dec
def duplicator(*args1):
    return [[i for j in range(2)] for i in args1]

@my_dec2
def kwfunc(x=3, y=1000):
    print(x * y)

def unregistered(str):
    return str


printer('hi')
print(duplicator(5, 6, '7'))
print(duplicator('r'))

print(unregistered('i\'m under the radar'))
kwfunc()
kwfunc(x=5, y=3)

print("The calls to registered functions in this system are:")
[print(f) for f in functions]

print("main question")
f = {"#x": lambda x: f"#{x}","x/2": lambda x: x/2,"x**2": lambda x: x**2}
[print(k + ": " + str([v(i) for i in range(10)])) for k,v in f.items()]

# shorter alternative using map
#[print(k + ": " + str(list(map(v,range(10))))) for k,v in f.items()]

print("\n\nbonus question no lambda")
f = {"x"+g: "x" + g for g in ["*5","/2","**2","%3","+3","-1"]}
[print(k + ": " + str([eval(v) for x in range(10)])) for k,v in f.items()]

#reduce
from functools import reduce
s = input("reverse\ntype string to reverse: ")
print(s + " <-> " + reduce(lambda x,y: y+x, s))

summary = {"ending": 0, "length": 0, "sum": 0}


def try_sum(step=2, undivided=3, target=200):
    sum = num = 0
    while sum <= target:
        num += step
        sum += num
        if not sum % undivided:
            continue
        print(str(num), end=" ")

    print(f"\nsum of multiples of {step} undivided by {undivided} from 0 to {num} = {sum}")
    summary["ending"] += num
    summary["sum"] += sum
    summary["length"] += 1


try_sum()
try_sum(target=300)
try_sum(undivided=7)
try_sum(step=3, undivided=2)
param = input("which average would like to print? (ending/sum)")
if param in ("ending", "sum"):
    print("average series " + param + ": " + str(summary[param] / summary["length"]))
else:
    print("no such parameter")


# exercise 1+2(בכלל מאתים מנה):

l = [str(['#' + str(x) if d == 1 else x * 0.5 if d == 2 else x * x for x in range(10)]) for d in [1, 2, 3]]
print('#x: ' + l[0] + '\n' + 'x/2: ' + l[1] + '\n' + 'x**x: ' + l[2])

# exercise 3,1:
s = [d + ': ' + str([eval(d) for x in range(10)]) for d in ['x*5', 'x/2', 'x**2', 'x%3', 'x+3', 'x-1']]
print('\n'.join(s))


# exercise 4:
def multipale(num):
    return lambda x: x * num


double = multipale(2)
print(double(9))

triple = multipale(3)
print(triple(4))

# exercise 5:
from functools import reduce


def opposite(string):
    return reduce(lambda a, b: b + a, string)


print('the opposite of python is: ' + opposite('python'))


# exercise 1:

str_arr = ['h', 'e', 'l', 'o', 'p', 'y', 't', 'h', 'o', 'n', 7.6]
new_str = "".join(str_arr[:2]) + str_arr[2] * 2 + " ".join(str_arr[3:5]) + "".join(str_arr[5:9]) + " ".join(
    (str_arr[9], str(str_arr[10] / 2)))
print(new_str.capitalize())


# exercise 2:
price_in_sheqel = input("please enter price in sheqel : ")
while not price_in_sheqel.isdigit():
    price_in_sheqel = input("please enter price in sheqel : ")
dollar = float(price_in_sheqel) / 3.6
print(f"the price in dollars is : {dollar}$")


# exercise 3,1 (deletes the first word):
times_of_dialog = input("how many times do you want this dialog to continue ? ")
for dialog in range(int(times_of_dialog)):
    first_input = input("please enter a sentance : ")
    new_first_input = " ".join(first_input.split()[1:]) + "?"
    print(new_first_input)


# exercise 3,2 (deletes the last word):
times_of_dialog = input("how many times do you want this dialog to continue ? ")
for dialog in range(int(times_of_dialog)):
    first_input = input("please enter a sentance : ")
    new_first_input = " ".join(first_input.split()[:-1]) + "?"
    print(new_first_input)


# exercise 4,1 (replacing one letter):
users_string = input("please enter a sentance : ")
new_string = users_string.replace(users_string[0], "e")
print(new_string.replace(new_string[0], users_string[0], 1))


# exercise 4,2 (replacing two letters):
users_string = input("please enter a sentance : ")
new_string = users_string.replace(users_string[0], "ef")
new_string = new_string.replace(new_string[0], users_string[0], 1)
new_string = new_string.replace(new_string[1], "", 1)
print(new_string)

# ------------------------exercise 2-------------------------------------



# exercise 1,1:
def delete_duplicate(x):
    return list(dict.fromkeys(x))


mylist = delete_duplicate(["a", "b", "a", "c", "c"])

print(mylist)



# exercise 1,2:
def delete_duplicate2(x):
    mylist = x
    mylist3 = []




    for item in mylist:
       if item not in mylist3:
          mylist3.append(item)
    return (mylist3)

print(delete_duplicate2(['a', 'd', 'e', 'a', 'b']))


# exercise 1,3:
def ab(arr):
    arr_as_set = set(arr)
    return arr_as_set


arr1 = ['a', 'b', 'c', 'a', 'r']
print(ab(arr1))

# exercise 2:
math = {"1": {"1": "algebra",
              "2": "geometria"},
        "2": {"1": "functions",
              "2": "statistics"}}
python = {"1": {"1": "strings",
                "2": "functions"},
          "2": {"1": "lists",
                "2": "loops"}}
devops = {"1": {"1": "Containers_and_Orchestration",
                "2": "Linux_administration"},
          "2": {"1": "Build_automation",
                "2": "Configuration_management"}}


def chosen_subject(course, week_num, lesson_num):
    return course[week_num][lesson_num]


print(chosen_subject(python, '2', '1'))

# exercise 3:


# def print_matrix(num_of_rows):
#     for i in range(num_of_rows):
#
#
# arr = []
# for j in range(num_of_rows):
#     arr.append(0)
#
# arr[i] = 1
# print(arr)
#
# print_matrix(10)

# exercise 4:


def print_matrix2(num_of_row):
    for i in range(num_of_row):
        str1 = []
        for j in range(num_of_row * 2 - 1):
            str1.append("0")
        str1[i], str1[num_of_row * 2 - 2 - i] = "x", "x"
        print("".join(str1))


print_matrix2(6)

import unittest
import getnum


class Test(unittest.TestCase):
    def test_get_num(self):
        result = getnum.get_num(40)
        self.assertEqual(result,"ok","ther is a problam")


if __name__ =="__main__":
    unittest.main()