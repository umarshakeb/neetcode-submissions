class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a)-1
        j = len(b)-1
        carry = 0
        result = []
        while i>=0 or j>=0 or carry !=0:
            digit_a = int(a[i]) if i>=0 else 0
            digit_b = int(b[j]) if j>=0 else 0
            total = digit_a + digit_b + carry
            final = total%2
            result.append(final)
            carry = total//2
            i-=1
            j-=1
        result.reverse()
        output = ''.join(map(str,result))    
        return output

        