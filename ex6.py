# Basic variable formatting inserting an integer and a string
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# Using parantheses to insert multiple variables
y = "Those who know %s and those %s." % (binary, do_not)

print x
print y

# Using the %r format character here. I think it tries to guess what variable type you're giving it.
print "I said: %r." % x
print "I also said: '%s'." %y

hilarious = False
joke_evaluation = "Isn't that joke funny?! %r"

# This method creates a string with a format character and then adds the specific variable to insert in the next line of code
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# concatenates two strings using a plus
print w + e
