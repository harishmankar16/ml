from mrjob.job import MRJob

class MRNumberOfRatingsPerRatingValue(MRJob):
    
    def mapper(self,_,line):
        user_id,movie_id,rating = line.split(',')
        yield rating ,1
    
    def reducer(self,rating,counts):
        
        total_count = sum(counts)
        yield rating,total_count

if __name__ == '__main__':
    MRNumberOfRatingsPerRatingValue.run()