from mrjob.job import MRJob 

class MRNumberOfFriendsPerUser(MRJob):
    def mapper(self,_,line):
        user_id,friend_id = line.split(',')
        yield user_id,1
    
    def reducer(self, user_id, counts):
         
        total_friends = sum(counts)
        
        yield user_id, total_friends
       

if __name__ == '__main__':
    MRNumberOfFriendsPerUser.run()