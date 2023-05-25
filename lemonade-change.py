class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c = defaultdict(int)
        for  bill in bills:
            change =  bill - 5

            if change and not c.get(5):
                return False

            if change == 5:
                if not c.get(5):
                    return False
                c[5] -= 1

            
            elif change == 15:

                #try 10 + 5
                if c.get(10):
                    c[5] -= 1
                    c[10] -= 1
                
                else:
                    if c.get(5 ,  0 ) * 5 < 15:
                        return False

                    c[5] -= 3

            c[bill] += 1
        return True 
            

                
                
                

        #     c[bill] += 1
        # return True