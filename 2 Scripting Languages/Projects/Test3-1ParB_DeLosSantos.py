# Fill in table information and pass to Class

from retailDeLosSantos import RetailItem
import pandas as pd

def main():
    prod1 = RetailItem('Jacket', 12, 249.99)

    prod2 = RetailItem('Designer Jeans', 30, 199.99)
    prod3 = RetailItem('Shirt', 45, 49.99)

    d = {'Description':[prod1.get_description(), prod2.get_description(), prod3.get_description()],
        'Units':[prod1.get_description(), prod2.get_description(), prod3.get_description()],
        'Price':[prod1.get_price(), prod2.get_price(), prod3.get_price()]
    }

    df_retail = pd.DataFrame(d, index = ('Product 1', 'Product 2', 'Product 3'))
    print(df_retail)

main()