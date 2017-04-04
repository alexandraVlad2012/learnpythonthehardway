from sys import argv
from os.path import exists

script, from_file, to_file = argv

#O varianta simplificata
print "Copying from %s to %s " % (from_file, to_file)

in_file = open(from_file).read()


out_file = open(to_file, 'w').write(in_file)

print "Alright, all done."

in_file.close()
out_file.close()
