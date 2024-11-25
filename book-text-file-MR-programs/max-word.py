from mrjob.job import MRJob
from mrjob.step import MRStep
import re

class MRMaxWord(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper,reducer=self.reducer) , 
            MRStep(reducer=self.reducer_find_max)
        ]
    
    def mapper(self,_,line):
        words = re.findall(r'\b\w+\b',line.lower())
        for word in words:
            yield word,1
    
    def reducer(self,word,count):
        total_count = sum(count)
        yield None, (total_count, word)
    
    def reducer_find_max(self, _, word_count_pairs):
        max_word = None
        max_count = 0
        
        for count , word in word_count_pairs :
            if count > max_count:
                max_count = count
                max_word = word
        
        yield max_word, max_count
    
if __name__ == '__main__':
     MRMaxWord.run()