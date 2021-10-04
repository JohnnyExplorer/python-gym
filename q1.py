'''
    given two list find the difference in letters and return the amount of difference
    if the array is not the same size return zero
'''
def get_minimum_difference(a, b):
    # Write your code here
    count = a[0]
    rtn = [];
    for key in range(1,count) :
        if not len(a[key]) == len(b[key]) :
            rtn.append(0)
        else:
            diff = 0
            diffed = []
            for letter in a[key]:
                if   b[key].find(letter) :
                    diff += 1
                    diffed.append(letter)
            for letter in b[key]:
                if   b[key].find(letter) and letter not in diffed:
                    diff += 1
            rtn.append(diff)
    print(rtn)
    return rtn


get_minimum_difference( [5,'a','jk','abb','mn','abc'],[5,'bb','kj','bbc','op','def'])