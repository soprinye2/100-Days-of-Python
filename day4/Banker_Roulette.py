#Split string method

import random

names_string = input("Give me everybody's name, seperated by a comma and a space. ")
names = names_string.split(", ")

num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today")


#YOU COULD ALSO USE THE "CHOICE" FUNCTION

''''
person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to buy the meal today")

'''
