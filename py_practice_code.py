shopping_cart = {
    "tax": .08,
    "items": [
        {
            "title": "orange juice",
            "price": 3.99,
            "quantity": 1
        },
        {
            "title": "rice",
            "price": 1.99,
            "quantity": 3
        },
        {
            "title": "beans",
            "price": 0.99,
            "quantity": 3
        },
        {
            "title": "chili sauce",
            "price": 2.99,
            "quantity": 1
        },
        {
            "title": "chocolate",
            "price": 0.75,
            "quantity": 9
        }
    ]
}

def get_average_spent_per_item(dct):
    totalPrice = 0
    totalQuantity = 0
    
    for lod in dct["items"]:
        for p in lod.keys():
            if p == "price":
                totalPrice += lod[p]
            elif p == "quantity":
                totalQuantity += lod[p]
                
    
    print((totalPrice / len(dct["items"])) / totalQuantity)

get_average_spent_per_item(shopping_cart)