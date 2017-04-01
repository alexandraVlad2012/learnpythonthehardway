from sys import argv

script, filname = argv

txt = open(filname)

print "Here's your file %r:" % filname
print txt.read()

print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()
