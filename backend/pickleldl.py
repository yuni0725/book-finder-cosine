import pickle
from utils import title_to_vector

with open("data2.pkl", "rb") as file:
    loaded_data = pickle.load(file)

print(loaded_data)

# new_data = []

# for d in loaded_data:
#     d["벡터"] = title_to_vector(d["도서명"])
#     new_data.append(d)
#     print(d)

# with open("data2.pkl", "wb") as file:
#     pickle.dump(new_data, file)
