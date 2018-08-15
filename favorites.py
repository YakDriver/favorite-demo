
favs = {
    "color":"red",
    "flavor":"lemon"
}

def get_fav(key):
    return favs[key]

def display_fav(key):
    print("Favorite for",key,"is",get_fav(key))

def add_fav(key, value):
    favs[key] = value

display_fav("color")
add_fav("car", "Audi S4")