def reverse_num(num: int):
    # Write your code here.
    if (num < 0):
        return print("Number must greater than or equal to 0")
    else :
        original_num = num
        reversed_num = 0
        n = 0
        while 1:
            if num // 10 == 0:
                break
            n += 1
            num = num // 10
        
        while original_num > 0:
            digit = original_num % 10
            reversed_num += (10**n)*digit
            original_num = original_num //10
            n -= 1
        
        return reversed_num

print(reverse_num(-1))

# Run this file for test
assert reverse_num(1234) == 4321
assert reverse_num(20903) == 30902
assert reverse_num(1_000_234) == 4320001
assert reverse_num(4444) == 4444
assert reverse_num(1) == 1
assert reverse_num(0) == 0