from room import Room
from player import Player
from world import World
from util import Queue, Stack

import random # to use shuffle
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt" #try to solve for this first
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
print("PLAYER", player)

# Fill this out with directions to walk
traversal_path = ['n', 's', 'e', 'w']
traversal_path = []
print("T PATH", traversal_path)

#DFS for unexplored rooms
# DO DFS Start by writing an algorithm that picks a random unexplored 
# direction from the player's current room, travels and logs that 
# direction, then loops.

# The depth-first search uses a Stack to remember where it should 
# go when it reaches a dead end.
# https://medium.com/basecs/breaking-down-breadth-first-search-cebe696709d9
# for quick reference of DFS and BFS

def unexplored_rooms(current_path, room_id, player): #from world.py
# reference social project
    visited = set()
  
    q = Queue()
    path = [room_id]
    
    q.enqueue([path])

    while q.size() > 0:
        path = q.dequeue()
        vroom = path[0]

    if vroom not in visited:
        visited[vroom] = path
        print("VISITED CUE", visited)

        for neighbors in current_path[vroom]:
            copy_of_path = path.copy()
            copy_of_path.insert(0, node)
            q.enqueue(copy_of_path)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)



for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
