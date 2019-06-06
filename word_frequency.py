STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
sentence_list = []
word_list = []
count_data = {}
import re


#adds individual words to word_list with no punctuation or caps
def sterilizeText(doc):
    for i in doc:
        sentence_list = i.split(" ")
        for x in sentence_list:
                if (x.lower() not in STOP_WORDS) and (x != ''):
                    z = re.sub(r'[^A-Za-z]', '', x)
                    word_list.append(z.lower())

#get_count provides the rules for sorting list_in_order
def get_count(word):
    return count_data[word]

def print_word_freq(file):
    wholeDoc = file.readlines()
    sterilizeText(wholeDoc)
    #this block counts the frequency of each word and stores it in dict count_data
    for i in word_list:
        if count_data.get(i) == None:
            count_data[i] = 1
        else:
            count_data[i] = count_data[i] + 1
    #words are put in order in a list (list_in_order) by their frequency.
    list_in_order = []
    for i in count_data:
        list_in_order.append(i)
    list_in_order.sort(key = get_count, reverse = True)
    list_in_order.remove('')

    #prints out the list of words, in order, with each word's frequency next to it
    for i in list_in_order:
        print(i, (" ")*(9 - len(i)), "  |    ", count_data[i], ("*" * count_data[i]))
        if list_in_order.index(i) == 9:
            break


    

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()
    #checks if file exists, exits program if it does not
    try:
        f = open(Path(args.file))
        f.close()
    except FileNotFoundError:
        print("File does not exist!")
        exit()
    file = open(Path(args.file))
    print_word_freq(file)
    file.close()

