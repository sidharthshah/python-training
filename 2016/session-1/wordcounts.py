import sys

if len(sys.argv) < 2:
    print "Please specify input files"
    sys.exit(-1)

def cleanup(contents):
    contents = contents.replace(".", " ")
    contents = contents.replace(",", " ")
    contents = contents.lower()
    return contents

def count_words(contents):
    counts = {}
    for token in contents.split():
        if token.strip() != "":
            if token not in counts:
                counts[token] = 0
            counts[token] += 1
    return counts

for file_to_process in sys.argv[1:]:
    print "Processing:%s" % file_to_process
    contents = open(file_to_process).read()
    word_counts = count_words(cleanup(contents))
    print "Total words in %s is %d" % (file_to_process, sum(word_counts.values()))

