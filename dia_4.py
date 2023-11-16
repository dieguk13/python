# Single line comment
letter = 'D'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be  a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = 'Espero estes disfrutando el lenguaje Python'
print(sentence)

# Multiline String
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)
# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)

# String Concatenation
nombre = 'diego'
apellido = 'londono'
space = ' '
full_name = nombre  +  space + apellido
print(full_name) # diego londono
# Checking length of a string using len() builtin function
print(len(nombre))  # 8
print(len(apellido))   # 7
print(len(nombre) > len(apellido)) # false
print(len(full_name)) # 13

#### Unpacking characters 
language = 'Diego'
a,b,c,d,e = language # unpacking sequence characters into variables
print(a) # D
print(b) # I
print(c) # E 
print(d) # G
print(e) # O
