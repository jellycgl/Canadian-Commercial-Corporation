import os


def split_str(search_word):
    sub_str_list = []
    word_size = len(search_word)
    for i in range(1, word_size):  # 分割点从 1 到 word_size - 1
        sub_str_list.append([search_word[:i], search_word[i:]])
    return sub_str_list


def parse_test_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    word = lines[0].strip()
    rows = int(lines[1].strip())
    cols = int(lines[2].strip())
    grid = [line.strip().split() for line in lines[3:]]
    return word, rows, cols, grid


def main():
    test_folder = "./test_data"
    
    if not os.path.exists(test_folder):
        print(f"Folder {test_folder} not found!")
        return
    
    # Loop test data
    for test_file in os.listdir(test_folder):
        if test_file.endswith(".txt"):
            file_path = os.path.join(test_folder, test_file)
            print(f"\nProcessing {test_file}...")

            word, rows, cols, grid = parse_test_file(file_path)

            print(f"Word to search: {word}")
            print(f"Grid size: {rows}x{cols}")
            print("Grid:")
            for row in grid:
                print(" ".join(row))

            result = get_result(word, rows, cols, grid)
            print(f"Result: {result}")


def check_same(compare_list, word):
    if ''.join(compare_list) == word:
        return True
    compare_list.reverse()
    if ''.join(compare_list) == word:
        return True
    return False


def search_by_horizontal(search_word, maze, is_horizontal=True):
    if is_horizontal:
        print("start search by horizontal")
    result = 0
    word_size = len(search_word)
    maze_col = len(maze[0])
    maze_row = len(maze)
    for r in range(maze_row):
        line = maze[r]
        for c in range(maze_col - word_size + 1):
            word = line[c:c+word_size]
            if check_same(word, search_word):
                result += 1
    if is_horizontal:
        print(f"Finish search by horizontal: {result}")
    return result


def search_by_vertical(search_word, maze):
    print("start search by vertical")
    maze_revert = [[maze[r][c] for r in range(len(maze))] for c in range(len(maze[0]))]
    result = search_by_horizontal(search_word, maze_revert, False)
    print(f"Finish search by vertical: {result}")
    return result


def search_by_diagonal(search_word, maze):
    print("start search by diagonal")
    result = 0
    word_size = len(search_word)
    maze_col = len(maze[0])
    maze_row = len(maze)
    for r in range(maze_row):
        for c in range(maze_col):
            if r + word_size <= maze_row and c + word_size <= maze_col:
                word_left_down = [maze[r+i][c+i] for i in range(word_size)]
                if check_same(word_left_down, search_word):
                    result += 1
            if r + word_size <= maze_row and c - word_size + 1 >= 0:
                word_right_down = [maze[r+i][c-i] for i in range(word_size)]
                if check_same(word_right_down, search_word):
                    result += 1
    print(f"Finish search by diagonal: {result}")
    return result


def search_by_perpendicular(search_word, maze):
    result = 0
    result += search_by_perpendicular_diagonal_horizontal(search_word, maze)
    result += search_by_perpendicular_diagonal_vertical(search_word, maze)
    result += search_by_perpendicular_diagonal_right(search_word, maze)
    result += search_by_perpendicular_diagonal_left(search_word, maze)
    return result


def search_by_perpendicular_diagonal_horizontal(search_word, maze):
    print("start search by perpendicular diagonal horizontal")
    result = 0
    sub_str_list = split_str(search_word)
    maze_row = len(maze)
    maze_col = len(maze[0])
    
    for sub_str in sub_str_list:
        str1, str2 = sub_str[0], sub_str[1]
        str1_size = len(str1)
        str2_size = len(str2)
        
        for r in range(maze_row):
            for c in range(maze_col - str1_size + 1):  # 水平起点
                word = [maze[r][c + i] for i in range(str1_size)]
                if ''.join(word) == str1:
                    # 检查向上的垂直部分
                    if r >= str2_size:
                        up_words = [maze[r - 1 - j][c + str1_size - 1] for j in range(str2_size)]
                        if ''.join(up_words) == str2:
                            result += 1
                    # 检查向下的垂直部分
                    if r + str2_size < maze_row:
                        down_words = [maze[r + 1 + j][c + str1_size - 1] for j in range(str2_size)]
                        if ''.join(down_words) == str2:
                            result += 1
    print(f"Finish search by perpendicular diagonal horizontal: {result}")
    return result


def search_by_perpendicular_diagonal_vertical(search_word, maze):
    print("start search by perpendicular diagonal vertical")
    result = 0
    sub_str_list = split_str(search_word)
    maze_row = len(maze)
    maze_col = len(maze[0])
    
    for sub_str in sub_str_list:
        str1, str2 = sub_str[0], sub_str[1]
        str1_size = len(str1)
        str2_size = len(str2)
        
        for c in range(maze_col):
            for r in range(maze_row - str1_size + 1):  # 垂直起点
                word = [maze[r + i][c] for i in range(str1_size)]
                if ''.join(word) == str1:
                    # 检查向左的水平部分
                    if c >= str2_size:
                        left_words = [maze[r + str1_size - 1][c - 1 - j] for j in range(str2_size)]
                        if ''.join(left_words) == str2:
                            result += 1
                    # 检查向右的水平部分
                    if c + str2_size < maze_col:
                        right_words = [maze[r + str1_size - 1][c + 1 + j] for j in range(str2_size)]
                        if ''.join(right_words) == str2:
                            result += 1
    print(f"Finish search by perpendicular diagonal vertical: {result}")
    return result


def search_by_perpendicular_diagonal_right(search_word, maze):
    print("start search by perpendicular diagonal right")
    result = 0
    sub_str_list = split_str(search_word)
    for sub_str in sub_str_list:
        str1, str2 = sub_str[0], sub_str[1]
        str1_size = len(str1)
        str2_size = len(str2)
        maze_col = len(maze[0])
        maze_row = len(maze)
        for r in range(maze_row):
            for c in range(maze_col):
                if r < maze_row - str1_size + 1 and c >= str1_size - 1:
                    word = [maze[r+i][c-i] for i in range(str1_size)]
                    if ''.join(word) == str1:
                        if c - str1_size + 1 >= str2_size and str1_size > str2_size:
                            up_words = [maze[r+str1_size-2-j][c-str1_size-j] for j in range(str2_size)]
                            if ''.join(up_words) == str2:
                                result += 1
                        if c - str1_size + str2_size +1 < maze_col and r + str1_size + str2_size <= maze_row:
                            down_words = [maze[r+str1_size+j][c-str1_size+2+j] for j in range(str2_size)]
                            if ''.join(down_words) == str2:
                                result += 1
                        continue
                    word.reverse()
                    if ''.join(word) == str1:
                        if r >= str2_size and c > str2_size:
                            up_words = [maze[r-1-j][c-1-j] for j in range(str2_size)]
                            if ''.join(up_words) == str2:
                                result += 1
                        if c + str2_size < maze_col and r + str2_size < maze_row:
                            down_words = [maze[r+1+j][c+1+j] for j in range(str2_size)]
                            if ''.join(down_words) == str2:
                                result += 1
    print(f"Finish search by perpendicular diagonal right: {result}")
    return result


def search_by_perpendicular_diagonal_left(search_word, maze):
    print("start search by perpendicular diagonal left")
    result = 0
    sub_str_list = split_str(search_word)
    for sub_str in sub_str_list:
        str1, str2 = sub_str[0], sub_str[1]
        str1_size = len(str1)
        str2_size = len(str2)
        maze_col = len(maze[0])
        maze_row = len(maze)
        
        for r in range(maze_row):
            for c in range(maze_col):
                # Check for matching str1
                if r >= str1_size - 1 and c + str1_size <= maze_col:
                    word = [maze[r - i][c + i] for i in range(str1_size)]
                    if ''.join(word) == str1:
                        # Check for str2 above
                        if r >= str1_size + str2_size - 1 and c + str1_size + str2_size <= maze_col:
                            up_words = [maze[r - str1_size - j][c + str1_size + j] for j in range(str2_size)]
                            if ''.join(up_words) == str2:
                                result += 1
                        # Check for str2 below
                        if r + str2_size < maze_row and c >= str2_size - 1:
                            down_words = [maze[r + 1 + j][c - str2_size + 1 + j] for j in range(str2_size)]
                            if ''.join(down_words) == str2:
                                result += 1
                        continue
                    
                    # Check reversed str1
                    word.reverse()
                    if ''.join(word) == str1:
                        # Check for str2 above
                        if r >= str2_size and c >= str2_size:
                            up_words = [maze[r - 1 - j][c + 1 + j] for j in range(str2_size)]
                            if ''.join(up_words) == str2:
                                result += 1
                        # Check for str2 below
                        if r + str2_size < maze_row and c + str2_size < maze_col:
                            down_words = [maze[r + 1 + j][c + 1 + j] for j in range(str2_size)]
                            if ''.join(down_words) == str2:
                                result += 1
    print(f"Finish search by perpendicular diagonal left: {result}")
    return result


def get_result(word, rows, cols, grid):
    result_horizontal = search_by_horizontal(word, grid)
    result_vertical = search_by_vertical(word, grid)
    result_diagnoal = search_by_diagonal(word, grid)
    result_perpendicular = 0
    #result_perpendicular = search_by_perpendicular(word, grid)
    total_result = result_horizontal + result_vertical + result_diagnoal + result_perpendicular
    result = f"total result: {total_result}"
    return result


if __name__ == "__main__":
    main()
