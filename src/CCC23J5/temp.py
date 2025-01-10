import os


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


def search_by_horizontal(search_word, rows, cols, maze):
    print("start search by horizontal")
    result = 0
    print(f"Finish search by horizontal: {result}")
    return result


def search_by_vertical(search_word, rows, cols, maze):
    print("start search by vertical")
    result = 0
    print(f"Finish search by vertical: {result}")
    return result


def search_by_diagonal(search_word, rows, cols, maze):
    print("start search by diagonal")
    result = 0
    print(f"Finish search by diagonal: {result}")
    return result


def search_by_perpendicular(search_word, rows, cols, maze):
    result = 0
    result += search_by_perpendicular_diagonal_horizontal(search_word, rows, cols, maze)
    result += search_by_perpendicular_diagonal_vertical(search_word, rows, cols, maze)
    result += search_by_perpendicular_diagonal_right(search_word, rows, cols, maze)
    result += search_by_perpendicular_diagonal_left(search_word, rows, cols, maze)
    return result


def search_by_perpendicular_diagonal_horizontal(search_word, rows, cols, maze):
    print("start search by perpendicular diagonal horizontal")
    result = 0
    print(f"Finish search by perpendicular diagonal horizontal: {result}")
    return result

def search_by_perpendicular_diagonal_vertical(search_word, rows, cols, maze):
    print("start search by perpendicular diagonal vertical")
    result = 0
    print(f"Finish search by perpendicular diagonal vertical: {result}")
    return result


def search_by_perpendicular_diagonal_right(search_word, rows, cols, maze):
    print("start search by perpendicular diagonal right")
    result = 0
    print(f"Finish search by perpendicular diagonal right: {result}")
    return result


def search_by_perpendicular_diagonal_left(search_word, rows, cols, maze):
    print("start search by perpendicular diagonal left")
    result = 0
    print(f"Finish search by perpendicular diagonal left: {result}")
    return result


def get_result(word, rows, cols, grid):
    result_horizontal = search_by_horizontal(word, rows, cols, grid)
    result_vertical = search_by_vertical(word, rows, cols, grid)
    result_diagnoal = search_by_diagonal(word, rows, cols, grid)
    result_perpendicular = search_by_perpendicular(word, rows, cols, grid)
    total_result = result_horizontal + result_vertical + result_diagnoal + result_perpendicular
    result = f"total result: {total_result}"
    return result


if __name__ == "__main__":
    main()
