#simple reflex agent
class Environment:
    def __init__(self, beds):
        self.beds = beds

    def get_precept(self, i):
        return self.beds[i]

    def get_number_states(self):
        return len(self.beds)

    def display(self):
        for i in range(len(self.beds)):
            print(f"Bed {i + 1}: {self.beds[i]}")


class SimpleReflexAgent:
    def __init__(self):
        self.index = 0

    def act(self, state, grid):
        if (state == "Dry"):
            grid[self.index] = "Moist"
            return "Watered"
        return "Skip"

    def move(self):
        self.index += 1


def run_agent(environment, agent):
    for i in range(environment.get_number_states()):
        state = environment.get_precept(i)
        action = agent.act(state, environment.beds)
        print(f"Step {i + 1}: Position {i} -> Percept - {state}, Action - {action}")
        agent.move()

    print()
    environment.display()


a = SimpleReflexAgent()
e = Environment(["Moist", "Dry", "Moist", "Moist", "Dry", "Moist", "Dry", "Moist", "Dry"])

run_agent(e, a)

#model based agents
class Environment:
    def __init__(self, path):
        self.path = path

    def get_precept(self, i):
        return self.path[i]

    def get_path_size(self):
        return len(self.path)


class ModelBasedAgent:
    def __init__(self):
        self.__has_key = False

    def act(self, precept):
        if precept == 'D' and not self.__has_key:
            return f"Access denied to room {precept}"

        s = ""
        if precept == 'B' and not self.__has_key:
            self.update_key()
            s = f", Key acquired in room {precept}"

        return f"Access granted to room {precept}" + s

    def update_key(self):
        self.__has_key = True


def run_agent(environment: Environment, agent: ModelBasedAgent):
    for i in range(environment.get_path_size()):
        percept = environment.get_precept(i)
        action = agent.act(percept)

        print(f"Step {i + 1}: Position {i} -> Percept - {percept}, Action - {action}")


e = Environment(["A", "C", "D", "B", "D"])
a = ModelBasedAgent()

run_agent(e, a)

#goal based agents
class Environment:
    def __init__(self, path):
        self.path = path

    def get_percept(self, i):
        return self.path[i]

    def get_path_size(self):
        return len(self.path)


class GoalBasedAgent:
    def __init__(self):
        self.goal = "Red House"

    def formulate_goal(self):
        return self.goal

    def act(self, percept):
        if percept == self.goal:
            return "Found! Exiting..."
        return "Not Found"


def run_agent(environment: Environment, agent: GoalBasedAgent):
    for i in range(environment.get_path_size()):
        percept = environment.get_percept(i)
        action = agent.act(percept)

        print(f"Step {i + 1}: Position {i} -> Percept - {percept}, Action - {action}")
        if (action != "Not Found"):
            return


e = Environment(['Blue House', 'Green House', 'Red House', 'Yellow House', 'White House'])
a = GoalBasedAgent()

run_agent(e, a)
import math


class Environment:
    def __init__(self, rocks):
        self.rocks = rocks

    def get_percept(self):
        return self.rocks


class UtilityBasedAgent:
    def __init__(self):
        pass

    def utility(self, rock):
        return rock['value'] * 2 - rock["cost"]

    def act(self, percept):
        best_rock = None
        best_utility = -math.inf

        for rock in percept:
            rock_utility = self.utility(percept[rock])
            if rock_utility > best_utility:
                best_rock = rock
                best_utility = rock_utility

        return f"{best_rock} is the best rock"

#utlity based agents
def run_agent(environment: Environment, agent: UtilityBasedAgent):
    percept = environment.get_percept()
    action = agent.act(percept)

    print(f"Percept - {percept}\nAction - {action}")


e = Environment({
    "Rock A": {
        "value": 5,
        "cost": 2
    },
    "Rock B": {
        "value": 9,
        "cost": 8
    },
    "Rock C": {
        "value": 6,
        "cost": 3
    }
})

a = UtilityBasedAgent()

run_agent(e, a)

#bfs search
# Tree representation
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}

# BFS function
def bfs(tree, start, goal):
    visited = []  # List to keep track of visited nodes
    queue = []    # Initialize a queue

    visited.append(start)
    queue.append(start)

    while queue:
        node = queue.pop(0)  # Dequeue
        print(node, end=" ")

        if node == goal:  # Stop if goal is found
            print("\nGoal found!")
            break

        for neighbour in tree[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Start and goal nodes
start_node = 'A'
goal_node = 'I'

# Run BFS
print("\nFollowing is the Breadth-First Search (BFS):")
bfs(tree, start_node, goal_node)

#bfs goal based agent

# Goal-Based Agent with BFS in a tree
class GoalBasedAgent:
    def __init__(self, goal):
        self.goal = goal

    def formulate_goal(self, percept):
        if percept == self.goal:
            return "Goal reached"
        return "Searching"

    def bfs_search(self, graph, start, goal):
        visited = []  # List for visited nodes
        queue = []    # Initialize a queue

        visited.append(start)
        queue.append(start)

        while queue:
            node = queue.pop(0)  # Dequeue
            print(f"Visiting: {node}")
            if node == goal:  # Stop if goal is found
                return f"Goal {goal} found!"
            for neighbour in graph.get(node, []):
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        return "Goal not found"

    def act(self, percept, graph):
        goal_status = self.formulate_goal(percept)
        if goal_status == "Goal reached":
            return f"Goal {self.goal} found!"
        else:
            return self.bfs_search(graph, percept, self.goal)


class Environment:
    def __init__(self, graph):  # Initial graph/tree/maze
        self.graph = graph

    def get_percept(self, node):
        return node


def run_agent(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    action = agent.act(percept, environment.graph)  # Pass graph to agent
    print(action)


# Tree Representation
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}

# Define Start and Goal Nodes
start_node = 'A'
goal_node = 'I'

# Create instances of agent and environment
agent = GoalBasedAgent(goal_node)
environment = Environment(tree)

# Run the agent
run_agent(agent, environment, start_node)

# ================= DFS =================

def dfs(graph, start, goal):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        print(node, end=" ")

        if node == goal:
            print("\nGoal Found!")
            return

        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))

# Example Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}

print("DFS Traversal:")
dfs(graph, 'A', 'I')


# ================= DFS Agent =================

class DFSAgent:
    def __init__(self, goal):
        self.goal = goal

    def search(self, graph, start):
        visited = []
        stack = [start]

        while stack:
            node = stack.pop()
            print("Visiting:", node)

            if node == self.goal:
                return "Goal Found!"

            if node not in visited:
                visited.append(node)
                stack.extend(reversed(graph[node]))

        return "Goal Not Found"


agent = DFSAgent('I')
print("\nAgent DFS Result:", agent.search(graph, 'A'))


#...................dls...............................
def dls(graph, node, goal, depth):
    if depth == 0:
        return False

    if node == goal:
        print("Goal Found!")
        return True

    for neighbor in graph[node]:
        if dls(graph, neighbor, goal, depth-1):
            return True

    return False


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}

print("DLS Result:")
dls(graph, 'A', 'I', 3)

#.......ids.............................
def dls(node, goal, depth, path):
    if depth == 0:
        return False

    if node == goal:
        path.append(node)
        return True

    for child in graph[node]:
        if dls(child, goal, depth-1, path):
            path.append(node)
            return True

    return False


def iterative_deepening(start, goal, max_depth):
    for depth in range(max_depth + 1):
        path = []
        if dls(start, goal, depth, path):
            print("Path:", list(reversed(path)))
            return
    print("Goal Not Found")


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}

print("IDS Result:")
iterative_deepening('A', 'I', 5)

#..............unifrom cost serach.............................
def ucs(graph, start, goal):
    frontier = [(start, 0)]
    visited = set()
    cost_so_far = {start: 0}
    parent = {start: None}

    while frontier:
        frontier.sort(key=lambda x: x[1])
        node, cost = frontier.pop(0)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            path = []
            while node:
                path.append(node)
                node = parent[node]
            print("Path:", path[::-1])
            print("Cost:", cost)
            return

        for neighbor, weight in graph[node].items():
            new_cost = cost + weight

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                parent[neighbor] = node
                frontier.append((neighbor, new_cost))


graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'D': 4, 'E': 3},
    'C': {'F': 1, 'G': 5},
    'D': {'H': 2},
    'E': {},
    'F': {'I': 6},
    'G': {},
    'H': {},
    'I': {}
}

print("UCS Result:")
ucs(graph, 'A', 'I')

...............best for serach...................
    from queue import PriorityQueue

    # Weighted graph
    graph = {
        'S': [('A', 3), ('B', 6), ('C', 5)],
        'A': [('D', 9), ('E', 8)],
        'B': [('F', 12), ('G', 14)],
        'C': [('H', 7)],
        'H': [('I', 5), ('J', 6)],
        'I': [('K', 1), ('L', 10), ('M', 2)],
        'D': [], 'E': [],
        'F': [], 'G': [],
        'J': [], 'K': [],
        'L': [], 'M': []
    }


    def best_first_search(graph, start, goal):
        visited = set()
        pq = PriorityQueue()
        pq.put((0, start))  # Priority queue with priority as the heuristic value

        while not pq.empty():
            cost, node = pq.get()
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                if node == goal:
                    print("\nGoal reached!")
                    return True
                for neighbor, weight in graph.get(node, []):
                    if neighbor not in visited:
                        pq.put((weight, neighbor))

        print("\nGoal not reachable!")
        return False


    # Example usage:
    print("Best-First Search Path:")
    best_first_search(graph, 'A', 'I')

# ....................maze game using best for search......................
from queue import PriorityQueue

# Node class for Best-First Search
class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # cost from start node to current node
        self.h = 0  # heuristic estimate of cost to end node
        self.f = 0  # total cost (for Best-First, f = h)

    def __lt__(self, other):
        return self.f < other.f

# Manhattan distance heuristic
def heuristic(current_pos, end_pos):
    return abs(current_pos[0] - end_pos[0]) + abs(current_pos[1] - end_pos[1])

# Best-First Search function
def best_first_search(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    start_node = Node(start)
    end_node = Node(end)

    frontier = PriorityQueue()
    frontier.put(start_node)
    visited = set()

    while not frontier.empty():
        current_node = frontier.get()
        current_pos = current_node.position

        if current_pos == end:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Reverse path from start to end

        visited.add(current_pos)

        # Generate adjacent nodes (up, down, left, right)
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            new_pos = (current_pos[0] + dx, current_pos[1] + dy)
            if (0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and
                maze[new_pos[0]][new_pos[1]] == 0 and new_pos not in visited):
                new_node = Node(new_pos, current_node)
                new_node.g = current_node.g + 1
                new_node.h = heuristic(new_pos, end)
                new_node.f = new_node.h  # Best-First Search uses only heuristic
                frontier.put(new_node)
                visited.add(new_pos)

    return None  # No path found

# Example maze (0 = open, 1 = blocked)
maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
end = (4, 4)

path = best_first_search(maze, start, end)

if path:
    print("Path found:", path)
else:
    print("No path found")

# .......................greedy best for search  ........................................
# Graph with different edge costs
graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'D': 4, 'E': 3},
    'C': {'F': 1, 'G': 5},
    'D': {'H': 2},
    'E': {},
    'F': {'I': 6},
    'G': {},
    'H': {},
    'I': {}
}

# Heuristic function (estimated cost to reach goal 'I')
heuristic = {'A': 7, 'B': 6, 'C': 5, 'D': 4, 'E': 7,
             'F': 3, 'G': 6, 'H': 2, 'I': 0}

# Greedy Best-First Search (GBFS) without heapq
def greedy_bfs(graph, start, goal):
    frontier = [(start, heuristic[start])]  # List-based priority queue
    visited = set()  # Keep track of visited nodes
    came_from = {start: None}  # For path reconstruction

    while frontier:
        # Sort frontier manually by heuristic (ascending)
        frontier.sort(key=lambda x: x[1])
        current_node, _ = frontier.pop(0)

        if current_node in visited:
            continue

        print(current_node, end=" ")  # Print visited node
        visited.add(current_node)

        # If goal is reached, reconstruct path
        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            print(f"\nGoal found with GBFS. Path: {path}")
            return

        # Expand neighbors
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                came_from[neighbor] = current_node
                frontier.append((neighbor, heuristic[neighbor]))

    print("\nGoal not found")

# Run Greedy Best-First Search
print("\nFollowing is the Greedy Best-First Search (GBFS):")
greedy_bfs(graph, 'A', 'I')

# ...................a star algorithm.................................................
# A* Search Implementation (List-based frontier)
# Graph with edge costs
graph = {
    'A': {'B': 4, 'C': 3},
    'B': {'E': 12, 'F': 5},
    'C': {'D': 7, 'E': 10},
    'D': {'E': 2},
    'E': {'G': 5},
    'F': {'G': 16},
    'G': {}
}

# Heuristic values (estimated cost to goal 'G')
heuristic = {'A': 14, 'B': 12, 'C': 11, 'D': 6, 'E': 4, 'F': 11, 'G': 0}

def a_star(graph, start, goal):
    frontier = [(start, 0 + heuristic[start])]  # List-based priority queue
    visited = set()
    g_costs = {start: 0}  # Actual cost from start to each node
    came_from = {start: None}  # For path reconstruction

    while frontier:
        # Sort frontier by f(n) = g(n) + h(n)
        frontier.sort(key=lambda x: x[1])
        current_node, current_f = frontier.pop(0)

        if current_node in visited:
            continue

        print(current_node, end=" ")  # Print visited node
        visited.add(current_node)

        # Goal check
        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            print(f"\nGoal found with A*. Path: {path}")
            return

        # Explore neighbors
        for neighbor, cost in graph[current_node].items():
            new_g_cost = g_costs[current_node] + cost  # Cost to neighbor
            f_cost = new_g_cost + heuristic[neighbor]  # f(n) = g(n) + h(n)

            if neighbor not in g_costs or new_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = new_g_cost
                came_from[neighbor] = current_node
                frontier.append((neighbor, f_cost))

    print("\nGoal not found")

# Run A* Search
print("\nFollowing is the A* Search:")
a_star(graph, 'A', 'G')

.......genetic algorithm...................
import random

# ================= PARAMETERS =================
POP_SIZE = 6
CHROMOSOME_LENGTH = 5
GENERATIONS = 10
MUTATION_RATE = 0.1

# ================= FITNESS FUNCTION =================
# Example: maximize number of 1s
def fitness(chromosome):
    return sum(chromosome)


# ================= INITIAL POPULATION =================
def create_population():
    population = []
    for _ in range(POP_SIZE):
        chromosome = [random.randint(0,1) for _ in range(CHROMOSOME_LENGTH)]
        population.append(chromosome)
    return population


# ================= SELECTION (Tournament) =================
def selection(population):
    a = random.choice(population)
    b = random.choice(population)
    return a if fitness(a) > fitness(b) else b


# ================= CROSSOVER =================
def crossover(parent1, parent2):
    point = random.randint(1, CHROMOSOME_LENGTH - 1)
    child = parent1[:point] + parent2[point:]
    return child


# ================= MUTATION =================
def mutate(chromosome):
    for i in range(len(chromosome)):
        if random.random() < MUTATION_RATE:
            chromosome[i] = 1 - chromosome[i]  # flip bit
    return chromosome


# ================= GENETIC ALGORITHM =================
def genetic_algorithm():
    population = create_population()

    for gen in range(GENERATIONS):
        print(f"\nGeneration {gen+1}: {population}")

        new_population = []

        for _ in range(POP_SIZE):
            parent1 = selection(population)
            parent2 = selection(population)

            child = crossover(parent1, parent2)
            child = mutate(child)

            new_population.append(child)

        population = new_population

    # Best solution
    best = max(population, key=fitness)
    print("\nBest Solution:", best)
    print("Fitness:", fitness(best))


# ================= RUN =================
genetic_algorithm()

#...chnage fitness....
def fitness(chromosome):
    return int("".join(map(str, chromosome)), 2)
#single pt vs two pt crossover
def crossover(p1, p2):
    p1_idx = random.randint(0, CHROMOSOME_LENGTH-2)
    p2_idx = random.randint(p1_idx+1, CHROMOSOME_LENGTH-1)

    return p1[:p1_idx] + p2[p1_idx:p2_idx] + p1[p2_idx:]

#...elitisn.....
best = max(population, key=fitness)
new_population.append(best)