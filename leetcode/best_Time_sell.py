class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        s_len=len(prices)
        if(s_len<2):
            return 0
        else:
            tmp_min=prices[0]
            tmp_pro=0
            s_stack=[]
            s_stack.append(tmp_min)
            for i in range(1,s_len):
                s_stack.append(prices[i])
                tmp_min=min(tmp_min,s_stack.pop(0))
                if(prices[i]-tmp_min>tmp_pro):
                    tmp_pro=prices[i]-tmp_min
            return tmp_pro
                