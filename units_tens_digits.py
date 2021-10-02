units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
tens = ["", "Ten", "Twenty", "Thirty", "Fourty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]


def read(number):
    units_digit = number % 10
    tens_digit = number // 10
    return str(tens[tens_digit] + ' ' + units[units_digit])


number = int(input("Number:"))
print(read(number))