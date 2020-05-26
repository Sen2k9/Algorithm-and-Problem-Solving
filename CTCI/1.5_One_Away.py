

class Solution:

    def oneAway(self, str1, str2):

        # maintaining DRY

        if abs(len(str1) - len(str2)) > 1:
            return False

        string1 = ""
        string2 = ""

        if len(str1) > len(str2):
            string2 = str1
            string1 = str2
        else:
            string1 = str1
            string2 = str2

        diff = 0

        index1 = 0
        index2 = 0

        while index1 < len(string1) and index2 < len(string2):

            if string1[index1] != string2[index2]:

                if index1 != index2:
                    return False
                diff += 1

                if len(string1) == len(string2):

                    if diff > 1:
                        return False

                    index1 += 1

            else:
                index1 += 1

            index2 += 1

        return True

        #     if len(str1) == len(str2):
        #         return self.oneFlipReplace(str1, str2)

        #     elif len(str1) + 1 == len(str2):
        #         return self.oneFlipInsert(str1, str2)

        #     elif len(str1) - 1 == len(str2):
        #         return self.oneFlipInsert(str2, str1)

        #     return False  # if one of the string is more than one length apart

        # def oneFlipReplace(self, str1, str2):
        #     diff = 0

        #     for i in range(len(str1)):
        #         if str1[i] != str2[i]:
        #             diff += 1

        #         if diff > 1:
        #             return False

        #     return True

        # def oneFlipInsert(self, str1, str2):

        #     index1 = 0
        #     index2 = 0

        #     while index1 < len(str1) and index2 < len(str2):

        #         if str1[index1] != str2[index2]:

        #             if index1 != index2:
        #                 return False

        #             index2 += 1

        #         else:

        #             index1 += 1
        #             index2 += 1

        #         return True


sol = Solution()
print(sol.oneAway("apple", "aple"))
print(sol.oneAway("pale", "bake"))
