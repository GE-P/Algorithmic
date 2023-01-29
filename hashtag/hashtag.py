import json
import sys


# Use << python .\hashtag.py "hash_list" >> to execute.
def function_01():

    with open(sys.argv[1], "r") as file_data:
        json_obj = json.load(file_data)

    dico_hash, sorted_list = {}, []
    json_file = json.loads(json.dumps(json_obj))

    for data in json_file["tweets"]:
        if len(data["hashtags"]) > 1:
            for hashtag in data["hashtags"]:
                if hashtag not in dico_hash:
                    dico_hash[hashtag] = 1
                else:
                    dico_hash[hashtag] += 1
        elif data["hashtags"][0] not in dico_hash:
            dico_hash[data["hashtags"][0]] = 1
        else:
            dico_hash[data["hashtags"][0]] += 1

    sorted_hash = sorted(dico_hash.items(), key=lambda item: item[1], reverse=True)

    for count in sorted_hash:
        if count[1] > ((len(sorted_hash)/100)*30):
            sorted_list.append(count[0])

    print(sorted_list)
    return sorted_list


function_01()

