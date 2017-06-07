name = 'Cyrus L. Sethna'
age = 25 # not a lie
height = (5 * 12 + 6) * 2.54 # 5'6" to inches, 2.54 centimeters = 1 inch
weight = 155 * 0.453592 # 1 pound = 0.453592 kg
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." % name
print "He's %d centimeters tall." % height
print "He's %d kilos heavy." % weight
print "Actually, that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % (teeth)

print "if I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
