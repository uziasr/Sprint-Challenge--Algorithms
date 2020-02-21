'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #takes in string, returns number    
    # print(word)
    # print(word)
    if word == 'th':
        return 1
    elif len(word) == 2 and word != 'th':
        return 0
    elif len(word)==0:
        return 0
    elif len(word)==1:
        return 0
    else:
        half = len(word)//2
        # print(half)
        first_half = word[:half]
        second_half = word[half:]
        count =  count_th(first_half) + count_th(second_half)
        return  count + count_th(word[half-1]+word[half])
