#Task01

for i in range(11)[1:11]:

    if i % 2 == 0:
        by2 = i
        print("divisible by 2 >>" , by2)

    elif i % 3 == 0:
        by3 = i
        print("divisible by 3 >>" , by3)

    elif i % 2 != 0 and i % 3 != 0 :
        by2and3 = i
        print("divisible by 2 and 3 >>"  , by2and3 )
