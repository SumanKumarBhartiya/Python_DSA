class GfG:
    def primeSum(self, n):
        sum = 0

        for i in range(2, n + 1):
            flag = 1
            for j in range(2, i // 2 + 1):
                if i % j == 0:
                    flag = 0
                    break

            if flag:
                sum += i

        return sum


gfg = GfG()
n = 10
result = gfg.primeSum(n)
print(result)