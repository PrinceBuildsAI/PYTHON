'''Sets-> you can't have duplicate in sets and set don't have any indexing'''
'''merge two dictionary'''
# d1 = {10:100,20:200,30:300}
# d2 = {40:400,50:500,60:600}

# for i in d2:
#     d1[i] = d2[i]
# print(d1)

'''write frequency of each element'''

# a = [1,1,2,2,2,3,3,4,4,5,5,5,5]
# d = {}
# for  i in a:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)

'''combine two dictionary'''

d1 = {10:100,20:200,40:300}
d2 = {40:400,50:500,60:600}

for i in d2:
    if i in d1.keys():
        d1[i] += d2[i]
    else:
        d1[i] = d2[i]
print(d1)

