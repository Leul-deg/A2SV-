class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real_1 , complex_1 = num1.split("+")
        real_2 , complex_2 = num2.split("+")
        real_1 = int(real_1)
        complex_1 = int(complex_1[:len(complex_1 )-1])
        real_2 = int(real_2)
        complex_2 = int(complex_2[:len(complex_2 )- 1])
        res_real = real_1 * real_2 - complex_1 * complex_2
        res_complex = real_1 * complex_2 + real_2 * complex_1
        return str(res_real) + "+" + str(res_complex) + "i"
        
        