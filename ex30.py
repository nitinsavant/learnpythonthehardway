people = 30
cars = 40
trucks = 15

# checks if the value for cars is greater than the value for people. if it is, it prints and ends the block, if not, it evaluates the elif statement. if that's true, it prints and ends the block. if not, it does the same with the else block.
if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."
