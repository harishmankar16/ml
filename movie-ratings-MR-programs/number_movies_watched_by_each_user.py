# from mrjob.job import MRJob

# class MRNumbersOfMoviesWatchedByEachUser(MRJob):
#     def mapper(self,_,line):
#         user_id,movie_id,rating = line.split(',')
#         yield user_id,1
    
#     def reducer(self,user_id,counts):
#         total = sum(counts)
#         yield user_id,total

# if __name__ == '__main__':
#     MRNumbersOfMoviesWatchedByEachUser.run()



from mrjob.job import MRJob
class MRNumbersOfMoviesWatchedByEachUser(MRJob):
    def mapper(self,_,line):
        user_id,movie_id,rating = line.split(',')
        yield user_id,1
        
    def reducer(self,user_id,counts):
        total=sum(counts)
        yield user_id,total
    
if __name__ == '__main__':
    MRNumbersOfMoviesWatchedByEachUser.run()