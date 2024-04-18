#<p>The series, $1^1 + 2^2 + 3^3 + \cdots + 10^{10} = 10405071317$.</p>
#<p>Find the last ten digits of the series, $1^1 + 2^2 + 3^3 + \cdots + 1000^{1000}$.</p>

from time import time


start1 = time()
result = 0
for i in range (1, 1001):
    summand = i
    for j in range(i-1):
        summand = summand* i
        summand = summand % (10**10)
    result += summand
    result = result % 10**10
end1 = time()

start2 = time()
total = 0
for x in range(1,1000+1):
    total += pow(x,x,10**10)
total = total % 10**10
end2 = time()
print(f'Both compute the same: {result == total}')
print(f'The manual approach is faster: {(end2- start2) - (end1-start1)> 0}')
# pow is faster because of tricks like fast exponantiation