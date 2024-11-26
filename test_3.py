def reverse_num(num: int):
    # Write your code here.
    original_num = num
    n = 0
    while 1:
        if num // 10 == 0:
            break
        n += 1
        num = num // 10
        print(n)
    
    

    print(n)
    print(original_num)
    print(num)
    print(original_num % 10 )

reverse_num(1234)

# Run this file for test
# assert reverse_num(1234) == 4321
# assert reverse_num(20903) == 30902
# assert reverse_num(1_000_234) == 4320001
# assert reverse_num(4444) == 4444
# assert reverse_num(1) == 1
# assert reverse_num(0) == 0

