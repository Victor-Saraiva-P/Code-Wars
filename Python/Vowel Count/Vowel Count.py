def get_count(sentence):
    list_sentence = list(sentence)
    vogals = 0
    for i in list_sentence:
        i = i.lower()
        if i == "a":
          vogals+=1
        elif i == "e":
          vogals+=1
        elif i == "i":
          vogals+=1
        elif i == "o":
          vogals+=1
        elif i == "u":
          vogals+=1
    pass
  
get_count("victor")