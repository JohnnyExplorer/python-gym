def findSubstring(s, k):
    checked = []
    pattern = list('aeiou')
    bestcombo = {}
    for key in range(0,len(s)):
        print('key: ' ,key)
        combo = s[key: key + k]
        print('combo: ',combo)
        count = check(combo,pattern)
        print('count', count)
        if count > len(bestcombo) :
            bestcombo = combo
        print(bestcombo) 
    return bestcombo

def check(s,pattern):
    count =0
    for letter in s :
        if letter in pattern :
                count += 1
    return count

combo =findSubstring('asdfqasdlajsdhfowuiiiiiiiiiiiieryasdlbvbieiweyrewueieeieieieieieieieieieieieieieieieiewurvlhvlhdfjasdfieuyr',20)
#print('last find ',combo)
print('should be ', 'erdii')

