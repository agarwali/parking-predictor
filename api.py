from math import exp
import random
import json
import random
import requests
from pprint import pprint
from functions import *

PARKING_API_KEY = 'AIzaSyDg7g9prn5vV3uNTA9O-GxACZFK1FSCCQg'
DIST_API_KEY = 'AIzaSyDdgl0atVsTB3mod1APbCzBzzOqr6jwmQU'
radius = '1000'


def get_lambda():
    return random.randint(0, random.randint(10, 20))

def get_prob_taken(timeDiff):
    return 1-exp(-get_lambda()*timeDiff)


def get_time_away(carLoc, lotLoc):
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins='+carLoc[0]+','+carLoc[1]+'&destinations='+lotLoc[0]+','+lotLoc[1]+'&key='+DIST_API_KEY
    r = requests.get(url)
    data = json.loads(r.content)
    return data['rows'][0]['elements'][0]['duration']['value']

def prob_finding_space(carLoc, lotLoc, capacity):
    plotLoc = (float(lotLoc[0]), float(lotLoc[1]))
    empty_spaces = capacity - compute_occupied_spaces(plotLoc, capacity)
    
    timeDiff = get_time_away(carLoc, lotLoc)
    return (empty_spaces, get_prob_taken(timeDiff)*empty_spaces/capacity)


def parking_near_zipcode(latitude, longitude):
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+latitude+','+longitude+'&radius='+radius+'&type=parking&key='+PARKING_API_KEY
    r = requests.get(url)
    data = json.loads(r.content)
    filtered_data = []
    for i,lot in enumerate(data['results']):
        pk_capacity = random.randint(25, 55)
        probData = prob_finding_space([latitude, longitude], [str(lot['geometry']['location']['lat']), str(lot['geometry']['location']['lng'])], pk_capacity)
        left = int(probData[0])
        prob=probData[1]
        parkingData = {'capacity':pk_capacity, 'left': left, 'prob': prob}
        filtered_data.append({'geometry':lot['geometry'], 'parkingData': parkingData})
    return filtered_data

def main():
    print(parking_near_zipcode('38.219053699999996', '-85.7532753'))
    # my_loc = ['38.219053699999996', '-85.7532753']
    # p_loc = ['38.2168179','-85.75560220000001']
    # print prob_finding_space(my_loc, p_loc)

if __name__ == '__main__':
    main()