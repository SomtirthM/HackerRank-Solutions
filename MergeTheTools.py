def merge_the_tools(string, k):
    # your code goes here
    num_subseg=int(len(string)/k)
    for index in range(num_subseg):
        t=string[index*k:(index+1)*k]
        u=""
        for c in t:
            if c not in u:
                u+=c
        print(u)



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
