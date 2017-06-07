# There are 4 places where a string is inside a string
#defines variable 'x' as containing two (10 in binary) types of people
x = "There are %d types of people." % 10
# sets the variable 'binary' equal to the string "binary"
binary = "binary"
# sets the variable "do_not" equal to the string "don't"
do_not = "don't"
# sets the variable "y" equal to the string "Those who know..." with the format characters to insert the variables "binary" and "do_not" which contain strings themselves
y = "Those who know %s and those who %s." % (binary, do_not) # 1, 2

print x # prints x and y variables
print y

print "I said: %r." % x # 3
print "I also said: '%s'." % y # 4

hilarious = False # defines variable "hilarious" and sets equal to boolean "False"
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
