def combinations(list1 ,list2):
    # result = []
    for item1 in list1:
        for item2 in list2:
            yield (item1, item2)
    #         result.append((item1, item2))
    #      # return result

    # list3 = zip(list1,list2)
    # return list3

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for combination in combinations(list1, list2):
    print(combination)

