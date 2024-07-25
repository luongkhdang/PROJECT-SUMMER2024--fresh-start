
"""
fizzbuzz
input: a number
output: if the number is //3=0 return fizz and //5=0 return buzz
        else: return number

"""


def fizzbuzz(number):
    answer = ""
    
    if number %3==0:
        answer+=("fizz")
    if number %5==0:
        answer+=("buzz")
    if not number%3==0 and number%5==0:
        answer += str(number)
    print(answer)    
    return answer

number = int(input(">"))
fizzbuzz(number)