m = 10
a = 0
b = 1
for i in range(m):
    print(a)
    a ,b=b,a+b

m = 'naresh'
print(m[:2]+m[2:][::-1])

m = [1,0,2,0]
h = [0,2,3]
m.extend(h)
m.sort()
result =[]
for i in m:
    if i !=0:
      result.append(i)
for i in m:
    if i ==0:
      result.append(i)
print(result)


def name(msc):
    def happy():
        print("msc")
        msc()
        print("hello")

    return happy


@name
def fam():
    print("name")
fam()

class name:
    def ahr(self):
        print('hari')


class city(name):
    def seri(self):
        super().ahr()
        print("cit")


cn = city()
cn.seri()