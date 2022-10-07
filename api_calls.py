import requests
from typing import List
from anime import Anime

__base_url = "https://shikimori.one"


__request_headers = {
    "User-Agent": "bebra app",
    "Authentication": "Bearer Wlykj_DkOmt6wEmnJ13SRXBioFoeJ26NNfhQ_MmhaLU",
}


def get_anime_list(skip_genres: List[str], **kwargs) -> List[Anime]:
    url = __base_url + "/api/animes"
    params = {"order": kwargs.get("order"),
              "kind": kwargs.get("kind"),
              "status": kwargs.get("status"),
              "score": kwargs.get("min_score"),
              "limit": kwargs.get("limit")
              }
    if kwargs.get("genres"):
        params["genre"] = __get_genres_ids(kwargs.get("genres"))
    response = requests.get(url=url, params=params, headers=__request_headers)
    print(response.status_code)
    anime_ids = [str(anime["id"]) for _, anime in enumerate(response.json())]
    print(anime_ids)
    return __get_anime_data(anime_ids, url=url, skip_genres=skip_genres)


def __get_anime_data(animes: List[str], url: str, skip_genres: List[str]) -> List[Anime]:
    anime_list: List[Anime] = []
    for _, anime_id in enumerate(animes):
        anime_data = requests.get(url=url + "/" + anime_id, headers=__request_headers).json()
        genres = [genre["russian"].lower() for _, genre in enumerate(anime_data["genres"])]
        if skip_genres:
            skip_anime = False
            for _, genre in enumerate(skip_genres):
                if genre in genres:
                    skip_anime = True
                    break

            if skip_anime:
                continue

        anime_list.append(
            Anime(
                title=anime_data["russian"], score=anime_data["score"],
                genres=genres,
                description=anime_data["description"],
                url=__base_url + anime_data["url"], episodes=anime_data["episodes"], status=anime_data["status"]
            )
        )

    return anime_list


def __get_genres_ids(genres_list: List[str]) -> List[int]:
    url = __base_url + "/api/genres"
    genres_response = requests.get(url=url, headers=__request_headers).json()
    print(genres_response)
    genres = sorted(genres_response, key=lambda genre: genre["id"], reverse=False)
    print(genres)
    genre_ids = []
    for _, genre_name in enumerate(genres_list):
        for _, genre in enumerate(genres):
            if genre_name == genre["russian"].lower():
                genre_ids.append(genre["id"])
                break

    return genre_ids

# __get_genres_ids(["безумие"])
