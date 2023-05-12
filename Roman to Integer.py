class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        strlen = len(s)
        for i in range(strlen):
            next = s[i+1] if i+1 < strlen else None
            match s[i]:
                case 'I':
                    if next == 'V' or next == 'X':
                        sum -= 1
                    else:
                        sum += 1
                case 'V':
                    sum += 5
                case 'X':
                    if next == 'L' or next == 'C':
                        sum -= 10
                    else:
                        sum += 10
                case 'L':
                    sum += 50
                case 'C':
                    if next == 'D' or next == 'M':
                        sum -= 100
                    else:
                        sum += 100
                case 'D':
                    sum += 500
                case 'M':
                    sum += 1000
        return sum
