from mrjob.job import MRJob
from mrjob.step import MRStep
import re

class MRSortedWordCount(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer_count_words),
            MRStep(reducer=self.reducer_sort_counts)
        ]

    def mapper(self, _, line):
        # Split the line into words and yield each word with a count of 1
        words = re.findall(r'\b\w+\b', line.lower())
        for word in words:
            yield word, 1

    def reducer_count_words(self, word, counts):
        # Sum up all counts for each word
        total_count = sum(counts)
        yield None, (total_count, word)

    def reducer_sort_counts(self, _, word_count_pairs):
        # Sort by count in descending order
        sorted_word_counts = sorted(word_count_pairs, reverse=True)
        for count, word in sorted_word_counts:
            yield word, count

if __name__ == '__main__':
    MRSortedWordCount.run()
