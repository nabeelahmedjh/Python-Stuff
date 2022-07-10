

def main():
    compute_change()
    return 0


def compute_change():

    coke_price = 50
    while (coke_price > 0):
        print(f"Amount due: {coke_price}")
        coin = int(input("Insert Coin: "))
        if (coin in [25, 10, 5]):
            coke_price -= coin

    print(f"Change owed: {-1*coke_price}")


main()
