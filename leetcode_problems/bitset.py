class Bitset:

    def __init__(self, size: int):
        self.bitset = ['0'] * size
        self.total = 0
        self.size = size
        print(self.bitset)

    def fix(self, idx: int) -> None:
        if self.bitset[idx] == '0':
            self.bitset[idx] = '1'
            self.total  += 1

    def unfix(self, idx: int) -> None:
        if self.bitset[idx] == '1':
            self.bitset[idx] = '0'
            self.total  -= 1

    def flip(self) -> None:
        for i in range(self.size):
            if self.bitset[i] == '1':
                self.bitset[i] = '0'
                self.total -= 1
            else:
                self.bitset[i] = '1'
                self.total += 1
        print(self.bitset)  

    def all(self) -> bool:
        return self.total == self.size

    def one(self) -> bool:
        return self.total > 0

    def count(self) -> int:
        return self.total 

    def toString(self) -> str:
        print(self.bitset)
        return ''.join(self.bitset)


# Your Bitset object will be instantiated and called as such:
obj = Bitset(2)
obj.flip()
obj.unfix(1)
obj.all()
obj.fix(1)
obj.fix(1)
obj.unfix(1)
print(obj.all())
obj.count()
obj.toString()
obj.toString()


["Bitset","flip","unfix","all","fix","fix","unfix","all","count","toString","toString","toString","unfix","flip","all","unfix","one","one","all","fix","unfix"]
[[2],[],[1],[],[1],[1],[1],[],[],[],[],[],[0],[],[],[0],[],[],[],[0],[0]]