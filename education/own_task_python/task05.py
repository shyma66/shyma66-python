Hash_Dict = dict()
Hash_Func = lambda x: x % 10
for i in range(0, 16, 5):

    Hash_Code = Hash_Func(i)

    Hash_Dict[Hash_Code] = i + Hash_Code

print(Hash_Dict)

print(15 % 10)