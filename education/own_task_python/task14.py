def right_justify(value):
    print(" "*70,value)
right_justify("monty")

def do_twice(func , arg):
    func(arg)
    func(arg)
def do_four(func,arg):
    do_twice(func,arg)
    do_twice(func,arg)
do_twice(print,"|spam|")
print("")
do_four(print,"spam")
