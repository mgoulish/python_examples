#! /usr/bin/python
  

# A tuple is an immutable sequence of things.

t = ( 1, 2, 3 )
print ( "tuple : ", t )

# They can be heterogenous.

number = 4.0
t = ( 1, 2, "three", number )
print ( "tuple : ", t )

# They can be any length.

t = ( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 )
print ( "tuple : ", t )

# You can access a particular element.

print ( "tuple[5] == ", t[5] )

# But you can't change an element.

# The following line would produce an error and
# abort the program. Uncomment it if you would 
# like to see the error.
# t[5] = 13


# Recognize tuples by their use of parentheses.


# Tuples are computationally less costly than lists.


# When should you use a tuple?
# Since you cannot add or delete elements once the tuple is 
# formed, tuples are good for situations where the position
# of a value in the ... collection? ... has meaning.
# I.e. like in math coordinates: (x, y) .  If you were to
# switch those values around, it would be a different 2D point.
# And if you were to add or delete a value ... it wouldn't be
# 2D a point any more.



