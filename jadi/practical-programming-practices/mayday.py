# https://www.youtube.com/watch?v=XlAJtpd3kSI

cipher = 'Whiskey Hotel Four Tango Dash Alpha Romeo Three Dash Yankee Oscar Uniform Dash Sierra One November Kilo India November Golf Dash Four Bravo Zero Uniform Seven'
cipher = cipher.split()
plain = list()
SPECIALS = {
    'Dash': '-',
    'Zero': '0',
    'One': '1',
    'Two': '2',
    'Three': '3',
    'Four': '4',
    'Five': '5',
    'Six': '6',
    'Seven': '7',
    'Eight': '8',
    'Nine': '9'
}

for word in cipher:
    plain.append(SPECIALS.get(word, word[0]))

ans = ''.join(plain)
print(ans)
