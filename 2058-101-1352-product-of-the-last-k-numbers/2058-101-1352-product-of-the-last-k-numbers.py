class ProductOfNumbers:
    prods = []
    zeroIdx = -1

    def __init__(self):
        self.prods = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.zeroIdx = len(self.prods)
            self.prods.append(num)
        elif self.prods[-1] == 0:
            self.prods.append(num)
        else:
            self.prods.append(self.prods[-1] * num)

    def getProduct(self, k: int) -> int:
        if self.zeroIdx in range(len(self.prods) - k, len(self.prods)):
            return 0
        elif self.prods[-(k + 1)] == 0:
            return self.prods[-1]
        else:
            return self.prods[-1] // self.prods[-(k + 1)]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)