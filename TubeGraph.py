import random

def station_data():
    global stations
    stations = {}
    file = open('stations.csv', 'r')
    lines = file.read().splitlines()
    for line in lines:
        items = line.split(',')
        stations[int(items[0])] = items[3]

def connections_data():
    global connections
    connections = {}
    file = open('connections.csv','r')
    lines = file.read().splitlines()
    for line in lines:
        items = line.split(',')
        station1 = int(items[0])
        station2 = int(items[1])
        if station1 not in connections.keys():
            connections[station1] = []
        if station2 not in connections.keys():
            connections[station2] = []
        connections[station1].append(station2)
        connections[station2].append(station1)
    
def free_roam():
    print('Which station would you like to start from ')
    print('If you want to quit enter "Q"')
    print('============================================')
    start_station_check = True
    
    while start_station_check == True:
        start_station = input()
        start_station = start_station.lower()
        if start_station == 'q':
            quit()
        for key in stations:
            if start_station == stations[key].lower():
                start_station_key = key
                start_station_check = False
        if start_station_check == True:
            print('Station Not Found - Enter Start Station Again')

    roaming = True
    current_station = start_station_key
    while roaming == True:
        print('You are at:', stations[current_station])
        print('Do you want to go to:')
        for x in range(len(connections[current_station])):
            print(x + 1, stations[connections[current_station][x]])
            
        user_station = int(input('Enter The Number Of The Station You Wish To Visit\n'))
        user_station -= 1
        if 0 <= user_station <= len(connections[current_station]) - 1:
            current_station = connections[current_station][user_station]
        
        
            
        

        
    
    
                                   
    
        
            
            

def main():
    station_data()
    connections_data()
    free_roam()

main()
