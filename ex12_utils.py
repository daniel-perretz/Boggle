MAX_ROW = 3
MAX_COL = 3
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
    for i in range(len(path)-1):
        x1,y1 = path[i]
        x2,y2 = path[i+1]
        if abs(x1-x2) > 1 or abs(y1-y2) > 1:
            return None
            break
    dup_list = list(set(path)) # check for double coordinate
    if len(dup_list) < len(path):
        return None
    word = ''
    for coor in path:
        x, y = coor
        word = word + board[x][y]
    if word in words:
        return word
    return None


def find_length_n_words(n, board, words):
    pass

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
    main()