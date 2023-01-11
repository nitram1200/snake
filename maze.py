import numpy as np

maze = [

    [" ", " ", " ", "#", "S", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", "#", " ", "#", "#", "#", "#", "#", " ", " ", " ", " ", " "],
    ["#", "#", " ", "#", " ", "#", " ", " ", " ", "#", " ", " ", " ", " ", " "],
    ["#", "#", " ", "#", " ", "#", " ", "#", " ", "#", " ", " ", " ", " ", " "],
    ["#", "#", " ", "#", " ", "#", " ", "#", " ", "#", " ", " ", " ", " ", " "],
    ["#", "#", "#", "#", " ", "#", " ", "#", " ", " ", " ", " ", " ", " ", " "],
    ["#", " ", " ", " ", " ", "#", " ", "#", " ", " ", " ", " ", " ", " ", " "],
    ["#", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " "],
    ["#", "#", "#", "#", "#", "#", "#", "#", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", "F", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
]


snake_list = [[500, 400], [400, 400], [300, 400], [200, 400], [100, 400], [0, 400]]
food = [1200, 300]
snake_size = 100


def pathfinder(maze):

    start = [snake_list[-1][0]//snake_size, snake_list[-1][1]//snake_size]  # Head of the snake
    start = (start[0], start[1])
    finish = tuple([food[0]//snake_size, food[1]//snake_size])  # Location of the food
    print(type(start))

    temp = start  # 'virtual' head of the snake on its exploration
    inf = maze.__sizeof__()  # Longest path possible
    andmed = {}
    visited = []  # Cells we have already looked
    min_list = []  # Shortest path

    for row in range(len(maze)):
        for col in range(len(maze)):
            if maze[row][col] != '#':
                distance = int(np.sqrt((finish[0] - row) ** 2 + (finish[1] - col) ** 2))
                andmed[(row, col)] = {"g": inf, "h": distance, "been": [], 'direction': []}

    andmed[start]["g"] = 0
    #for x in andmed:
    #    print(x, end=" ;")
    #    print(andmed[(x)])

    kohal = False
    tries = 0

    while not kohal:
        tries += 1
        #print("Esimene: ", temp)
        if temp not in visited:
            #print("temp, not in visited: ", temp)
            #print("visited", visited)

            visited.append(temp)
            print(temp)
            juures = [
                ((temp[0] + 1, temp[1]), 'd'),  # down
                ((temp[0] - 1, temp[1]), 'u'),  # up
                ((temp[0], temp[1] + 1), 'r'),  # right
                ((temp[0], temp[1] - 1), 'l')  # left
            ]
            print(juures)
            for j in juures:
                # print("Juures: ", j)
                if j[0] in andmed:
                    #print(j[0])
                    #print("väljakul")
                    if j[0] not in visited:
                        g = andmed[temp]["g"] + 1  # Cells from the start
                        #print("Uus ruut", g)
                        if g < andmed[j[0]]["g"]:
                            andmed[j[0]]["g"] = g
                            andmed[j[0]]['direction'] = andmed[temp]['direction'] + [j[1]]
                            print(j[1])
                            andmed[j[0]]["been"] = andmed[temp]["been"] + [temp]  # Route to this cell
                    summa = andmed[j[0]]["g"] + andmed[j[0]]['h']
                    min_list.append([summa, j[0]])  # How long is the current path + the path remaining

        min_list.sort()
        temp = min_list[0][1]  # selecting an adjacent cell
        #print(min_list)
        min_list.pop(0)
        #print(min_list)
        if temp == finish:
            break

    for x in andmed[temp]["been"]:
        maze[x[0]][x[1]] = "+"
    for x in maze:
        print(x)
    #for x in andmed:
        #print(x, end='; ')
        #print(andmed[x])
    print(andmed[temp]['direction'])
    print(f"Path found in {tries} tries")


pathfinder(maze)
