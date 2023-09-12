import csv
import random

"""
Retrieve a random quote from the specified CSV file.
"""
def get_random_quote(quotes_file='quotes.csv'):
    try: # load motivational quotes from csv file 
       with open(quotes_file) as csvfile:
           quotes = [{'author': line[0],
                      'quote': line[1]} for line in csv.reader(csvfile, delimiter='|')]

    except Exception as e: # use a default quote to help things turn out for the best
        quotes = [{'author': 'Eric Idle',
                   'quote': 'Always Look on the Bright Side of Life.'}]
    
    return random.choice(quotes)

def get_weather_forecast():
    pass

def get_twitter_trends():
    pass

def get_wikipedia_article():
    pass

if __name__ == '__main__':
    ##### test get_random_quote() #####
    print('\nTesting quote generation...')

    quote = get_random_quote()
    print(f' - Random quote is "{quote["quote"]}" - {quote["author"]}')
    
    quote = get_random_quote(quotes_file = None)
    print(f' - Default quote is "{quote["quote"]}" - {quote["author"]}')