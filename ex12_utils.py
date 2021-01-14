from typing import List, Tuple, Dict

MAX_ROW = 3
MAX_COL = 3
MAX_DIFFERENCE = 1


def load_words_dict(file_path):
    with open(file_path) as f:
        content = f.read().splitlines()
        word_dict = {x: True for x in content}
    return word_dict


def is_valid_path(board, path, words):
    for coor in path:
        x, y = coor
        if x > MAX_ROW or y > MAX_COL:
            return None
    for i in range(len(path) - 1):
        x1, y1 = path[i]
        x2, y2 = path[i + 1]
        if abs(x1 - x2) > MAX_DIFFERENCE or abs(y1 - y2) > MAX_DIFFERENCE:
            return None
    dup_list = set(path)  # check for double coordinate
    if len(dup_list) < len(path):
        return None
    word = ''
    for coor in path:
        x, y = coor
        word += board[x][y]  # join didnt work for some reason
    if word in words:
        return word
    return None


def find_length_n_words(n, board, words):
    """ Returns a list of tuples containing all the valid words in given a
    given length on the board"""
    words_list = minimize_dict(n, words)  # filters words that are too long
    output = []
    for y in range(len(board)):
        for x in range(len(board[0])):
            output += finder_helper(n, "", [], (x, y), board, words_list)
    return output


def finder_helper(n: int, path: str, coordinates: List[Tuple[int, int]],
                  cur_step: Tuple[int, int], board: List[List[str]],
                  words_list: List[str]):
    """ An internal function that helps 'find_length_n_words' to check
    all possible words that start in a specific coordinate"""
    x, y = cur_step
    if x > MAX_ROW or y > MAX_COL or x < 0 or y < 0:  # out of bounds
        return []
    if cur_step in coordinates:  # duplicated coordinate
        return []
    path += board[x][y]
    if not is_path_possible(path, words_list):  # no matching words in list
        return []
    coordinates = coordinates + [cur_step]

    if n == len(path):  # base case
        if path in words_list:
            return [(path, coordinates)]
        else:
            return []
    output = \
        proceed_to_neighbors(board, coordinates, n, path, words_list, x, y)
    return output


def proceed_to_neighbors(board, coordinates, n, path, words_list, x, y):
    """ An internal function that calls finder_helper on all of a given
    coordinate's surroundings"""
    output = []
    neighbors = [(x + 1, y), (x + 1, y + 1), (x, y + 1), (x + 1, y - 1),
                 (x, y - 1), (x - 1, y - 1), (x - 1, y), (x - 1, y + 1)]
    for neighbor in neighbors:
        output += \
            finder_helper(n, path, coordinates, neighbor, board, words_list)
    return output


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


def main():
    board = [
        ['A', 'E', 'A', 'N', 'E', 'G'],
        ['A', 'H', 'S', 'P', 'C', 'O'],
        ['A', 'S', 'P', 'F', 'F', 'K'],
        ['O', 'B', 'J', 'O', 'A', 'B'],
        ['I', 'O', 'T', 'M', 'U', 'C'],
        ['R', 'Y', 'V', 'D', 'E', 'L'],
        ['L', 'R', 'E', 'I', 'X', 'D'],
        ['E', 'I', 'U', 'N', 'E', 'S'],
        ['W', 'N', 'G', 'E', 'E', 'H'],
        ['L', 'N', 'H', 'N', 'R', 'Z'],
        ['T', 'S', 'T', 'I', 'Y', 'D'],
        ['O', 'W', 'T', 'O', 'A', 'T'],
        ['E', 'R', 'T', 'T', 'Y', 'L'],
        ['T', 'O', 'E', 'S', 'S', 'I'],
        ['T', 'E', 'R', 'W', 'H', 'V'],
        ['N', 'U', 'I', 'H', 'M', 'QU']
    ]

    dic = load_words_dict("boggle_dict.txt")
    print(is_valid_path(board, [(1, 2), (2, 3), (1, 3)], dic))


if __name__ == '__main__':
    pass