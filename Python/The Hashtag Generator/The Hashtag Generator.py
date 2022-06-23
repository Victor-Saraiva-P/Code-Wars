def generate_hashtag(s):
    if len(s) == 0:
        return False
    word = "#" + "".join([i.capitalize() for i in s.split()])
    if len(word) > 140:
        return False
    else:
        return word


print(generate_hashtag("victor alexandre"))
