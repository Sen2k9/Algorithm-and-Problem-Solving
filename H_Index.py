"""
Problem

It is important for researchers to write many high quality academic papers. Jorge has recently discovered a way to measure how impactful a researcher's papers are: the H-index.

The H-index score of a researcher is the largest integer h such that the researcher has h papers with at least h citations each.

Jorge has written N papers in his lifetime. The i-th paper has Ai citations. The number of citations that each paper has will never change after it is written. Please help Jorge determine his H-index score after each paper he wrote.
Input

The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a line containing N, the number of papers Jorge wrote.

The second line contains N integers. The i-th integer is Ai, the number of citations the i-th paper has.
Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is a space-separated list of integers. The i-th integer is the H-index score after Jorge wrote his i-th paper.
Limits

Time limit: 50 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
1 ≤ Ai ≤ 105.
Test set 1 (Visible)

1 ≤ N ≤ 1000.
Test set 2 (Hidden)

1 ≤ N ≤ 105.
Sample

Input
  	
Output
 

2
3
5 1 2
6
1 3 3 2 2 15

  

	

Case #1: 1 1 2
Case #2: 1 1 2 2 2 3

  

In Sample Case #1, Jorge wrote N = 3 papers.

    After the 1st paper, Jorge's H-index score is 1, since he has 1 paper with at least 1 citation.
    After the 2nd paper, Jorge's H-index score is still 1.
    After the 3rd paper, Jorge's H-index score is 2, since he has 2 papers with at least 2 citations (the 1st and 3rd papers).


In Sample Case #2, Jorge wrote N = 6 papers.

    After the 1st paper, Jorge's H-index score is 1, since he has 1 paper with at least 1 citation.
    After the 2nd paper, Jorge's H-index score is still 1.
    After the 3rd paper, Jorge's H-index score is 2, since he has 2 papers with at least 2 citations (the 2nd and 3rd papers).
    After the 4th paper, Jorge's H-index score is still 2.
    After the 5th paper, Jorge's H-index score is still 2.
    After the 6th paper, Jorge's H-index score is 3, since he has 3 papers with at least 3 citations (the 2nd, 3rd and 6th papers).
"""


class Solution:
    def h_index(self, n, citations):
        if n == 0:
            return 0
        dictionary = {}
        max_citation = 1
        result = [1] * n
        dictionary[1] = 1
        for j, each in enumerate(citations):
            if each > max_citation:

                for i in range(max_citation, each + 1):
                    dictionary[i] = dictionary.get(i, 0) + 1
                    if dictionary[i] >= i:
                        max_citation = i

            result[j] = max_citation
        return result


sol = Solution()
n = 10
c = [5, 2, 3, 4, 3, 4, 5, 2, 5, 4]
#print(sol.h_index(n, c))


test_case = eval(input())
for t in range(test_case):
    n = eval(input())
    if n == 0:
        print("Case #{}: {}".format(t + 1, 0))
        continue
    dictionary = {}
    max_citation = 1
    result = [1] * n
    dictionary[1] = 1
    citation = []
    citation = input().split(" ")
    for j, each in enumerate(citation):
        each = int(each)

        if each > max_citation:
            for i in range(max_citation, each + 1):
                dictionary[i] = dictionary.get(i, 0) + 1
                if dictionary[i] >= i:
                    max_citation = i

        result[j] = str(max_citation)

    print("Case #{}: {}".format(t+1, " ".join(result)))


"""
algo:
taking a taly(1 to Ai), but whenever the largest one meets the criteria dictionary[citanation_number] >=paper_number, take it as the max_citation
and ignore to update the lower values (values < max_citation)
"""
