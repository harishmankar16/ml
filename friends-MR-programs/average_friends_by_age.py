# from mrjob.job import MRJob

# class MRAverageFriendsByAge(MRJob):

#     def mapper(self, _, line):
        
#             user_id,name, age, num_friends = line.split(',')
            
#             yield age, int(num_friends)
      

#     def reducer(self, age, num_friends):
#         total_friends = 0
#         total_users = 0
       
#         for friends in num_friends:
#             total_friends += friends
#             total_users += 1
        
       
#         if total_users > 0:
#             average_friends = total_friends / total_users
#             yield age, average_friends

# if __name__ == '__main__':
#     MRAverageFriendsByAge.run()





from mrjob.job import MRJob

class MRAverageFriendsByAge(MRJob):
    def mapper(self,_,line):
        user_id , name , age , num_friends = line.split(',')
        yield age , int(num_friends)
    
    def reducer(self,age,num_friends):
        total_friends = 0
        total_number = 0
        
        for friends in num_friends:
            total_friends += friends
            total_number += 1
        
        if total_number > 0 :    
            average = total_friends / total_number
            yield age,average

if __name__ == "__main__":
    MRAverageFriendsByAge.run()
             
        














