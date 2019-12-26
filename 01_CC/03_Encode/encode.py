def encode(s):
    n = len(s)
    i = 0
    while(i<n):
        count = 1;
        while (i<n-1 and s[i]==s[i + 1]):
            count+=1
            i+=1
        print(s[i]+str(count), end="")
        i += 1

if __name__ == '__main__':
    input_str = str(input())
    encode(input_str)

