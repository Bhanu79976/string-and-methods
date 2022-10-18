r="hello world"
a=r.maketrans("l","r")
print(r.translate(a))

h="hello welcome to the world"
print(h.split(" "))
print(h.split(''))
print(h.split(""))

v=r"hello\bollywood"
print(v,type(v))

a="hell\to"
print(a.expandtabs(1))
print(a.expandtabs(2))

a="hello\ncore python\n programming"
g=a.splitlines()
print(g.type(g))

a=[int(x) for x in input().split()]
print(sum(a))

b="hello:welcome:to:josh:innnovations"
print(b.split(":"))

f='hi\ballon'
print(f)

f='hi\\ballon'
print(f)
