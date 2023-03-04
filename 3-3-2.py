s=input("Введите несколько слов: ")

def short_words(s):
    sw=[]
    import string
    string.punctuation
    for p in string.punctuation:
        if p in s:
            s=s.replace(p, "")
    s=s.split()
    for i in range(0, len(s)):
        if len(s[i])<5:
            sw.append(s[i])
    sn=", ".join(sw)
    return sn

print(short_words(s))