name = 'Alexandra Vlad'
age = 20 # not a lie
height = 1.57
weight = 57 #kg
eyes = 'Green'
teeth = 'White'
hair = 'Brown'

print "Lat's talk about %s" %name
print "She's %d meter tall" %height
print "She's %d kg heavy" %weight
print "Actually that's not too heavy."
print " He's got %s eyes and %s hair" %(eyes, hair)
print "Her teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, (age + height + weight))
