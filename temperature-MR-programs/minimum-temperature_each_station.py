from mrjob.job import MRJob

class MRMinTemperature(MRJob):
    def mapper(self, _, line):
       
        # data = line.split(',')
        
        # if data[0]=='station_id':
        #     return
        # station_id = data[0]
        # temperature = float(data[2])
        station_id , date , temperature = line.split(',')
       
        yield station_id, temperature
       
    def reducer(self, station_id, temperatures):
        min_temperature = min(temperatures) # use max() for maximun tempature
        yield station_id, min_temperature


if __name__ == '__main__':
    MRMinTemperature.run()