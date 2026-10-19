import re
text1 = "это   строка   с   большим   количеством   пробелов."
result1 = re.sub(r"\s+", " ", text1)
print(result1)
text2 = "   текст   с   пробелами   "
result2 = re.sub(r"\s+", " ", text2).strip()
print(result2)