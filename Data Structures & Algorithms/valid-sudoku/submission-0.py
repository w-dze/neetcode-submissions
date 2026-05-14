class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row = len(board)
        col = len(board[0])

        # check rows
        for i in range(row):
            seen = set()

            for num in board[i]:
                if num == ".":
                    continue

                if num in seen:
                    return False

                seen.add(num)

        # check columns
        for j in range(col):
            seen = set()

            for i in range(row):
                num = board[i][j]

                if num == ".":
                    continue

                if num in seen:
                    return False

                seen.add(num)

        # check 3x3 boxes
        for boxRow in range(0, 9, 3):
            for boxCol in range(0, 9, 3):
                seen = set()

                for i in range(boxRow, boxRow + 3):
                    for j in range(boxCol, boxCol + 3):
                        num = board[i][j]

                        if num == ".":
                            continue

                        if num in seen:
                            return False

                        seen.add(num)

        return True