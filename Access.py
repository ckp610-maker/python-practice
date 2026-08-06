#Accessing String Characters
city = "Bangalore"
print(city[0])  #output: B

#We can also use navigate indexing to start counting from the ebd of the string
print(city[-1]) #Output: e(When we r considering from backward and starts with -1 -2-3 nd so on)

#Slicing Strings(You can extract a portion(substring) of a string uing slicing.
text = "Python Programming"
print(text[0:6]) #Output:Python(we have to give index+1 when we r giving last position)
print(text[:6])  #Output:Python
print(text[7:])  #Output:Programming
