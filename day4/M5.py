#problem statement:
'''Print multiplication table of a number'''

#solution:
series = int(input("Give me the number: "))
i = 1
while i <= 10:
    print(series, '*', i, '=', series*i)
    i+=1
