#kmeans
# Importing libraries
import numpy as nm
import matplotlib.pyplot as mtp
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Import dataset
df = pd.read_csv('Mall_Customers.csv')

# Extract required columns (Annual Income, Spending Score)
x = df.iloc[:, [3, 4]].values

# ---------------- ELBOW METHOD ----------------
wcss_list = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(x)
    wcss_list.append(kmeans.inertia_)

# Plot Elbow Graph
mtp.plot(range(1, 11), wcss_list)
mtp.title('Elbow Method')
mtp.xlabel('Number of clusters (k)')
mtp.ylabel('WCSS')
mtp.show()

# ---------------- FEATURE SCALING ----------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(x)

# ---------------- K-MEANS TRAINING ----------------
kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
y_predict = kmeans.fit_predict(X_scaled)

# ---------------- VISUALIZATION ----------------
mtp.scatter(x[y_predict == 0, 0], x[y_predict == 0, 1], s=100, c='blue', label='Cluster 1')
mtp.scatter(x[y_predict == 1, 0], x[y_predict == 1, 1], s=100, c='green', label='Cluster 2')
mtp.scatter(x[y_predict == 2, 0], x[y_predict == 2, 1], s=100, c='red', label='Cluster 3')
mtp.scatter(x[y_predict == 3, 0], x[y_predict == 3, 1], s=100, c='black', label='Cluster 4')
mtp.scatter(x[y_predict == 4, 0], x[y_predict == 4, 1], s=100, c='purple', label='Cluster 5')

# Plot centroids
mtp.scatter(kmeans.cluster_centers_[:, 0],
            kmeans.cluster_centers_[:, 1],
            s=300, c='yellow', label='Centroids')

# Labels
mtp.title('Clusters of Customers')
mtp.xlabel('Annual Income (k$)')
mtp.ylabel('Spending Score (1-100)')
mtp.legend()
mtp.show()



#decsin trees
from sklearn.tree import DecisionTreeClassifier
# Initialize the DecisionTreeClassifier
DT = DecisionTreeClassifier()
# Train the model
ModelDT = DT.fit(x_train, y_train)
# Model Testing (Prediction)
PredictionDT = DT.predict(x_test)
print(&quot;Predictions:&quot;, PredictionDT)
# Model Training Accuracy
print(&#39;====================DT Training Accuracy===============&#39;)
tracDT = DT.score(x_train, y_train) # The score method gives accuracy
directly
TrainingAccDT = tracDT * 100
print(f&quot;Training Accuracy: {TrainingAccDT:.2f}%&quot;)
# Model Testing Accuracy
print(&#39;=====================DT Testing Accuracy=================&#39;)
teacDT = accuracy_score(y_test, PredictionDT)
testingAccDT = teacDT * 100
print(f&quot;Testing Accuracy: {testingAccDT:.2f}%&quot;)

#implement linear regression
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2,
random_state=42)
# Create and train the Linear Regression model
LR = LinearRegression()
ModelLR = LR.fit(x_train, y_train)
# Predict on the test data
PredictionLR = ModelLR.predict(x_test)
# Print the predictions
print(&quot;Predictions:&quot;, PredictionLR)


#eda
pip install pandas

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
import warnings
warnings.filterwarnings('ignore')

# read
df_mat = pd.read_csv(r'/content/student-mat.csv', delimiter=';')
df_por = pd.read_csv(r'/content/student-por.csv',delimiter=';')

#show 10 records
df_mat.head(10)

# print number of rows and columns
df_mat.shape

#2.2
!pip install python-docx
from docx import Document

# Load the document
doc = open(r'/content/student.txt')

# Read and print paragraphs
for para in doc:
    print(para)

 # count the number of true values
df_mat.isna().sum()

#check duplictae
df_por.duplicated()
#check duplocate sum
df_mat.duplicated().sum()

# Check Null and Dtypes
df_mat.info()

#checking nuber of unique value of each col
df_mat.nunique()

#check statistics of the data
df_mat.describe()

#print category in each column
for column in df_por.columns:
    print(f"Categories in {column} variable:     ",end=" " )
    print(df_por[column].unique())

# define numerical & categorical columns
numeric_features = [feature for feature in df_mat.columns if df_mat[feature].dtype != 'O']
categorical_features = [feature for feature in df_mat.columns if df_mat[feature].dtype == 'O']

# print columns
print('We have {} numerical features : {}'.format(len(numeric_features), numeric_features))
print('\nWe have {} categorical features : {}'.format(len(categorical_features), categorical_features))


#adding column
df_por['total score'] = df_por['G1'] + df_por['G2']
df_por['average'] = df_por['total score']/2
df_por.head()

#................
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(25,6))

# Overall distribution
plt.subplot(131)
sns.histplot(data=df_por, x='G3', kde=True)
plt.title("Overall Final Grade Distribution (G3)")

# Female students
plt.subplot(132)
sns.histplot(data=df_por[df_por['sex']=='F'], x='G3', kde=True)
plt.title("Female Students G3 Distribution")

# Male students
plt.subplot(133)
sns.histplot(data=df_por[df_por['sex']=='M'], x='G3', kde=True)
plt.title("Male Students G3 Distribution")

plt.tight_layout()
plt.show()

#.....................
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(18,8))

# G1
plt.subplot(1, 3, 1)
plt.title('G1 SCORES')
sns.violinplot(y='G1', data=df_por, linewidth=3)

# G2
plt.subplot(1, 3, 2)
plt.title('G2 SCORES')
sns.violinplot(y='G2', data=df_por, linewidth=3)

# G3
plt.subplot(1, 3, 3)
plt.title('G3 SCORES')
sns.violinplot(y='G3', data=df_por, linewidth=3)

plt.tight_layout()
plt.show()

#...........
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (30, 12)

# 1. Gender (sex)
plt.subplot(1, 3, 1)
size = df_por['sex'].value_counts()
labels = size.index
plt.pie(size, labels=labels, autopct='%1.2f%%')
plt.title('Gender (Sex)', fontsize=20)
plt.axis('off')

# 2. School
plt.subplot(1, 3, 2)
size = df_por['school'].value_counts()
labels = size.index
plt.pie(size, labels=labels, autopct='%1.2f%%')
plt.title('School', fontsize=20)
plt.axis('off')

# 3. Address (Urban/Rural)
plt.subplot(1, 3, 3)
size = df_por['address'].value_counts()
labels = size.index
plt.pie(size, labels=labels, autopct='%1.2f%%')
plt.title('Address', fontsize=20)
plt.axis('off')

plt.tight_layout()
plt.show()

#...........
import matplotlib.pyplot as plt
import seaborn as sns

f, ax = plt.subplots(1, 2, figsize=(20, 10))

# Countplot
sns.countplot(x='sex', data=df_por, palette='bright', ax=ax[0], saturation=0.95)

for container in ax[0].containers:
    ax[0].bar_label(container, color='black', size=14)

ax[0].set_title("Gender Count")

# Pie chart
size = df_por['sex'].value_counts()
ax[1].pie(size, labels=size.index, explode=[0, 0.1],
          autopct='%1.1f%%', shadow=True)

ax[1].set_title("Gender Distribution")

plt.tight_layout()
plt.show()
#............
import matplotlib.pyplot as plt
import seaborn as sns

f, ax = plt.subplots(1, 2, figsize=(20, 10))

# Countplot
sns.countplot(x='sex', data=df_por, palette='bright', ax=ax[0], saturation=0.95)

for container in ax[0].containers:
    ax[0].bar_label(container, color='black', size=14)

ax[0].set_title("Gender Count")

# Pie chart
size = df_por['sex'].value_counts()
ax[1].pie(size, labels=size.index, explode=[0, 0.1],
          autopct='%1.1f%%', shadow=True)

ax[1].set_title("Gender Distribution")

plt.tight_layout()
plt.show()




#min max alpjha beta by myslf
import math


# Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.minmax = None


# Alpha-Beta function
def alpha_beta(node, depth, alpha, beta, isMax):
    # Base case (leaf node)
    if depth == 0 or not node.children:
        return node.value

    if isMax:
        value = -math.inf
        for child in node.children:
            value = max(value, alpha_beta(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)

            if beta <= alpha:
                print("Pruned:", child.value)
                break

    else:
        value = math.inf
        for child in node.children:
            value = min(value, alpha_beta(child, depth - 1, alpha, beta, True))
            beta = min(beta, value)

            if beta <= alpha:
                print("Pruned:", child.value)
                break

    node.minmax = value
    return value


# Build tree
root = Node('A')
B = Node('B');
C = Node('C')
root.children = [B, C]

D = Node('D');
E = Node('E')
F = Node('F');
G = Node('G')
B.children = [D, E]
C.children = [F, G]

D.children = [Node(2), Node(3)]
E.children = [Node(5), Node(9)]
F.children = [Node(0), Node(1)]
G.children = [Node(7), Node(5)]

# Run
alpha_beta(root, 3, -math.inf, math.inf, True)

# Output
print("\nMinimax Values:")
print("A:", root.minmax)
print("B:", B.minmax)
print("C:", C.minmax)
print("D:", D.minmax)
print("E:", E.minmax)
print("F:", F.minmax)
print("G:", G.minmax)


#alpha beta by tchr
import math

# Node class
class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []
        self.minmax_value = None


# Minimax Agent
class MinimaxAgent:
    def __init__(self, depth):
        self.depth = depth

    def formulate_goal(self, node):
        if node.minmax_value is not None:
            return "Goal reached"
        else:
            return "Searching"

    def act(self, node, environment):
        goal_status = self.formulate_goal(node)

        if goal_status == "Goal reached":
            return f"Minimax value for root node: {node.minmax_value}"
        else:
            return environment.alpha_beta_search(
                node, self.depth, -math.inf, math.inf, True
            )


# Environment class
class Environment:
    def __init__(self, tree):
        self.tree = tree
        self.computed_nodes = []

    def get_percept(self, node):
        return node

    def alpha_beta_search(self, node, depth, alpha, beta, maximizing_player=True):
        self.computed_nodes.append(node.value)

        # Base case
        if depth == 0 or not node.children:
            return node.value

        # Maximizing player
        if maximizing_player:
            value = -math.inf
            for child in node.children:
                value = max(
                    value,
                    self.alpha_beta_search(child, depth - 1, alpha, beta, False)
                )
                alpha = max(alpha, value)

                if beta <= alpha:
                    print("Pruned node:", child.value)
                    break

            node.minmax_value = value
            return value

        # Minimizing player
        else:
            value = math.inf
            for child in node.children:
                value = min(
                    value,
                    self.alpha_beta_search(child, depth - 1, alpha, beta, True)
                )
                beta = min(beta, value)

                if beta <= alpha:
                    print("Pruned node:", child.value)
                    break

            node.minmax_value = value
            return value


# Run agent
def run_agent(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    agent.act(percept, environment)


# ---------------- TREE CONSTRUCTION ----------------

root = Node('A')
n1 = Node('B')
n2 = Node('C')
root.children = [n1, n2]

n3 = Node('D')
n4 = Node('E')
n5 = Node('F')
n6 = Node('G')

n1.children = [n3, n4]
n2.children = [n5, n6]

# Leaf nodes
n3.children = [Node(2), Node(3)]
n4.children = [Node(5), Node(9)]
n5.children = [Node(0), Node(1)]
n6.children = [Node(7), Node(5)]

# ---------------- RUN ----------------

depth = 3
agent = MinimaxAgent(depth)
environment = Environment(root)

run_agent(agent, environment, root)

# ---------------- OUTPUT ----------------

print("Computed Nodes:", environment.computed_nodes)

print("\nMinimax values:")
print(f"A: {root.minmax_value}")
print(f"B: {n1.minmax_value}")
print(f"C: {n2.minmax_value}")
print(f"D: {n3.minmax_value}")
print(f"E: {n4.minmax_value}")
print(f"F: {n5.minmax_value}")
print(f"G: {n6.minmax_value}")

#csp1
from ortools.sat.python import cp_model

model = cp_model.CpModel() #craetee an empty csp model


#defining3 variabe
num_var = 3

x = model.new_int_var(0,num_var-1,"x")
y = model.new_int_var(0,num_var-1,"y")
z = model.new_int_var(0,num_var-1,"z")

model.add(x != y) #constraint

#solve amd check status
solver = cp_model.CpSolver()
status = solver.Solve(model)

#check if model find atleast one solution
if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
  print(f"x = {solver.value(x)}")
  print(f"y = {solver.value(y)}")
  print(f"z = {solver.value(z)}")
else:
    print("No solution found")

#csp2
from ortools.sat.python import cp_model
model = cp_model.CpModel()

var_num = max(30,20,25)
x = model.new_int_var(0,var_num,'x')
y = model.new_int_var(0,var_num,'y')
z = model.new_int_var(0,var_num,'z')

model.add(2*x + 5*y + 2 *z <= 40)
model.add(5*x + 10 *y + 2*z <= 50)
model.add(y <= 5)

model.maximize(2 *z + 5*y + 10*z)
solver = cp_model.CpSolver()
status = solver.solve(model)

if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
  print(f"objective value is {solver.objective_value}")
  print(f"x is {solver.value(x)}")
  print(f"y is {solver.value(y)}")
  print(f"z is {solver.value(z)}")
else:
  print("not found")

#csp3
from ortools.sat.python import cp_model

class Printer(cp_model.CpSolverSolutionCallback):
    def __init__(self, var_list):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.vars = var_list
        self.count = 0

    def on_solution_callback(self):
        self.count += 1
        for v in self.vars:
            print(f"{v} = {self.value(v)}", end=" ")
        print()

    @property
    def solution_count(self):
        return self.count


def solve_all():
    model = cp_model.CpModel()

    n = 3
    x = model.NewIntVar(0, n - 1, "x")
    y = model.NewIntVar(0, n - 1, "y")
    z = model.NewIntVar(0, n - 1, "z")

    model.Add(x != y)

    solver = cp_model.CpSolver()   # () missing before
    pri = Printer([x, y, z])

    solver.parameters.enumerate_all_solutions = True   # wrong name fixed
    status = solver.Solve(model, pri)   # Solve not solve

    print("status:", solver.StatusName(status))
    print("total:", pri.solution_count)


solve_all()

#csp4 n queens
import time
from ortools.sat.python import cp_model


# ---------------- PRINTER CLASS ----------------
class NQueenSolutionPrinter(cp_model.CpSolverSolutionCallback):
    def __init__(self, queens):
        super().__init__()
        self.queens = queens
        self.count = 0
        self.start = time.time()

    def on_solution_callback(self):
        print(f"\nSolution {self.count}, time = {time.time() - self.start:.2f}s")
        self.count += 1

        n = len(self.queens)

        for i in range(n):          # rows
            for j in range(n):      # columns
                if self.Value(self.queens[j]) == i:
                    print("Q", end=" ")
                else:
                    print("_", end=" ")
            print()
        print()


# ---------------- MAIN FUNCTION ----------------
def main():
    model = cp_model.CpModel()

    n = 4   # change n for different board sizes

    # Create variables
    queens = []
    for i in range(n):
        queens.append(model.NewIntVar(0, n - 1, f"q{i}"))

    # Constraints
    model.AddAllDifferent(queens)

    for i in range(n):
        for j in range(i + 1, n):
            model.Add(queens[i] - queens[j] != i - j)
            model.Add(queens[i] - queens[j] != j - i)

    # Solver
    solver = cp_model.CpSolver()
    solver.parameters.enumerate_all_solutions = True

    printer = NQueenSolutionPrinter(queens)

    solver.Solve(model, printer)

    print("Total solutions:", printer.count)

main()

# baysians network part1
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Step 1: Define structure
model = DiscreteBayesianNetwork([
    ('Burglary', 'Alarm'),
    ('Earthquake', 'Alarm'),
    ('Alarm', 'JohnCalls'),
    ('Alarm', 'MaryCalls')
])

# Step 2: Define CPDs

# P(Burglary)
cpd_burglary = TabularCPD(
    variable='Burglary',
    variable_card=2,
    values=[[0.999], [0.001]]
)

# P(Earthquake)
cpd_earthquake = TabularCPD(
    variable='Earthquake',
    variable_card=2,
    values=[[0.998], [0.002]]
)

# P(Alarm | Burglary, Earthquake)
cpd_alarm = TabularCPD(
    variable='Alarm',
    variable_card=2,
    values=[
        [0.999, 0.71, 0.06, 0.05],  # Alarm = False
        [0.001, 0.29, 0.94, 0.95]   # Alarm = True
    ],
    evidence=['Burglary', 'Earthquake'],
    evidence_card=[2, 2]
)

# P(JohnCalls | Alarm)
cpd_john = TabularCPD(
    variable='JohnCalls',
    variable_card=2,
    values=[
        [0.3, 0.9],  # False
        [0.7, 0.1]   # True
    ],
    evidence=['Alarm'],
    evidence_card=[2]
)

# P(MaryCalls | Alarm)
cpd_mary = TabularCPD(
    variable='MaryCalls',
    variable_card=2,
    values=[
        [0.2, 0.99],  # False
        [0.8, 0.01]   # True
    ],
    evidence=['Alarm'],
    evidence_card=[2]
)

# Step 3: Add CPDs
model.add_cpds(cpd_burglary, cpd_earthquake, cpd_alarm, cpd_john, cpd_mary)

# Step 4: Check model
assert model.check_model(), "Model is incorrect"

# Step 5: Inference
inference = VariableElimination(model)

# Query
result = inference.query(
    variables=['Burglary'],
    evidence={'JohnCalls': 1, 'MaryCalls': 1}
)

print(result)

#baysians network part 2

import numpy as np

# States
states = ["Red", "Blue"]

# Transition Matrix
transition_matrix = np.array([
    [0.5, 0.5],  # From Red
    [0.5, 0.5]   # From Blue
])

# Function to simulate Markov Process
def simulate_markov_process(initial_state, num_steps):
    current_state = initial_state
    state_sequence = [current_state]

    for _ in range(num_steps):
        if current_state == "Red":
            next_state = np.random.choice(states, p=transition_matrix[0])
        else:
            next_state = np.random.choice(states, p=transition_matrix[1])

        state_sequence.append(next_state)
        current_state = next_state

    return state_sequence


# Run simulation
initial_state = "Red"
num_steps = 10

sequence = simulate_markov_process(initial_state, num_steps)

print(f"State sequence for {num_steps} steps starting from {initial_state}:")
print(" -> ".join(sequence))
