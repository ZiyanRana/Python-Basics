def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOU":
            translation = translation + 'G'
        elif letter in "aeiou":
            translation = translation + 'g'
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter the phrase to translate: ")))