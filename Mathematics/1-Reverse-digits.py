# Given N,  reverse the digits of N.

def reverse_digits(n):
    reverse = 0
    while(n > 0):
        remain = n%10
        reverse = (reverse*10) + remain
        n = n//10
    return reverse

print(reverse_digits(123))