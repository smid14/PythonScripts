'''
Scripts that deal with dictionaries
Based on Python 3.4.3
'''
from collections import defaultdict



def dictionary_basic():
    book = {'Book1': 2001, 'Book2': 2003, 'Book3': 2005, 'Book4': 1980, 'Book5': 1990}
    #Get the Keys:
    print ('Dict Keys: ', book.keys())
    #Get the values:
    print ('Dict Values: ', book.values())
    #Change the publisher Date of Book2
    book['Book2'] = 1998
    #Check if specific key is in  book dict
    print ('Book3' in book)
    print ('Book8' in book)


def dictionary_comprehensions():
    strings = ('Peter', 'Paul', 'Donald', 'Daisy', 'Michael')
    string_length = {x: len(x) for x in strings}
    print ('Dictionary for Strings and the length: ', string_length)

    pairs = [('Book1', 2001), ('Book2', 2013), ('Book3', 2000)]
    pairs_dict = dict(pairs)
    print ('Key Value List to Dictionary: ', pairs_dict)


def dictionary_loops():
    #Loop trough a dict:
    book = {'Book1': 2001, 'Book2': 2003, 'Book3': 2005, 'Book4': 1980, 'Book5': 1990}
    for key, value in book.items():
        print (key, value)

    #Index the dict while looping sorted by the key:
    for index, entry in enumerate(sorted(book)):
        print (index, entry)

    #Index the dict while looping sorted by the value:
    for index, entry in enumerate(sorted(book.values())):
        print (index, entry)

# Implemented with defaultdict
# Check
def multi_dictionary():
    dict_list = defaultdict(list)
    dict_list['Book1'].append('Goethe')
    dict_list['Book1'].append('Schiller')
    dict_list['Book1'].append('Lessing')
    dict_list['Book2'].append('Mann')
    dict_list['Book2'].append('Tolkin')
    print('Multi Dict: ', dict_list)

    dict_set = defaultdict(set)
    dict_set['Book1'].append('Goethe')
    dict_set['Book1'].append('Schiller')
    dict_set['Book1'].append('Lessing')
    dict_set['Book2'].append('Mann')
    dict_set['Book2'].append('Tolkin')
    print('Multi Dict: ', dict_set)

    dict = defaultdict(list)
    for key, value in range(1,5):
        dict[key].append(value)
    print ('Loop dict: ', dict)

# Check
def calc_dictionary():
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }
    #Switches Key and values
    zip_prices = zip(prices.values(), prices.keys())
    min_prices = min(zip_prices)
    zip_prices = zip(prices.values(), prices.keys())
    max_prices = max(zip_prices)

    print ('Min Prices: ', min_prices)
    print ('Max Prices: ', max_prices)

    min_key = min(prices, key=lambda k: prices[k])
    print (min_key)

    min_value = prices[min(prices, key=lambda k: prices[k])]
    print (min_value)

# Chekc
def compare_dictionary():
    x = {
        'a': 1,
        'b': 2,
        'c': 3,
        'e': 4
    }

    y = {
        'b': 154,
        'c': 24,
        'd': 8,
        'e': 4,
        'a': 1
    }

    same_keys = x.keys() & y.keys()
    inter_keys = y.keys() - x.keys()
    same_pairs = x.items() & y.items()

    print('Same Keys in both dictionaries: {}'.format(same_keys))
    print('Keys in y but not in x: {}'.format(inter_keys))
    print('Find same key/value pairs: {}'.format(same_pairs))

#More to come

if __name__ == "__main__":
    #dictionary_basic()
    #calc_dictionary()
    #multi_dictionary()
    #dictionary_comprehensions()
    compare_dictionary()
    #dictionary_loops()
