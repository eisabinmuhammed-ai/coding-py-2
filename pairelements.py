class pair:
    def twonum(self,nums,target):
        lookup={}
        for i,num in enumerate(nums):
            if target-num in lookup:
                return (lookup[target-num],i)
            lookup[num]=i
vale=int(input("enter number"))
print("indx1=%d, index2=%d"%pair().twonum((10,30,50,70),vale))  