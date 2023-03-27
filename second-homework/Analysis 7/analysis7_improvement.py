S = input()

# funktsioon, et saada tuple --> ([vaiksed], [suured])
def get_lower_and_upper_tuple(string):
    lower = []
    upper = []
    for letter in string:
        if letter.islower():
            lower.append(letter)
        elif letter.isupper():
            upper.append(letter)
    lower_sorted = sorted(lower)
    upper_sorted = sorted(upper)
    return lower_sorted, upper_sorted

# funktsioon, et saada tuple --> ([paaris], [paaritu])
def get_numbers_tuple(string):
    numbers_even = []
    numbers_odd = []
    for number in string:
        if number.isdigit():
            if int(number) % 2 == 0:
                numbers_even.append(number)
            else:
                numbers_odd.append(number)
    even_sorted = sorted(numbers_even)
    odd_sorted = sorted(numbers_odd)
    return even_sorted, odd_sorted

# kontrollime, kas string sisaldab ainult lubatud karaktere
if not S.isalnum():
    print("Input string must contain only alphanumeric characters.")
else:
    # et saada final listi jaoks indeksid tuplest
    letter_tuple = get_lower_and_upper_tuple(S)
    numbers_tuple = get_numbers_tuple(S)

    # koik uhte listi
    final_list = letter_tuple[0] + letter_tuple[1] + numbers_tuple[1] + numbers_tuple[0]

    # joinin listi stringiks
    print(''.join(final_list))