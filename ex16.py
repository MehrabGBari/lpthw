from sys import argv

script,filename = argv

txt = open(filename,'a')

print "I'm going to add 3 lines in %r: " % filename

print "enter 1st line :"
line1 = raw_input(' > ')
print "enter 2nd line :"
line2 = raw_input(' > ')
print "enter 3rd line :"
line3 = raw_input(' > ')


txt.write(line1)
txt.write("\n")
txt.write(line2)
txt.write('\n')
txt.write(line3)
txt.write('\n')

txt.close()
txt = open(filename,'r')
print txt.read()
