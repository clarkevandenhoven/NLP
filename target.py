import nltk
import itertools
def target_solver(matrix):
    """ Input: an odd nxn matrix with char
        Output: all possible words formed by that matrix """
 
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    letter_list = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            letter_list.append(matrix[i][j])
    permutations = list(itertools.permutations(letter_list))
    short_perm = []
    for i in range(len(permutations)):
        for j in range(1, len(permutations[i])):
            string = ''.join(permutations[i][:j])
            short_perm.append(string)
    short_perm = set(short_perm)
    solutions = []
    for w in short_perm:
        if matrix[int((len(matrix) - 1) / 2)][int((len(matrix) - 1) / 2)] in w and w in english_vocab:
            solutions.append(w)
    return(solutions)


print(target_solver([['e', 'g', 'i'],
               ['v', 'r', 'v'],
               ['o', 'n', 'l']]))
