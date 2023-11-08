from pzbasket.base import BaseData
import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate



class Teamstatistics(BaseData):
    def __init__(self, group_name):
        super().__init__("https://rozgrywki.pzkosz.pl/liga/4/statystyki/druzynowe.html")
        if group_name not in ['2657', '2658', '2659', '2660']:
            raise Exception("Group name should be 2657, 2658, 2659 or 2660.")
        self.group_name = group_name
       

    def data(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, "html.parser")
        group = soup.find("div", id=f"grupa{self.group_name}")
        table = group.find("table", class_="statystyki druzynowe stattype splitTable").find('tbody').find_all('tr')

        for row in table:
            dic = {}

            row_data = row.find_all('td')
            dic['team'] = row_data[0].text
            dic['m'] = row_data[1].text
            dic['points'] = row_data[2].text
            dic['2/c'] = row_data[3].text
            dic['2/w'] = row_data[4].text
            dic['[2/%]'] = row_data[5].text
            dic['3/c'] = row_data[6].text
            dic['3/w'] = row_data[7].text
            dic['3/%'] = row_data[8].text
            dic['game/c'] = row_data[9].text
            dic['game/w'] = row_data[10].text
            dic['[game/%]'] = row_data[11].text
            dic['1/c'] = row_data[12].text
            dic['1/w'] = row_data[13].text
            dic['1/%'] = row_data[14].text
            dic['zb/a'] = row_data[15].text
            dic['zb/0'] = row_data[16].text
            dic['zb/s'] = row_data[17].text
            dic['a'] = row_data[18].text
            dic['f'] = row_data[19].text
            dic['[fw]'] = row_data[20].text
            dic['s'] = row_data[21].text
            dic['p'] = row_data[22].text
            dic['b'] = row_data[23].text
            dic['bo'] = row_data[24].text
            dic['eval'] = row_data[25].text

            self.table_data.append(dic)

    def show_data(self):
        self.headers = self.table_data[0].keys()
        print(tabulate(self.table_data, headers="keys", tablefmt="grid"))
