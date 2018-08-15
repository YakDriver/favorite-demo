
favs = {
    "color":"red",
    "flavor":"lemon"
}

def get_fav(key):
    return favs[key]

def display_fav(key):
    print("Favorite for",key,"is",get_fav(key))

display_fav("color")
