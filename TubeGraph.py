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
            connections[station1] = [station2]
        if station2 not in connections.keys():
            connections[station2] = [station1]
        else:
            connections[station1].append(station2)
            connections[station2].append(station1)
    
    
                                   
    
        
            
            

def main():
    station_data()
    connections_data()
    free_roam()

main()
