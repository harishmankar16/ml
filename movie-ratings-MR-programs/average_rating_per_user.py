# from mrjob.job import MRJob

# class MRAverageRatingPerUser(MRJob):
    
#     def mapper(self,_,line):
#         user_id,movie_id,rating = line.split(',')
#         yield user_id , float(rating)
    
#     def reducer(self,user_id,ratings):
#         total_rating = 0
#         num_rating = 0
        
#         for rating in ratings:
#             total_rating += rating
#             num_rating += 1
            
#         average_rating = total_rating / num_rating
#         yield user_id , average_rating

# if __name__ == '__main__':
#     MRAverageRatingPerUser.run()





from mrjob.job import MRJob

class MRQuestion1(MRJob):
    def mapper(self,_,line):
        user_id,movie_id,rating = line.split(',')
        yield user_id,float(rating)

    def reducer(self,user_id,ratings):
        total_num_rating = 0
        user_rating = 0
        
        for rating in ratings:
            user_rating += rating
            total_num_rating += 1

        average_rating = user_rating / total_num_rating
        yield user_id,average_rating

if __name__ == '__main__':
    MRQuestion1.run()
















