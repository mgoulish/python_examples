#! /usr/bin/python
  

file_name = "02_output"
dst = open ( file_name, 'w' )
print ( "Hello, World!", file=dst )

print ( "\n    Output was written to file |" + file_name  + "|.\n" )

