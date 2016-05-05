



def Tuples():
    tuple = ('Max Mustermann', 'Mustermann Road 12', '2121324432', '13','max@mustermann.de')
    *personal_data, email = tuple
    print ('The personal data is: {} and the E-Mail is: {}'.format(personal_data, email))


    tuple = ('A','B',('C',('D','E')))
    *first_element, (second_element, (third_element)) = tuple
    print ('First element: {}, the second element: {}, the third element: {}'.format(first_element,second_element, third_element))


def Dictionary():
    book = {'Book1': 2001, 'Book2': 2003, 'Book3': 2005, 'Book4': 1980, 'Book5': 1990}
    print ('Dict Keys: {} and dict values: {}'.format(book.keys(), book.values()) )
    for key, value in book.items():
        print (key, value)
    for index, entry in enumerate(sorted(book)):
        print (index, entry)
    for index, entry in enumerate(sorted(book.values())):
        print (index, entry)
    zip_keys = zip(book.values(), book.keys())
    print ('Changed Key/Values {}'.format([element for element in zip_keys]))
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

if __name__ == '__main__':
    Tuples()
    Dictionary()