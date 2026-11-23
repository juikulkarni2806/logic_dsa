class Solution:
    def removeElement(self,nums: list[int], val: int) -> int:
        j=0
        for i in range(len(nums)):
            if (nums[i])!=val:
                nums[j]=nums[i]
                j+=1

        return j

    num=[1,3,2,4,3,5]
    removeElement(1,nums=[1,3,2,4,2,3,21,3],val=3)