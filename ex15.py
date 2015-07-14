# enables the use of the argv feature by importing the sys module
from sys import argv

# unpacks the argument variable into script and filename
# this means the script accepts one argument since (script is included always by default.)
script, filename = argv

# opens the file specified in the argument
txt = open(filename)

# print your filename and the contents of the file
print "Here's your file %r:" % filename
print txt.read()

# asks you to type a filename again
print "Type the filename again:"
file_again = raw_input("> ")

# opens the file
txt_again = open(file_again)

# prints the content of the filewhile True:
print txt_again.read()

txt.close()
txt_again.close()
