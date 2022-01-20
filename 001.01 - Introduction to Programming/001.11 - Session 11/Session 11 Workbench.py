import re
s = "Kern County [661]"
pattern = "\[(.*?)\]"
substring = re.search(pattern, s).group(1)
print(substring)