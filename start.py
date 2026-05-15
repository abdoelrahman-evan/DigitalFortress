
"""
    ## abs / pow / round / max / min / len / sum / list [] / values = / print(f"") / """ 
    

from posixpath import join
from tracemalloc import start
from turtle import color
from typing import final

from pyparsing import nums
from webcolors import names


x = 99
print (x);

temperature = -15 
print(f"The Temperature changed by {abs(temperature)} degrees.")

pi = 3.14159
print(f"Rounded Pi: {round(pi, 4)}")

bits = pow(2, 2)
print(bits) 

prices = [29,223,22,574,8,34,2,96]
print(max(prices))
print(min(prices)) 

expenses = [100, 200, 300, 400, 500] 
total = sum(expenses)
print(total)


# challenge number 1 #

Values = [70 , 85 , 92.5441554 ,70,88] 
sum_values = sum(Values) 
min_value = min(Values) 
max_value = max(Values) 
average = sum_values / len(Values) 
print(f"My average is {round(average , 1)} ,  but my best score was {round(max_value , 4)}")

#############################################

new_values = "   New One Start Mission "
print(len(new_values))
print(new_values.upper())
print(new_values.lower())
print(new_values.split())
print("-".join(new_values.split()))
print(f"{new_values.strip()}")
print(f"{new_values.replace("New One", "Let's" )}")


# Challenge 2 #

User = "   user_name:evan_pro_99   "
remove_spaces = User.strip()
upper = User.upper()
replace = User.replace("_", " ")
Lenght = len(replace)
print(f"User Name: {remove_spaces} \nUpper Case: {upper} \nReplace: {replace} \nLenght: {Lenght}")
print(f"User Name: {final} \n Lenght:{Lenght}")

final = User.strip().upper().replace("_"," ")
print(f"User Name: {final} \n Lenght:{len(final)}")
##############################################

tools= ["C","C++","Rust","Python"]
tools.append("Linux")
print(tools)

tools.insert(1,"Ubuntu")
print(tools)

tools.remove("Rust")
print(tools)

tools.pop()
print(tools)

tools.sort()
print(tools)

# Challenge 3 #

Numbers = [ 10 , 5 , 20 , 1 ]
Numbers.sort ()
Numbers.remove(5)
Numbers.append(100)
print(f"the New Order List {Numbers}")

########################################


# ips_list = ["122.1.1565.1","11.2.1662.1","122.1.1565.1","122.1.1565.1"]
# ips_locked = tuple(ips_list)
# print(f"Locked Tuples:{ips_locked}")

# count_admin = ips_locked.count("122.1.1565.1")
# print(f"the admin IP Appears {count_admin} times") 

# position = ips_locked.index("122.1.1565.1")
# print(f"The Local IP is at index : {position}")





customers = ["Ahmed","Ali","Jhon"]
properties = ["Villa","basement","Studio"]

zipped_data = list(zip(customers,properties))
print(zipped_data)

for i , (name,item) in enumerate ( zipped_data ,start = 1 ) :
    print(f"{i} - {name} wants to buy a {item}") 



class Piece:
    def __init__(self, name,
    color):
        self.name = name
        self.color = color
    @classmethod
    def white_piece(cls,name):
        return cls(name,"White")
    @classmethod
    def black_piece(cls,name):
        return cls(name,"Black")
    @property
    def value(self):
        scores = {
            "King": 100,
            "Queen": 9,
            "Rook": 5,
            "Bishop": 3,
            "Knight": 3,
            "Pawn": 1,
        }
        return scores.get(self.name.capitalize(), 0)
    def __str__(self):
        return f"""{self.color} {self.name} (value: {self.value})"""
    @staticmethod
    def game_rules():
        return "Chess is a game of strategy. Protect your King!"
class ChessBoard:
        def __init__(self):
            self.pieces = []

        def add_piece(self, piece):
            self.pieces.append(piece)

        def __len__(self):
            return len(self.pieces)

p1= Piece.white_piece("king")
p2= Piece.black_piece("Pawn")

board = ChessBoard()
board.add_piece(p1)
board.add_piece(p2)

print(f"{"Number of pieces on board:".upper()} {len(board)}")
print(f"First piece: {p1}")
print(f"First piece: {p2}")
print(Piece.game_rules())
# print(p1)
# print(p2)

def register_vehicles(*name,
**details):
    print(f"Registering cars : {' - '.join(name)}")
    for key, value in details.items():
        print(f"property : {key} -> Value: {value}")

register_vehicles("Toyota","Hyundai", owner="Evan", city="Alexandria")


def process_image(  threshold: float, *image_ids:int) -> str :
    ids_str = " , ".join(map(str, image_ids))
    return f"Image ( {ids_str} ) processed with {threshold}% accuracy "
result = process_image(26.5 , 990 , 89 , 987)
print(result)



Numbers = [1,2,3,5,6,8,40]

doubled = list (map(lambda num: num ** 2, Numbers))
print(doubled)


class_names = ["ahmed  ","yellows","   gooR"]
clean_names = list(map(lambda name : name.strip().capitalize(),class_names))
print(clean_names)


string_numbers = ["1","55","1","55","8"]

int_numbers = list(map(int,string_numbers))
print(int_numbers)


EGP = "1"
dollar = int(EGP) * 50
print(dollar)


dollar1 = list (map(lambda d : int(d)*50, EGP))
single_dollar = dollar1[0]
print(single_dollar)

string_numbers = ["1","55","1","55","8"]
evens = list(filter(lambda num: int(num) % 2 == 0, string_numbers))
print(evens)

Products = ["IPhones","Samsung","Huawei","Xiaomi","Oppo"]
Prices_s = [5000,564,944,4000,6100]
catalog =list(zip(Products,Prices_s))
print(catalog)

for product, price in catalog:
    print(f"Product: {product} - Price: {price} EGP")


employees = ["Ahmed","Evan","Ali"]
Salaries = [5000,672,5000]

increased_salaries = list(map(lambda x: x * 1.1, Salaries))
Staff_data = list(zip(employees,increased_salaries))
over = list(filter(lambda x: x[1] > 5000 and x[0] == 'Ali' or x[0] =="Ahmed", Staff_data))
over = list(filter(lambda x: x[1] > 5000 and x[0] in ["Ali","Ahmed"], Staff_data))
print(over)
print(Staff_data)

increased_1 = [s * 1.1 for s in increased_salaries]
print(f" Increased salaries : {[round(s, 0) for s in increased_1]}")

names_only = [x [0] for x in Staff_data]
print(names_only)

employees_data = {  "evan"  : {"name" : "Evan", "Salary" : 7000,"city" : "Alexandria"} ,
                    "Jhon"  : {"name" : "John", "City" : "Texas", "Salary" : 9000}}
print (f"Employee's Name is : {employees_data['evan']['name']}\nhis salary is : {employees_data['evan']['Salary']}\nCity : {employees_data['evan']['city']}")


def give_raise(name, percent):
    old = employees_data[name]["Salary"]
    new_salary = old * (1+ percent/100) 
    employees_data[name]["Salary"] = round(new_salary, 2)
    print(f"Done! {name}'s salary updated from {old} to {employees_data[name]['Salary']}")




give_raise("evan",25)
give_raise("Jhon",-25)







