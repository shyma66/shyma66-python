def reverse_list(l):
    'return a list with the reverse order of l'
    l = l[::-1] # or l.reverse()
    return l
m = [ 1 ,2 ,33 ,211, 3]
print(reverse_list(m))