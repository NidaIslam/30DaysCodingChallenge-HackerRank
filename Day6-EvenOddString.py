# Enter your code here. Read input from STDIN. Print output to STDOUT

def indexValues(string):
    evenCharacter, oddCharacter = [] , []   
    for s in range(len(string)):
        if s%2==0:
            evenCharacter.append(string[s])
        else:
            oddCharacter.append(string[s])
    evenstr = ''.join(evenCharacter)
    oddstr = ''.join(oddCharacter)
        
    print(evenstr,oddstr)


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        string = input()
        indexValues(string)

