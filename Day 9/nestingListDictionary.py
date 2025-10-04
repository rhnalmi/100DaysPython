capitals = {
    "France" : "Paris",
    "Germany": "Berlin",
    "Indonesia": "Jakarta"
}

#Nested list in dictionary

travel_log = {
    "Indonesia": ["Jakarta", "Pekanbaru", "Batam", "Semarang"],
    "France" : ["Lille", "Paris"]
}

#print Batam
print(travel_log["Indonesia"][2])

#print C
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][0])

#print Pekanbaru
travel = {
    "Indonesia":{
        "cities_visited" : ["Jakarta", "Semarang", "Bandung", "Pekanbaru", "Batam"],
        "total_visit" : 12
    },
    "Malaysia": {
        "cities_visited": ["Kuala Lumpur", "Genting", "Sarawak"],
        "total_visit": 3
    },

}

print(travel["Indonesia"]["cities_visited"][3])


