print("-"*10, "range", "-"*10 )
for i in range(6):
    print(i)

print("-"*10, "range [::-1]", "-"*10 )
for i in range(6)[:0:-1]:
    print(i)

print("-"*10, "list []", "-"*10 )
for i in [1,2,3,4,5,6]:
    print(i)

print("-"*10, "list [::-1]", "-"*10 )
for i in [1,2,3,4,5,6][::-1]:
    print(i)

print("-"*10, "list reversed 1.1", "-"*10 )
for i in reversed([1,2,3,4,5,6]):
    print(i)

print("-"*10, "list {}", "-"*10 )
for i in {1,2,3,4,5,6}:
    print(i)

print("-"*10, "list {}[::-1]", "-"*10 )
try:
    for i in {1, 2, 3, 4, 5, 6}[::-1]:
        print(i)
except TypeError:
    print("-Error- \n-SyntaxWarning-")

print("-"*10, "enumerate list []", "-"*10 )
for i in enumerate([1,2,3,4,5,6]):
    print(i)

print("-"*10, "enumerate list [] 1.1", "-"*10 )
for index,i in enumerate([1,2,3,4,5,6] ):
    print(f'{index}: {i}')

print("-"*10, "enumerate list [] 1.2", "-"*10 )
for index,i in enumerate([1,2,3,4,5,6],start=1 ):
    print(f'{index}: {i}')

print("-"*10, "enumerate list [::-1]", "-"*10 )
for i in enumerate([1,2,3,4,5,6][::-1]):
    print(i)

print("-"*10, "enumerate list [::-1] 1.1", "-"*10 )
for index ,i in enumerate([1,2,3,4,5,6][::-1]):
    print(f'{index}: {i}')

print("-"*10, "enumerate list [::-1] 1.2", "-"*10 )
for index,i in enumerate([1,2,3,4,5,6][::-1],start=1 ):
    print(f'{index}: {i}')

print("-"*10, "enumerate list reversed 1.3", "-"*10 )
for index,i in enumerate(reversed([1,2,3,4,5,6]), start=1):
    print(f'{index}: {i}')

print("-"*10, "enumerate list reversed 1.4", "-"*10 )
for index, i in enumerate(reversed([1,2,3,4,5,6]), start=1):
    reversed_index = len([1,2,3,4,5,6]) - index + 1
    print(f'{reversed_index}: {i}')

print("-"*10, "enumerate list reversed 1.5", "-"*10 )
for index, i in zip(range(len([1,2,3,4,5,6]), 0, -1), reversed([1,2,3,4,5,6])):
    print(f'{index}: {i}')

