MAX_ROW = 3
MAX_COL = 3
def load_words_dict(file_path):
    with open(file_path) as f:
        content = f.read().splitlines()
        word_dict = {x: True for x in content}
    return word_dict

print(load_words_dict("boggle_dict.txt"))


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

    return "Word_Test"

print(is_valid_path([],[(1, 2) ,(2, 3),(1, 3)],"test"))


def find_length_n_words(n, board, words):
    pass