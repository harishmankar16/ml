from mrjob.job import MRJob

class MRTotalSpentByCustomer(MRJob):
    
    def mapper(self, _, line):
        # # Split the line by commas
        # data = line.split(',')
        
        # # Skip the header
        # if data[0] == 'customer_id':
        #     return
        
        # # Extract customer_id and amount
        # customer_id = data[0]
        # amount = float(data[2])
        
        # # Emit customer_id as the key and amount as the value
        # yield customer_id, amount
        customer_id,order_id,amount = line.split(',')
        yield customer_id,float(amount)
    
    def reducer(self, customer_id, amounts):
        # Sum all amounts for each customer_id
        total_spent = sum(amounts)
        
        # Emit customer_id and the total amount spent
        yield customer_id, total_spent

if __name__ == '__main__':
    MRTotalSpentByCustomer.run()
