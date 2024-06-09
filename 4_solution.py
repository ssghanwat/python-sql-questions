def reverse_words(s):

  s = s.strip().replace("  ", " ")

  words = s.split()

  words.reverse()

  return " ".join(words)

s = "  hello world  "
result = reverse_words(s)
print(result)  
