from time import time
import load_data
import compare_soundex
import compare_levenshtein
import compare_damerau_levenshtein
import compare_jaro_winkler
import compare_jaccard_similarity
import compare_double_metaphone
import compare_metaphone


def main():
    small_data = "/home/bruce/Documents/tools/data-generator/GECO-Ethiopia/data-01000-00500-abcd.csv"

    df = load_data.full(small_data)

    # df[i][2], df[j][2]

    for i in range(1, 30):
        for j in range(i+1, 31):
            break


if __name__ == '__main__':
    s = time()
    main()
    e = time()
    print(e - s)
