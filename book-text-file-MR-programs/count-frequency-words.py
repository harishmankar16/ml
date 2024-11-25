# from mrjob.job import MRJob
# import re

# class MRWordCount(MRJob):
    
#     def mapper(self,_,line):
#         words = re.findall(r'\b\w+\b',line.lower())
#         for word in words:
#             yield word,1
    
#     def reducer(self,word,count):
#         yield word,sum(count)
    
# if __name__ == '__main__':
#      MRWordCount.run()


from mrjob.job import MRJob
import re

class Question2(MRJob):
    def mapper(self,_,line):
        words = re.findall(r'\b\w+\b',line.lower())
        for word in words:
            yield word,1
    
    def reducer(self,word,count):
        yield word,sum(count)

if __name__ == "__main__":
    Question2.run()