import os


def parse_test_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    word = lines[0].strip()
    rows = int(lines[1].strip())
    cols = int(lines[2].strip())
    grid = [line.strip().split() for line in lines[3:]]
    return word, rows, cols, grid


def get_result(word, rows, cols, grid):
    return "test_result"


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


if __name__ == "__main__":
    main()
