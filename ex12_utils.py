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



def find_length_n_words(n, board, words):
    pass