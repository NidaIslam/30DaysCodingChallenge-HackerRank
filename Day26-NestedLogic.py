# Enter your code here. Read input from STDIN. Print output to STDOUT

r_day, r_month, r_year=map(int,input().split())
d_day, d_month, d_year=map(int,input().split())


if r_year > d_year:
    print(10000)
elif r_year == d_year:
    if r_month > d_month:
        print(500*(r_month-d_month))
    else:
        if r_day > d_day:
            print(15* (r_day-d_day))
        else:
            print(0)
else:
    print(0)
        
