def generate_square(n):
    return[i**2 for i in range(1,n)]
for x in generate_square(100):
    print(x)

def generate_square(n):
    for i in range(1,n):
        yield i**2
for i in generate_square(10):
    print(i)

