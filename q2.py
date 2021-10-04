def decryptPassword(s):
    # Write your code here
    pwd = {}
    count = len(s)
    numcontainer = []
    offset = 0
    # print('string ', s)
    # #print('count: ',count)
    for key in range(0,count):
        # print('--key: ', key)
        # print('letter: ', s[key])

        if s[key].isnumeric() and s[key] != '0':
            numcontainer.append(s[key])
            # print('append to numcontainer ',numcontainer)
            offset += 1
        elif s[key] == '*':
            pwd[key - 2 - offset] = s[key -1].lower()
            pwd[key - 1 - offset] = s[key -2].upper()
            # print('letter switch ', pwd)
        elif s[key] == '0' :
            pwd[key - offset] = numcontainer.pop(-1)
            # print('found zero dumping numcontainer ' , pwd)
        else :
            pwd[key - offset] = s[key]
            # print('adding to pwd ', pwd)
    # print('final pwd ',"".join(pwd.values()))
    return "".join(pwd.values())

q = '51Pa*0Lp*0e'
mya = decryptPassword(q)
# print(mya)
a = 'aP1pL5e'
# print('final should be: ',a)
q1 = 'pTo*Ta*O'
mya = decryptPassword(q1)
# print(mya)
a1 = 'poTaTO'
# print('final should be: ',a1)
