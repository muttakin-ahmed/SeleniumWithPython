def sumNumbers(dic):
    sm = 0
    for i in dic.keys():
        for j in dic[i]:
            sm += j
    return sm
d = ({
    "numbers" : [1,2,-3]
})
print(sumNumbers(d))
