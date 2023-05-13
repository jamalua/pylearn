fav_colour: str = input("Enter the favourite colour: ").lower()

match fav_colour:
    case "black":
        print("colour is black")
    case "red":
        print("colour is red")
    case _:
        print("colour is undefined")
