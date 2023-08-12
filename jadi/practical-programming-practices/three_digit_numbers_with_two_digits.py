# https://www.youtube.com/watch?v=D48MKRyQZMA
# https://github.com/jadijadi/Practical-Programming-Practices/tree/main/math/111-999-two-digits-no-zero

# Way 1
numbers = [str(number) for number in range(100, 1000)]
result = [number for number in numbers if ('0' not in number) and (len(set(number)) == 2)]
print(len(result))


# Way 2 (based on jadi's solution)
numbers = [number for number in range(100, 1000)]
counter = 0


def check_digits(number: int) -> bool:
    digits = set()
    for _ in range(3):
        digit = number % 10
        digits.add(str(digit))
        number //= 10
    return ('0' not in digits) and (len(digits) == 2)


for number in numbers:
    if check_digits(number):
        counter += 1

print(counter)
