from sys import stdin

class Matrix2d:
    a:int
    b:int
    c:int
    d:int

    def __init__(self, lines:list) -> None:
        # print(f"Input: {lines}")
        assert(len(lines)>=2)
        self.a,self.b = (int(x) for x in lines[0].split())
        self.c,self.d = (int(x) for x in lines[1].split())

    def inverse(self) -> str:
        a,b,c,d = self.a,self.b,self.c,self.d
        denominator = 1/(a*d-b*c)
        aa = int(denominator * d)
        bb = int(denominator * -b)
        cc = int(denominator * -c)
        dd = int(denominator * a)
        return f"{aa} {bb}\n{cc} {dd}"

# main
# print(Matrix2d("1 0\n0 1").inverse())
# assert(Matrix2d(["1 0","0 1"]).inverse()=="1 0\n0 1")

lines = list(stdin.readlines())
lines = [l.strip() for l in lines if l.strip()!=""]
# print(lines)

for i in range(len(lines)//2):
    # print(f"Indexes: {2*i},{(2*i)+2}")
    m = Matrix2d(lines[2*i:(2*i)+2])
    print(f"Case {i+1}:")
    print(m.inverse())