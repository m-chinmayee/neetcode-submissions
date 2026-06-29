class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        sum = 0
        for i in range(len(operations)):
            if operations[i] == "+" and len(score) >= 2:
                score_sum = score[-1] + score[-2]
                score.append(score_sum)
                sum += score_sum
            elif operations[i] == "D" and len(score) >=1:
                score.append(2*score[-1])
                sum += score[-1]
            elif operations[i] == "C" and len(score) >= 1:
                last = score.pop(-1)
                sum -= last
            else:
                score.append(int(operations[i]))
                sum += int(operations[i])

        
        return sum