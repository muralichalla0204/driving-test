#m = "naresh"
#print(m[::-1])

#m = "naresh"
#print(m[0:2]+m[2:][::-1])

#m = "naresh padamala"
#print(m.split()[::-1])

m = "padamala"
h =[]
for i in m:
    if i not in "aeiou":
        h.append(i)
print(h)

m = "hello sri"
g = []
for i in m:
    if i in "aeiou" and i not in g:
        g.append(i)
print(g)

m = 123123
d = []
for i in str(m):
    if str(m).count(i)>1 and i not in d:
        d.append(i)
print(d)

m = 123
p = 0
for i in str(m):
     p +=1
print(p)

M = "121"
if M == M[::-1]:
    print("palenfrom")














