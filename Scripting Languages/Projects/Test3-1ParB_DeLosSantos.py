from retailDeLosSantos import RetailItem

def main():
    prod1 = RetailItem('Jacket', 12, 249.99)
    prod1.set_description('Jacket')
    prod1.set_units(12)
    prod1.set_price(249.99)

    prod2 = RetailItem('Designer Jeans', 30, 199.99)

    prod3 = RetailItem('Shirt', 45, 49.99)

    print('Product 1: ', prod1.get_description(), prod1.get_units(), prod1.get_price())

main()