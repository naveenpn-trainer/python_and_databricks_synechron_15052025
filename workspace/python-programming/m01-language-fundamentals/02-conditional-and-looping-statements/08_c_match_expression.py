shopping_cart = ["IPhone","Case Cover"]

match shopping_cart:
    case []:
        print("Nothing in the cart")
    case [action]:
        print("Added one item")
    case [action, *rest]:
        print("Added one item also more items")