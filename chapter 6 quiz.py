my_dict = {
    "name": "Troy Aikman",
    "position": "QB",
    "team" : "Dallas Cowboys",
    "age": 54,
    "weight": 220.,
    "superbowls":["XXVII", "XXVIII", "XXX"],
    "awards":{
            "super_bowl_mvp":"XXVII",
            "probowl":[1991, 1992, 1993, 1994, 1995, 1996],
            "man_of_the_year": 1997
    }
}

for value, key in my_dict.items():
    if value == 54:
        print("Old", end = " ")
    if value == "age":
        print("54", end = " ")