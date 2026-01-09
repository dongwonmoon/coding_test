croatian = input()
alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for a in alphabet:
    if a in croatian:
        croatian = croatian.replace(a, "*")

c_count = croatian.count("*")
print(c_count + len(croatian.replace("*", "")))
