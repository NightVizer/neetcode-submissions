
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        j = 0;
        # проверяем все столбцы
        while j < len(board):
            values = set()
            i = 0
            # бежим по всему столбцу
            while i < len(board):
                if board[i][j] == '.':
                    i += 1
                    continue
                if board[i][j] in values:
                    return False
                else:
                    values.add(board[i][j])
                i += 1
            j += 1

        # пробегаем строки
        i = 0;
        while i < len(board):
            values = set()
            j = 0
            # бежим по всей строке
            while j < len(board):
                if board[i][j] == '.':
                    j += 1
                    continue
                if board[i][j] in values:
                    return False
                else:
                    values.add(board[i][j])
                j += 1
            i += 1

        # проверяем блоки
        # проверяем блоки
        bool_result = True;
        for start_i in range(0, 7, 3):
            for start_j in range(0, 7, 3):
                values = set()

                for plus_i in range(0, 3):
                    for plus_j in range(0, 3):
                        if board[start_i + plus_i][start_j + plus_j] == '.':
                            continue
                        bool_result = bool_result and self.TryAddValue(board[start_i + plus_i][start_j + plus_j],values)

        if bool_result:
            return True
        else:
            return False

    def TryAddValue(self, value: str, values: set) -> bool:
        if value in values:
            return False
        else:
            values.add(value)
            return True
