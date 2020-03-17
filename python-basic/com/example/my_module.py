PI = 3.141592

class Math:
    def solv(self, r):
        return PI * (r ** 2)

def sum(a, b):
    return a + b

if __name__ == "__main__":
    print(PI)
    m = Math()
    print( m.solv(10) )
    print( sum(10, 20) )