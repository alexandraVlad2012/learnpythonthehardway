from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

name =  raw_input("What's your name?")
print (name)

from sys import argv

script, first, second, third = argv
fourth = raw_input("What is your fourth variable? ")

print "All together, your script is called %r, your first variable is %r, your second is %r, your third is %r, and your fourth is %r" % (script, first, second, third, fourth)
