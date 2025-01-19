sentence = input("Enter a sentence :\n")
sentence = sentence.lower()
vowels = "aeiou"
vowels_count = 0 

for char in sentence:
    if char in vowels:
        vowels_count += 1 

print(f"The number of vowels in sentence is : {vowels_count}")