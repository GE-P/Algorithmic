import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-e', dest="examine", action='append', nargs=1)
parser.add_argument(dest="file", help="file directory")
args = parser.parse_args()

search_word = args.examine
length_word = len(search_word[0][0])

search_word2 = search_word[1][0]
length_word2 = len(search_word2)


# Use << python .\word_position.py -e 'word1' -e 'word2' "file.txt" >> to execute.
def pattern_particulier():

    pos_char = 0
    pos_char_glob = 0
    list_pos = []
    with open(args.file, 'r') as file:
        for line in file:
            for character in line:
                if (line[pos_char - length_word:pos_char]) == search_word[0][0]:
                    string1 = search_word[0][0] + " : " + str(pos_char_glob + pos_char - length_word)
                    list_pos.append(string1)
                    # print(search_word[0][0] + " : " + str(pos_char_glob + pos_char - length_word))
                elif (line[pos_char - length_word2:pos_char]) == search_word2:
                    string2 = search_word2 + " : " + str(pos_char_glob + pos_char - length_word2)
                    list_pos.append(string2)
                    # print(search_word2 + " : " + str(pos_char_glob + pos_char - length_word2))
                pos_char += 1
            pos_char_glob += pos_char
            pos_char = 0
    print(list_pos)
    return list_pos


pattern_particulier()
