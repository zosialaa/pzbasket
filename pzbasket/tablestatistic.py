from pzbasket.base import BaseData
import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate


class TableStatistics(BaseData):

    def __init__(self, group_name):
        super().__init__("https://rozgrywki.pzkosz.pl/liga/4/tabela.html")
        if group_name not in ['a0', 'b1', 'c2', 'd3']:
            raise Exception("Group name should be a0, b1, c2 or d3.")
        self.group_name = group_name

    def data(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, "html.parser")
        group = soup.find("div", id=f"runda-zasadnicza--gr--{self.group_name}")
        table = group.find("table", class_="stattype splitTable tabela").find('tbody').find_all('tr')  # type: ignore

        for row in table:
            dic = {}

            row_data = row.find_all('td')
            dic['place'] = row_data[0].text
            dic['team'] = row_data[1].text
            dic['matches'] = row_data[2].text
            dic['points'] = row_data[3].text
            dic['win-lose'] = row_data[4].text
            dic['home'] = row_data[5].text
            dic['away'] = row_data[6].text
            dic['p_scored-p_lost'] = row_data[7].text
            dic['difference'] = row_data[8].text
            dic['win/matches'] = row_data[9].text
            self.table_data.append(dic)

    def show_data(self):
        self.headers = self.table_data[0].keys()
        print(tabulate(self.table_data, headers="keys", tablefmt="grid"))


