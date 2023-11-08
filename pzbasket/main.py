#from apiclient import ApiClient, Statistic, Teamstatistic

'''
api_client = ApiClient('d3')

data = api_client.data()

api_client.show_data()


api_client1 = Statistic()

data1 = api_client1.data()

api_client1.show_data()

api_client2 = Teamstatistic("2657")
data2 = api_client2.data()

api_client2.show_data()
'''

from tablestatistic import TableStatistics

if __name__ == '__main__':
    

    api_client = TableStatistics('d3')
    api_client.data()
    api_client.show_data()
