class Solution(object):
    def fx(self,n):
        while(n):
            n-=1
            key = input()+1
            key = bin(key)[3:]
            re =''
            for i in key:
                if i=='1':
                    re+='7'
                else:
                    re+='4'
            print re


if __name__ =="__main__":
    k = input()
    # print k
    s=Solution()
    s.fx(k)
