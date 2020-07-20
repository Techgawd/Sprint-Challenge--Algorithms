'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word)<2:
        return 0
    l1 = word[0]
    l2 = word[1]
    subword = word[2:]
    return find_th(l1, l2, subword)
  
def find_th(l1, l2, subword):
    count = 0
    if l1 == 't' and l2 == 'h':
        count += 1
    if len(subword) == 0:
        return count
    l1 = l2
    l2 = subword[0]
    subword = subword[1:]
    count += find_th(l1, l2, subword)
    return count

