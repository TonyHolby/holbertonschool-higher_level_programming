#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = (' '.join(str[5:7]) + ' '.join(str[12]) + ' '.join(str[0]))
print(str)