from sys import argv

script,filename = argv

text = open(filename,'rU')
print "\n your file name %r " % filename 
print text.read()


