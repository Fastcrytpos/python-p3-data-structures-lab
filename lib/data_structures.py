spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [key["name"] for key in spicy_foods]
    #returns a list (key["name"]) of 
    pass


def get_spiciest_foods(spicy_foods):

    happy=[key for key in spicy_foods if key["heat_level"] >5]
    #iterates the list the key being iteration of the objects. /
    #Once it does that it filters according to the condition in 
    #which the iteration[the key]==value is greater than 5
    
    return happy
    pass

def print_spicy_foods(spicy_foods):
    #[key.update({"heat_level":key["heat_level"]*"🌶" })for key in spicy_foods]
    for key in spicy_foods:
        heatemoji=key["heat_level"]*"🌶"
        print(f"{key['name']} ({key['cuisine']}) | Heat Level: {heatemoji}")
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return next(key for key in spicy_foods if key["cuisine"]==cuisine)
    pass

def print_spiciest_foods(spicy_foods):
            
            for key in spicy_foods:
                 if key["heat_level"] > 5:
                    heatemoji=key["heat_level"]*"🌶"
                    print(f"{key['name']} ({key['cuisine']}) | Heat Level: {heatemoji}")


def get_average_heat_level(spicy_foods):
    lsty=[]
    for key in spicy_foods:
        lsty.append(key["heat_level"])

    return sum(lsty)/len(lsty)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass
