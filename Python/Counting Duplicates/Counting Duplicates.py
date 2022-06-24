def duplicate_count(text):
    # Your code goes here
    text = text.lower()
    letters = {}
    duplicates = 0
    for i in text:
        letters[i] = -1
    for i in text:
      letters[i] += 1
    for i in letters:
      if letters[i] > 0:
        duplicates += 1
    return duplicates 

print(duplicate_count(""))
