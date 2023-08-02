
print('this program will give numbers from you, then calculate the average of them. when your input is done, enter -1 to start calculat :)')

numbers_sum = 0
numbers_count = 0
average = 0
number = int(input('Please enter an integer: '))

while number != -1:
    numbers_sum += number
    numbers_count += 1
    number = int(input('Please enter an integer: '))
    if number == -1:
        average = numbers_sum / numbers_count

print('DONE')
print(f'Result is {average}')
