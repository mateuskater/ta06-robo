def printMaze(maze):
    for listy in maze:
        print(''.join(listy))

with open('maze.txt','r') as file:
    string = file.read()

maze = list(list(listy) for listy in string.split('\n'))
visible_maze = 

