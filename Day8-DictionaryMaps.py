# Enter your code here. Read input from STDIN. Print output to STDOUT

phone_dict ={}
n = int(input())

for i in range(n):
    ph = input().split()
    phone_dict[ph[0]]= ph[1]
    
try:
    while True:
        s = input()
        if s in phone_dict:
            print(f'{s}={phone_dict[s]}')
        else:
            print('Not found')
except EOFError:
    pass
