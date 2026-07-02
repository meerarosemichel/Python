#Strings

text="I am from nagercoil"
print(text)
print(text[-1])
print(text[:4])
print(text[4::2])
print(text[::-1])

#string manuplation
text="I am from nagercoil"
print(text)
print(text[-1])
print(text[:4])
print(text[::-1])
print(len(text))
text_upper=text.upper()
print(text_upper)
print(text.capitalize())
print(text.title())
print(text.strip())
print(text.split(" "))

new_text="so far it's been a great climate in coimbatore "
new_list=new_text.split(" ")
print(new_list)
str=" ".join(new_list)
print(str)
print(text.find("amaa"))
print(str.find("climate"))
print(str.count("in"))

#upper 
text1 = "coimbatore is wonderful city"
text1_upper=text1.upper()
print(text1_upper)
#strip
print(text1.strip())
#split
text2=text1.split(" ")
print(text2)

test="kavi"
if test.isalpha():
    print(f"'{test}' is a letter")
elif test.isdigit():
    print(f" '{test}' is a number")
elif test.isspace():
    print(f" '{test}' is a whitespace")
else:
    print(f" '{test}' is any other symbol")
