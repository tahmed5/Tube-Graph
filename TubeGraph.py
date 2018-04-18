import random
import pprint
#1: [52, 73, 73, 234, 265]
def station_data():
    global stations
    stations = {} #holds station key with station name 
    file = open('stations.csv', 'r')
    lines = file.read().splitlines()
    for line in lines:
        items = line.split(',')
        stations[int(items[0])] = items[3]


def connections_data():
    global connections
    global connected_lines
    global text_connections
    connections = {} #holds station 1 key and station 2 key
    connected_lines = {} #holds concatenated key of both stations and lines

    text_connections = {}
    
    file = open('connections.csv','r')
    lines = file.read().splitlines()
    for line in lines:
        items = line.split(',')
        both_stations = items[0] + items[1]
        flipped_both_stations = items[1] + items[0]

        if (both_stations not in connected_lines.keys()) and (flipped_both_stations not in connected_lines.keys() ):
            connected_lines[both_stations] = []
            
        if both_stations in connected_lines.keys():
            connected_lines[both_stations].append(items[2])

        if flipped_both_stations in connected_lines.keys():
            connected_lines[flipped_both_stations].append(items[2])

            
        
        station1 = int(items[0])
        station2 = int(items[1])

        text_station1 = stations.get(station1)
        text_station2 = stations.get(station2)

        ########

        if text_station1 not in text_connections.keys():
            text_connections[text_station1] = []

        if text_station2 not in text_connections.keys():
            text_connections[text_station2] = []

        text_connections[text_station2].append(text_station1)
        text_connections[text_station1].append(text_station2)           


        #######
        
        if station1 not in connections.keys():
            connections[station1] = []
        if station2 not in connections.keys():
            connections[station2] = []

        connections[station2].append(station1)
        connections[station1].append(station2)



def lines_data():
    global tube_lines
    tube_lines = {} # holds Line Key and Line Name
    
    file = open('lines.csv','r')
    lines = file.read().splitlines()
    
    for line in lines:
        items = line.split(',')
        tube_lines[int(items[0])] = items[1]


def dfs():
    station_check = True
    
    while station_check == True:
        start_station = input('Enter Your Start Station')
        end_station = input('Enter Your End Station')
        start_station = start_station.lower()
        if start_station == 'q':
            quit()
        for key in stations:
            if start_station == stations[key].lower():
                start_station_key = key
                start_station_check = False
        if start_station_check == True:
            print('Station Not Found - Enter Start Station Again')
    

def station_lines(current, neighbour):
    current,neighbour = str(current), str(neighbour)
    connectedkey = current + neighbour

    
    if connected_lines.get(connectedkey) == None:
        connectedkey = neighbour + current
        
    if connectedkey not in temp_station.keys():
        temp_station[connectedkey] = []
        for line in connected_lines[connectedkey]:
            temp_station[connectedkey].append(line)

    line = tube_lines[int(temp_station[connectedkey][0])]
    
    del temp_station[connectedkey][0]

    return line




    
def free_roam():
    pprint.pprint(text_connections)
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
    first_station = start_station_key
    line = None
    while roaming == True:
        print('You are at:', stations[current_station])
        print('Do you want to go to:')
        global temp_station
        temp_station = {}
        for x in range(len(connections[current_station])):
            print(x + 1, stations[connections[current_station][x]], 'via' , station_lines(current_station, connections[current_station][x]))
        print(temp_station)
        user_station = int(input('Enter The Number Of The Station You Wish To Visit\n'))
        user_station -= 1
        if 0 <= user_station <= len(connections[current_station]) - 1:
            current_station = connections[current_station][user_station]
        
        
            
    
def main():
    station_data()
    connections_data()
    lines_data()
    print('Do you wish to:')
    print('1: Free Roam')
    print('2: DFS')
    print('3: BFS')
    choice = int(input())
    if choice == 1:
        free_roam()
    elif choice == 2:
        pass
    elif choice == 3:
        dfs()




main()
