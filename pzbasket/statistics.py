from pzbasket.base import BaseData
import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate


class Statistics(BaseData):
    def __init__(self):
        super().__init__("https://rozgrywki.pzkosz.pl/liga/4/statystyki.html")
            

    def data(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, "html.parser")
        table = soup.find("table", class_="stattype splitTable").find('tbody').find_all('tr')  # type: ignore

        for row in table:
            dic = {}

            row_data = row.find_all('td')
            dic['place'] = row_data[0].text
            dic['player'] = row_data[1].text
            dic['team'] = row_data[2].text
            dic['matches'] = row_data[3].text
            dic['points_sum'] = row_data[4].text
            dic['points_avg'] = row_data[5].text
            self.table_data.append(dic)

    def show_data(self):

        self.headers = self.table_data[0].keys()
        print(tabulate(self.table_data, headers="keys"))
