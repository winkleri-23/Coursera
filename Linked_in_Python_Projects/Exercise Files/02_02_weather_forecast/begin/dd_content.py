import csv
import random
from urllib import request
import json
import datetime

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

def get_weather_forecast(coords = {'lat': 30.2748, 'lon': -97.7404}):
    try:
        api_key = ''
        url = f'http://api.openweathermap.org/data/2.5/forecast?lat=51.5098&lon=-0.1180&limit=5&appid={api_key}'
        data = json.load(request.urlopen(url))

        forecast = {'city': data['city']['name'],
                    'country': data['city']['country'],
                    'periods': list()
                    }


        # for period in data['list'][0:9]: # populate list with next 9 forecast periods 
        #     forecast['periods'].append({'timestamp': datetime.datetime.fromtimestamp(period['dt']),
        #                                 'temp': round(period['main']['temp']),
        #                                 'description': period['weather'][0]['description'].title(),
        #                                 'icon': f'http://openweathermap.org/img/wn/{period["weather"][0]["icon"]}.png'})
        for period in data['list'][0:9]:
            forecast['periods'].append({'timestamp': datetime.datetime.fromtimestamp(period['dt']),
                                        'temp': round(period['main']['temp']),
                                        'description': period['weather'][0]['description'].title(),
                                        'icon': f'http://openweathermap.org/img/wn/{period["weather"][0]["icon"]}.png'
                                        })
        print( forecast )
        return forecast

    except Exception as e:
        print(e)

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

    forecast = get_weather_forecast()

    if forecast:
        print(f'\n Weather forecaset for {forecast["city"]}, {forecast["country"]} is ...' )
        for period in forecast['periods']:
            print(f' - {period["timestamp"]} | {period["temp"]} | {period["description"]}')
    else:
        print("Problem")