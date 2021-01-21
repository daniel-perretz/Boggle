from typing import List, Tuple, Dict

MAX_ROW = 3
MAX_COL = 3
MAX_DIFFERENCE = 1


def load_words_dict(file_path):
    """Filters all words from a file whose path was provided and returns a
    dictionary whose keys are the words, and values the bool 'True'"""
    with open(file_path) as f:
        content = f.read().splitlines()
        word_dict = {x: True for x in content}
    return word_dict


def is_valid_path(board, path, words):
    """Checks if a certain coordinates path is valid - in board, adds up to
    a word in dictionary, has a certain coordinate twice"""
    for coor in path:
        x, y = coor
        if x > MAX_ROW or y > MAX_COL or x < 0 or y < 0 \
                or x * y > MAX_ROW * MAX_COL:
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
        word += board[x][y]
    if word in words:
        return word
    return None


def find_length_n_words(n, board, words):
    """ Returns a list of tuples containing all the valid words in given a
    given length on the board"""
    if n > MAX_ROW * MAX_COL * 2 or n < 1:  # each tile is up to 2 letters
        return []
    words_dict = minimize_dict(n, words)  # filters words that are too long
    output = []
    if words_dict:
        for y in range(len(board)):
            for x in range(len(board[0])):
                output += finder_helper(n, "", [], (x, y), board, words_dict)
    return output


def finder_helper(n: int, path: str, coordinates: List[Tuple[int, int]],
                  cur_step: Tuple[int, int], board: List[List[str]],
                  words_dict: Dict[str, bool]):
    """ An internal function that helps 'find_length_n_words' to check
    all possible words that start in a specific coordinate"""
    x, y = cur_step
    if x > MAX_ROW or y > MAX_COL or x < 0 or y < 0:  # out of bounds
        return []
    if cur_step in coordinates:  # duplicated coordinate
        return []
    path += board[x][y]
    coordinates = coordinates + [cur_step]

    if n == len(path):  # base case
        if path in words_dict:
            return [(path, coordinates)]
        else:
            return []
    output = \
        proceed_to_neighbors(board, coordinates, n, path, words_dict, x, y)
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


def minimize_dict(n: int, words: Dict[str, bool]) -> Dict[str, bool]:
    """ Returns a minimized dictionary so that it only contains words up to a given length"""
    output = {}
    for word in words:
        if len(word) <= n:
            output[word] = True
    return output

if __name__ == '__main__':
    pass
