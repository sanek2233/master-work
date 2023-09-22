import json


def intToRoman(num):
    roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    integer = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    result = ''
    while num > 0:
        for i in range(len(integer)):
            while num >= integer[i]:
                result += roman[i]
                num -= integer[i]
    return result


result = []
for i in range(1, 3999):
    result.append(
        {
            'input': [intToRoman(i)],
            'output': i,
        }
    )

with open('romanToInt.json', 'w') as file:
    json.dump(result, file)