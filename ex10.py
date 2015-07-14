tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print "test \a test"
print "test\btest"
print "test \f test"
print "test \n test"
print "test \r test"
print "test \t test"
print "test \v test"
print "test \ooo test"


while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
