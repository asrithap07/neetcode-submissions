class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        boxes = {}

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue

                box = (r // 3, c // 3)

                if r not in rows:
                    rows[r] = set()
                if c not in cols:
                    cols[c] = set()
                if box not in boxes:
                    boxes[box] = set()

                if val in rows[r]:
                    return False
                if val in cols[c]:
                    return False
                if val in boxes[box]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box].add(val)

        return True