# here is answer of another question
d1 = {"1": "ankur",
        "2": "rishabh",
        "3": "rakshit"}

d2 = {"1": 50,
        "2": 60,
        "3": 70}

def print_max(d1,d2):
    for i in d2:
        if i == max(d2):
            return {i: d2[i]}
print(print_max(d1,d2))