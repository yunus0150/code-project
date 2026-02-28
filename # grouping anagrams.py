# grouping anagrams
words = input().split()
mp= {}
for word in words:
    key= "" .join(sorted(word))
    mp.setdefault(key,[]).append(word)
print(list(mp.values()))    