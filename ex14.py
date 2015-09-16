from sys import argv 
script,username = argv
prompt = ' > '
print " Hi %r, I'm the %r script." % (username,script)
print "\n I'd like to ask you some questions: "
print "Do you like me %r ?" % username
like = raw_input(prompt)
print "where do you %r ?" % username
live = raw_input(prompt)
print "what kind of car do you have %r?" % username
car = raw_input(prompt)

print "alright %r, you said %r about like me and you are living %r, and you car is %r" % (username,like,live,car)
