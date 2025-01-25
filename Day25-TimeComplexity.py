# Enter your code here. Read input from STDIN. Print output to STDOUT
        
def prime_check(n):
    if n < 2:
        return False
    for i in range(2, int((n**(1/2))+1)):
        if n % i == 0:
            return False
    return True


num = int(input())
for n in range(num):
    prime_result = prime_check(int(input()))
    if prime_result:
        print("Prime")
    else:
        print("Not prime")        
        
