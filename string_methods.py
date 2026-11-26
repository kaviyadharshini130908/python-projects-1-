
text = "  Hello Python Student  "
print("Lowercase:", text.lower())
clean_text = text.strip()
print("After strip:", clean_text)
words = clean_text.split()
print("After split:", words)
joined_text = "-".join(words)
print("After join:", joined_text)
new_text = clean_text.replace("Python", "AIML")
print("After replace:", new_text)
if "Python" in clean_text:
    print("Python is present in the string.")
else:
    print("Python is not present.")
