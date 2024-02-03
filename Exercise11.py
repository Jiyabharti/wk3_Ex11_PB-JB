#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
print(Belgium)

# ("3A) A line of splitPage the same length as the Belgium string, followed by")

#  Identified the length of the variable "Belgium" using len function
BelgiumLength = len(Belgium)
# multiplied the string "-" by the length of the variable Belgium
splitPage = "-" * BelgiumLength
print(splitPage)

# ("3B) The string with the comma colonSeparator replaced by colonSeparator ':', followed by")

# replace method used to change commas to colonSeparator
colonSeparator = Belgium.replace(",", ":")
print(colonSeparator)

# ("3C) The population of Belgium (the second field) plus the population of the capital city (the fourth field).")
# Hint the answer is 11183818

# converted the original list to a collection. Specifically a tuple
BelgiumTuple = ('Belgium', 10445852, 'Brussels', 737966, 'Europe', 1830, 'Euro', 'Catholicism', 'Dutch', 'French', 'German')
# print(type(BelgiumTuple))

# used an operator to sum the "1" and "3" values in my tuple
population = BelgiumTuple[1] + BelgiumTuple[3]
# print(population)
# s = f"Belgium has the population of ({BelgiumTuple[1]} + {BelgiumTuple[3]})"
populationTotal = f"The population of Belgium and Brussels is {population} people"
print(populationTotal)

# 3B Alternative:
# mytuple = "a","bee","cee"
# myseparator = ":"
# "mytuple" - replaces commas to colons
# "Belgium" - adds a column after each character
# "BlegiumTuple" - results in error - is it because .join only works with strings?
BelgiumTuple2 = ('Belgium', str(10445852), 'Brussels', str(737966), 'Europe', str(1830), 'Euro', 'Catholicism', 'Dutch', 'French', 'German')
# newColonSeperator = myseparator.join(mytuple)
# newColonSeperator = myseparator.join(Belgium)
# print(newColonSeperator)
print(BelgiumTuple2)

BelgiumSplit = Belgium.split("' ")
print(BelgiumSplit)

# Alternatives/Considerations/Questions
# What is the more efficient way to complete 3C?
# Is there a quicker way to extract the two values to add?
# if we had larger data, how could we convert the data to a collection quickly and identify the items to add?

# Alternative: slice the data? separate the collection into two.

# test git