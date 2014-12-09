import sys
from collections import defaultdict, Counter

line_count = 0
word_count = 0
word_freq = Counter()

def cleanup_word(word):
    word = word.replace(".", "")
    word = word.replace(",", "")
    word = word.replace("!", "")
    word = word.replace("?", "")
    return word.lower()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Please specify input"
        sys.exit(0)

    file_to_process = sys.argv[1]
    with open(file_to_process) as input_doc:
        for line in input_doc.readlines():
            line_count += 1
            words = line.split()
            word_count += len(words)
            word_freq.update(map(cleanup_word, words))

    print "Total Lines: %d" % line_count
    print "Total Words: %d" % word_count
    print "Total Unique Words: %d" % len(word_freq)
    print word_freq