x = "There are %d types of people" %10
binary = "binary"
do_not = "don't"
y  = "Those who know %s and those who %s" %(binary, do_not)

print x
print y

print "I said : %r" % x
print "I also said: '%s'" % y

hilarious = False
joke_evaluation = "Isn't that joke so funy?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side..."

print w + e

# 2.Find all the places where a string is put inside a string. There are four places.
# y  = "Those who know %s and those who %s" %(binary, do_not)
# print "I said : %r" % x
# "I also said: '%s'" % y


# 4. Explain why adding the two strings w and e with + makes a longer string.
# In this case + concatenate two character strings
