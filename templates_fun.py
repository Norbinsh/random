# So templates existed huh
# Feels like .format() is just better but I guess this can come in handy, at
# times...


from string import Template
from random import randint


class ProductCalculator(object):
    cart = []
    cart.append(dict(item="bamba", price=5, amount=1))
    cart.append(dict(item="milky", price=4, amount=12))

    t = Template("$amount * $item = $price")
    total = 0
    print("Calc: ")
    for item in cart:
        print(t.substitute(item))
        total += (item["price"] * item["amount"])
    print("Total: "+str(total))

ProductCalculator()


"""
Calc:
1 * bamba = 5
12 * milky = 4
Total: 53
"""


class GasPrice(object):
    gas_market = []
    x = randint(5,10000)
    gas_market.append(dict(a=x, b=x, c=x, d=x))

    t = Template("$a $b $c $d $e") # Using safe_substitute method, that would
    # display literal when there's no value match
    for estimated_price in gas_market:
        print(t.safe_substitute(estimated_price))

pi = GasPrice()


"""
8992 8992 8992 8992 $e
"""