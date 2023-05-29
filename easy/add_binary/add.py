class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ret = []
        carry = 0

        a_pos = len(a) - 1
        b_pos = len(b) - 1

        while a_pos >= 0 or b_pos >= 0 or carry == 1:
            if a_pos >=0:
                carry += int(a[a_pos])
                a_pos -= 1
            if b_pos >=0:
                carry += int(b[b_pos])
                b_pos -= 1
            # if 3 then 1 and carry
            # if 2 then 0 and carry
            # if 1
            # if 0
            # dunno if this is faster than modulo
            match carry:
                case 0:
                    ret.insert(0, 0)
                case 1:
                    ret.insert(0, 1)
                    carry = 0
                case 2:
                    ret.insert(0, 0)
                    carry = 1
                case 3:
                    ret.insert(0, 1)
                    carry = 1

        return ''.join(str(val) for val in ret)
