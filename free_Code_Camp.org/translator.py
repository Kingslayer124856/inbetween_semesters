"""
Building a translator
by; Cassandra King
Date; 2/1/20
Note: Any vowels become a 'g' to transfer the phrase into 'Giraffe Language'
"""

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a Phrase: ")))
