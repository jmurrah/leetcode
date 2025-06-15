class Solution:
    def maxDiff(self, num: int) -> int:
        sn = str(num)
        r_min = r_max = None
        min_num, max_num = [], []

        for i in range(len(sn)):
            if (sn[i] != "0" and sn[i] != "1") and not r_min:
                r_min = sn[i]
            if sn[i] != "9" and not r_max:
                r_max = sn[i]
                
            min_digit = "0" if sn[0] != r_min and r_min else "1"
            min_num.append(min_digit if sn[i] == r_min else sn[i])
            max_num.append("9" if sn[i] == r_max else sn[i])
        
        return int("".join(max_num)) - int("".join(min_num))
