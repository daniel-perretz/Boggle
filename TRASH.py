from typing import List, Tuple, Dict

MAX_ROW = 3
MAX_COL = 3
MAX_DIFFERENCE = 1


def load_words_dict(file_path):
    with open(file_path) as f:
        content = f.read().splitlines()
        word_dict = {x: True for x in content}
    return word_dict


def find_length_n_words(n, board, words):
    words_list = minimize_dict(n, words)  # filters words that are too long
    output = []
    for y in range(len(board)):
        for x in range(len(board[0])):
            print(f"Outside loop in ({x}, {y})")
            output += finder_helper(n, "", [], (x, y), board, words_list)
    return output


def finder_helper(n: int, path: str, coordinates: List[Tuple[int, int]],
                  cur_step: Tuple[int, int], board: List[List[str]],
                  words_list: List[str]):

    x, y = cur_step
    if x > MAX_ROW or y > MAX_COL or x < 0 or y < 0:  # out of bounds
        return []
    if cur_step in coordinates:  # duplicated coordinate
        return []
    print("         I'm assesing board value")
    addition: int = len(board[x][y])
    path += board[x][y]
    if not is_path_possible(path, words_list):  # no matching words in list
        return []
    coordinates = coordinates + [cur_step]

    if n == 0:  # base case
        if path in words_list:
            print("decided in", cur_step, "to add word")
            return [(path, coordinates)]
        else:
            return []
    if n < 0:
        return []


    output = []
    neighbors = [(x + 1, y), (x + 1, y + 1), (x, y + 1), (x + 1, y - 1),
                 (x, y - 1), (x - 1, y - 1), (x - 1, y), (x - 1, y + 1)]
    print(f" I'm recursively calling all ({x}, {y}) neighbors:")
    for neighbor in neighbors:
        print(f"   n = {n - addition}, path = {path}, neighbor = {neighbor}")
        output +=\
            finder_helper(n - addition, path, coordinates, neighbor, board,
                          words_list)
    return output
    # do not update path or coordinate as they do that in the next call


def minimize_dict(n: int, words: Dict[str, bool]) -> List[str]:
    """ Extracts from a dictionary a list of words up to a given length"""
    output = []
    for word in words:
        if len(word) <= n:
            output.append(word)
    return output


def is_path_possible(path: str, words_list: List[str]):
    """ Checks if any of the words in a given list start with a given string"""
    for word in words_list:
        if len(word) < len(path):
            continue
        for i in range(len(path)):
            if path[i] == word[i]:
                if i == len(path) - 1:  # -> word starts with the whole "path"
                    return True
                continue  # check the next letter
            else:
                break
    # meaning no word in list starts with path
    return False


if __name__ == '__main__':
    board0 = [['C', 'A'],
              ['Q', 'Q']]
    word_dict0 = {'CA': True}
    # print(find_length_n_words(2, board0, word_dict0))
    board1 = [['C', 'A', 'T', 'Q'],
             ['D', 'O', 'G', 'Q'],
             ['B', 'I', 'T', 'Q'],
             ['Q', 'Q', 'Q', 'Q']]
    word_dict1 = {'CAT': True, 'DOG': True, 'BIT': True}
    expected1 = [("CAT", [(0, 0), (0, 1), (0, 2)]),
                ("DOG", [(1, 0), (1, 1), (1, 2)]),
                ("BIT", [(2, 0), (2, 1), (2, 2)])]
    # print(find_length_n_words(3, board1, word_dict1))
    board2 = [['Q', 'Q', 'Q', 'Q'],
             ['DO', 'GS', 'Q', 'Q'],
             ['Q', 'Q', 'Q', 'Q'],
             ['Q', 'Q', 'Q', 'Q']]
    word_dict2 = {'DOGS': True}
    expected2 = [("DOGS", [(1, 0), (1, 1)])]
    # print(find_length_n_words(2, board2, word_dict2))
