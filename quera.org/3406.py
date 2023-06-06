# https://quera.org/problemset/3406/


number_one = input()
number_two = input()

if number_one[::-1] > number_two[::-1]:
    print(f"{number_two} < {number_one}")
elif number_one[::-1] < number_two[::-1]:
    print(f"{number_one} < {number_two}")
else:
    print(f"{number_one} = {number_two}")