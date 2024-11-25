from mrjob.job import MRJob
from mrjob.step import MRStep

class MRFriendsByAgeSorted(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer_age_total_friends),
            MRStep(reducer=self.reducer_sort_by_age)
        ]
    
    def mapper(self, _, line):
        user_id,name,age,num_friends = line.split(',')
        yield age,int(num_friends)
    
    def reducer_age_total_friends(self, age, num_friends):
        total_friends = sum(num_friends)
        yield int(age), total_friends

    def reducer_sort_by_age(self, age, total_friends):
        # Sort by age in ascending order
        yield age, list(total_friends)[0]

if __name__ == '__main__':
    MRFriendsByAgeSorted.run()
