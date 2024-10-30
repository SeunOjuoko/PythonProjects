capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

#travel_log = {
#    "France": ["Paris", "Lille", "Dijon"],
#    "Germany": ["Berlin", "Bamberg"]
#}

#city = travel_log["France"][0]
#print(city)

nested_list = ["A","B",["C","D"]]
print(nested_list[2][1])

travel_log = {
    "France": {
        "visited": 8,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    "Germany": {
    "visited": 13,
    "cities": ["Berlin", "Bamberg"]
    }
}

print(travel_log["Germany"]["cities"][1])