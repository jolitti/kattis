vowels = {"a","e","i","o","u","y"}

def doubles(s:str) -> int:
    ans = 0
    for i in range(len(s)-1):
        a,b = s[i],s[i+1]
        if a in vowels and a==b: ans+=1
    return ans

assert(doubles("ee")==1)
assert(doubles("eevaa")==2)
assert(doubles("baloon")==1)
assert(doubles("llbbtt")==0)


while True:
    n = int(input()) # size of sample
    if n <= 0: break

    winner = ""
    winner_num = 0
    for _ in range(n):
        word = input()
        num = doubles(word)
        # print(num)
        if num > winner_num: 
            winner = word
            winner_num = num
    print(winner)