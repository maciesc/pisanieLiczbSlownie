
thousands = (' tysiąc', ' tysiące', ' tysięcy')
millions = (' milion', ' miliony', ' milionów')
milliards = (' miliard', ' miliardy', ' miliardów')
hundreds = (
    '', ' sto', ' dwieście', ' trzysta', ' czterysta', ' pięćset', ' sześćset', ' siedemset', ' osiemset',
    ' dziewięćset')
unity = (
    '', ' jeden', ' dwa', ' trzy', ' cztery', ' pięć', ' sześć', ' siedem', ' osiem', ' dziewięć', ' dziesięć',
    ' jedenaście',
    ' dwanaście', ' trzynaście', ' czternaście', ' piętnaście', ' szesnaście', ' siedemnaście', ' osiemnaście',
    ' dziewiętnaście')
decimal = (
    '', '', ' dwadzieścia', ' trzydzieści', ' czterdzieści', ' pięćdziesiąt', ' sześćdziesiąt', ' siedemdziesiąt',
    ' osiemdziesiąt',
    ' dziewięćdziesiąt')


def convert_three_digit_number_to_string(number=0):
    digits = convert_number_to_digits(number)
    hundreds_digit = decimal_digit = 0
    unity_digit = digits[0]
    if number >= 10:
        decimal_digit = digits[1]
    if number >= 100:
        hundreds_digit = digits[2]

    output = hundreds[hundreds_digit]
    if decimal_digit > 1:
        output += decimal[decimal_digit]
        output += unity[unity_digit]
    else:
        output += unity[decimal_digit * 10 + unity_digit]
    return output


def convert_number_to_digits(number=0):
    digits = [int(i) for i in str(number)]
    digits.reverse()
    return digits


def divide_number_to_parts(number=0):
    digits = convert_number_to_digits(number)
    output = []
    number = 0
    multiplier = 1
    for d in digits:
        number += d * multiplier
        multiplier *= 10
        if multiplier == 1000:
            multiplier = 1
            output.append(number)
            number = 0
    if number != 0:
        output.append(number)
    return output


def check_part_of_a_speach(number):
    digits = convert_number_to_digits(number)
    digit = digits[0]
    if number >= 12 and digit == 1:
        return 2
    if number >= 10:
        decimal_digit = digits[1] * 10 + digit
        if 10 < decimal_digit < 20:
            return 2
    if digit >= 5 or digit == 0:
        return 2
    if digit >= 2:
        return 1
    return 0


def convert_listed_divided_numbers_to_string(data):
    concatenate_number = []
    for d in range(len(data)):
        word = convert_three_digit_number_to_string(data[d])
        if d == 1:
            word += thousands[check_part_of_a_speach(data[d])]
        elif d == 2:
            word += millions[check_part_of_a_speach(data[d])]
        elif d == 3:
            word += milliards[check_part_of_a_speach(data[d])]
        concatenate_number.append(word)
    concatenate_number.reverse()
    output = ''.join(concatenate_number)
    return output


def convert_number_to_written_in_words(number):
    if number == 0:
        return " zero"
    if number < 0:
        number *=-1
        print(number)
        return " minus" + convert_listed_divided_numbers_to_string(divide_number_to_parts(number))
    return convert_listed_divided_numbers_to_string(divide_number_to_parts(number))
