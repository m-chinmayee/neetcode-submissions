class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        h_dict = defaultdict(set)
        v_dict = defaultdict(set)
        s_dict = defaultdict(set)

        for row in range(9):
            for col in range(9):
                el = board[row][col]
                if el == ".":
                    continue

                if el in h_dict[row] or el in v_dict[col] or el in s_dict[(row//3, col//3)]:
                    return False

                h_dict[row].add(el)
                v_dict[col].add(el)
                s_dict[(row//3, col//3)].add(el)

        return True