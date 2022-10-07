from api_calls import get_anime_list
from anime_to_xlsx import DataContainer

if __name__ == '__main__':
    while True:
        command = input("выбрать действие(search, exit):")
        if command.lower() == "exit":
            break
        anime_list = get_anime_list(
            order=input("сортировка(ranked, name):").lower(), kind=input("тип(tv, movie):").lower(),
            status=input("статус(released, ongoing):").lower(), genres=input("жанры:").lower().split(" ") or None,
            min_score=int(input("мин.оценка(1-10):")), limit=int(input("лимит(1-50):")),
            skip_genres=input("исключить жанры:").lower().split(" ") or None
        )
        data_container = DataContainer(anime_list)
        file_name = input("имя файла:")
        data_container.data_to_xlsx(file_name)
        print("finished..")
