def load_words_dict(file_path):
    with open(file_path) as f:
        content = f.read().splitlines()
        word_dict = {x: True for x in content}
    return word_dict

print(load_words_dict("boggle_dict.txt"))

def is_valid_path(board, path, words):
    pass


def find_length_n_words(n, board, words):
    pass