import pdb


class Solution:
    def merge_split(self, number):
        if len(number) < 2:
            return number

        n = len(number)
        m = n // 2
        left = number[0:m]
        right = number[m:]

        left_inv = self.merge_split(left)
        right_inv = self.merge_split(right)

        merge_inv = self.merge_sort(left_inv, right_inv, n)

        return merge_inv

    def merge_sort(self, left, right, n):
        arr=[0]*n
        inversion = 0
        k =0
        i=0
        j=0 
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i +=1
                k +=1
            else:
                inversion += (len(left) - i)
                arr[k] = right[j]
                j +=1
                k +=1
        while i < len(left):
            arr [k] = left[i]
            i +=1
            k +=1

        while j < len(right):
            arr [k] = right[j]
            j +=1
            k +=1

        return inversion



    # def isOneBitCharacter(self, bits):
    #     i = 0
    #     single = 0
    #     double = 0
	
    #     while i< len(bits)-1:
    #         if bits[i] == 0:
    #             #single +=1
    #             i +=1
    #         else:
    #             #double +=1
    #             i +=2
    #     if i == len(bits)-1:
    #         return True
    #     else:
    #         return False
				
				
                
        


sol = Solution()
#pdb.set_trace()
# bits = [0,1,1,0,0]
# print(sol.isOneBitCharacter(bits))
numbers = [1, 3, 5, 2, 4, 6]
#target = 12
pdb.set_trace()
print(sol.merge_split(numbers))
