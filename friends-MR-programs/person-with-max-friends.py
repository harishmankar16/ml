# from mrjob.job import MRJob

# class MRMaxFriends(MRJob):

#     def mapper(self, _, line):
        
#             user_id, name, age, num_friends = line.split(',')
#             num_friends = int(num_friends)
           
#             yield None, (num_friends, name, user_id)  
       

#     def reducer(self, _, values):
        
#         max_friends = -1
#         max_user = None
#         max_user_id = None

        
#         for num_friends, name, user_id in values:
#             if num_friends > max_friends:
#                 max_friends = num_friends
#                 max_user = name
#                 max_user_id = user_id

      
#         yield max_user, (max_user_id, max_friends)

# if __name__ == '__main__':
#     MRMaxFriends.run()



from mrjob.job import MRJob

class MRQUESTION2(MRJob):
    def mapper(self,_,line):
        user_id,name,age,num_friends = line.split(",")
        yield None ,(user_id,name,int(num_friends))
    
    def reducer(self,_,values):
        max_friends = -1
        max_user=None
        
        for user_id,name,num_friends in values:
            if num_friends > max_friends:
                max_friends = num_friends
                max_user = name
        
        yield max_user,max_friends
if __name__ == "__main__":
    MRQUESTION2.run()
