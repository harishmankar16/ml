from mrjob.job import MRJob

class MRAverageRatingPerMovie(MRJob):
    def mapper(self,_,line):
        user_id,movie_id,rating = line.split(',')
        yield movie_id,float(rating)
    
    def reducer(self,movie_id,ratings):
        total_rating = 0
        total_num = 0
        
        for rating in ratings:
            total_rating += rating
            total_num += 1
        
        average_rating = total_rating / total_num
        yield movie_id,average_rating

if __name__ == "__main__":
    MRAverageRatingPerMovie.run()