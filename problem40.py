def findNDigit(x):
    counter = x
    nextNumber = 0
    while (counter > 0):
        nextNumber += 1
        copyNumber = str(nextNumber)
        while(len(copyNumber) > 0):
            lastDigit = copyNumber[-1]
            copyNumber = copyNumber[:-1]
            counter -= 1
            if counter == 0:
                return int(lastDigit)
            

# print (findNDigit(1) * findNDigit(10)* findNDigit(100)* findNDigit(1000)* findNDigit(10000)* findNDigit(100000)* findNDigit(1000000))





def findNDigitMoreEfficient(x):
    factor = 9
    step = 1
    limit = 1
    raiseLimitCounter = factor * limit
    coefficients = []
    while (x > 0):
        coefficient = 0
        while (raiseLimitCounter > 0 and x >= step):
            x -= step 
            coefficient += 1
            raiseLimitCounter -=1
        coefficients.append(coefficient)
        if x < step:
            break 
        step += 1
        limit *= 10
        raiseLimitCounter = limit * factor
    print(coefficients)
    resultNumber =  sum([(coefficient)  for coefficient in (coefficients)])
    if x > 0:
        resultNumber += 1
    print(resultNumber)

    return int(str(resultNumber)[x-1])


def find_digit_even_more_efficient(position):
    length = 1
    while True:
        numbers_in_this_range = 9 * 10**(length - 1)
        if position > length * numbers_in_this_range:
            position -= length * numbers_in_this_range
            length += 1
        else:
            number = 10**(length - 1) + (position - 1) // length
            digit_in_number = (position - 1) % length
            return int(str(number)[digit_in_number])


