from typing import List
from anime import Anime
from openpyxl import Workbook

first_row = ["Название", "Рейтинг", "Жанры", "Описание", "Ссылка", "Кол-во серий", "Статус"]
directory = "C:\\Users\\top_p\\Desktop\\"


class DataContainer(object):

    def __init__(self, anime_list: List[Anime]):
        self.__anime_list = anime_list

    def data_to_xlsx(self, file_name):
        wb = Workbook()
        ws = wb.active
        ws.column_dimensions['A'].width = 42.5
        ws.column_dimensions['B'].width = 10
        ws.column_dimensions['C'].width = 85
        ws.column_dimensions['D'].width = 10
        ws.column_dimensions['F'].width = 15
        ws.column_dimensions['G'].width = 10.5
        ws.append(first_row)
        print("запись в файл..")
        for _, anime in enumerate(self.__anime_list):
            ws.append([anime.title, anime.score, str(anime.genres),
                       anime.description, anime.url, anime.episodes, anime.status])

        wb.save(directory + file_name + ".xlsx")

    def __str__(self):
        _str = ""
        for _, anime in enumerate(self.__anime_list):
            _str += str(anime) + "\n"
        return _str
