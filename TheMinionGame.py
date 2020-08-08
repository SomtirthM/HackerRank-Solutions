def minion_game(string):
    # your code goes here
    S=string.strip()
    S_length=len(S)
    plr1,plr2 = 0,0

    for i in range(S_length):
        if S[i] in 'AEIOU':
            plr1 +=S_length-i
        else:
            plr2 +=S_length-i
    if plr1>plr2:
        print("Kevin",plr1)
    elif plr2>plr1:
        print("Stuart",plr2)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
