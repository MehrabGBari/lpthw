
def basicmath(num1,num2):
    result = [0]*5
    result[0] = num1+num2
    result[1] = num1-num2
    result[2] = num1*num2
    result[3] = num1/num2
    result[4] = num1%num2
    return result



print "please enter a number"
a = float(raw_input(' > '))
print "enter the 2nd number"
b = float(raw_input(' > '))

out = basicmath(a,b)

print "\n Alright, already, You enterd %r and %r" % (a,b)
print "Sum of them = ", out[0]
print "Subtraction of them = ", out[1]
print "Multiplication of them = ", out[2]
print "division of them = ", out[3]
print "remider of division = ", out[4]
