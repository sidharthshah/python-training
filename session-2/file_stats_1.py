import sys

line_count = 0
word_count = 0
word_freq = {}

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
            for word in words:
                word = cleanup_word(word)
                if not word_freq.has_key(word):
                    word_freq[word] = 0
                word_freq[word] += 1

    print "Total Lines: %d" % line_count
    print "Total Words: %d" % word_count
    print "Total Unique Words: %d" % len(word_freq)
    print word_freq