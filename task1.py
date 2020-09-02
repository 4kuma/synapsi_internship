from data import *
from random import randint
from json import dumps


class Product(ParentProduct):
    def __init__(self, name, amount, price):
        super().__init__(name)
        self.amount = int(amount)
        self.price = int(price)

    def show_price(self, currency):
        print(f'{self.name} price is {self.price} {currency}')

    def show_amount(self):
        print(f'{self.name} amount is {self.amount}')

    def calculate_total_value(self):
        return self.amount * self.price


def main():
    generated_products = [(p['name'],
                           randint(p['amount']['min'], p['amount']['max']),
                           randint(p['price']['min'], p['price']['max']))
                          for p in products]
    obj_list = [Product(*g) for g in generated_products]
    summary_values = [{'name': o.name, 'summary_value': o.calculate_total_value()} for o in obj_list]

    with open('results_01.txt', 'w') as output_file:
        output_file.write(f'products = {products}\n')
        s = '{'
        for o in obj_list: s += f'{dumps(o.__dict__)},'
        s = s[:-1] + '}'
        objects_string = f'obj_list = {s}\n'
        output_file.write(objects_string)
        output_file.write(f'summary_values = {summary_values}')


if __name__ == '__main__':
    main()
