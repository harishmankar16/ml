import mrjob.job from MRJob

class MRMaxTemperature(MRJob):
    def mapper(self,_,line):
        data = data.split(",")
        if data