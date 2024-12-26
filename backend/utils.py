def read_csv():
    import csv

    data = []

    f = open("전주시립도서관꽃심.csv", "r", encoding="utf-8")
    rdr = csv.reader(f)

    for line in rdr:
        library_name = line[0]
        author_name = line[1]
        book_name = line[2]
        book_place = line[3]

        print(book_name)

        data.append(
            {
                "도서관": library_name,
                "작가": author_name,
                "도서명": book_name,
                "도서위치": book_place,
            }
        )
    f.close()

    return data


def get_titles(csv_data):
    title_list = []
    for data in csv_data:
        title_list.append(data["도서명"])

    return title_list


def making_text_clean(text):
    import re

    clean_text = re.sub(r"[^가-힣\s]", "", text)
    return clean_text


def title_to_vector(title):
    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer("jhgan/ko-sroberta-multitask")
    print("vector")
    return model.encode(making_text_clean(title))


def calculate_cosine_similarity(vector1, vector2):
    import numpy as np

    v1 = np.array(vector1)
    v2 = np.array(vector2)

    dot_product = np.dot(v1, v2)

    norm1 = np.linalg.norm(v1)
    norm2 = np.linalg.norm(v2)

    if norm1 == 0 or norm2 == 0:
        return 0.0
    cosine_similarity = dot_product / (norm1 * norm2)

    return cosine_similarity


def match_data(query):
    import pickle

    data_with_value = []
    query_vector = title_to_vector(query)

    with open("data2.pkl", "rb") as file:
        data = pickle.load(file)

    for d in data:
        score = calculate_cosine_similarity(query_vector, d["벡터"])

        d["스코어"] = float(score)

        del d["벡터"]

        data_with_value.append(d)

    import json

    json_val = json.dumps(sort_data(data_with_value))

    return json_val


def sort_data(data: list):
    sorted_data = sorted(data, key=lambda x: x["스코어"], reverse=True)
    return sorted_data
