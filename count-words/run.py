import csv
import re
import sys
from collections import Counter
from os.path import join

target_folder, document_text_path = sys.argv[1:]
target_path = join(target_folder, 'word_counts.csv')
document_text = open(document_text_path, 'rt').read()
words = re.sub(r'[^a-zA-Z]+', ' ', document_text).lower().split()
count_by_word = Counter(words)

csv_writer = csv.writer(open(target_path, 'wt'))
csv_writer.writerow(['word', 'count'])
for word, count in sorted(count_by_word.items(), key=lambda x: -x[1]):
    csv_writer.writerow([word, count])

print('word_count = %s' % len(words))
print('word_count_table_path = %s' % target_path)
