print "\nWhat is your name:",
name=raw_input()
print "How old are you:",
age = int(raw_input())
print "How tall are you in feets:",
height = float(raw_input())
print "How much dou you weight in pounds?",
weight = float(raw_input())

print "\nSo %r, you are %r old, %r tall and %r weight." % (name,age,height,weight)

print "\n and your BMI is: ", height*height/weight


