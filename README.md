# Travel-Optimizer

In this Repo, I use MIP to find the shortest way to visit all European capitals. This is done in three steps:

1. Get all European capitals and their geographical position (lattitude/longitude)
2. Define and optimize a MIP model to find the shortest route to visit all capitals
3. Visualize the route on a map using Plotly

## To Get Started

First create an environment (for example using conda) and install the required packages from requirements.txt:

```
conda create --name [environment_name]
conda activate [environment_name]
conda install --file requirements.txt
```

To have the Plotly figures working in JupyterLab, you need to run:

```
jupyter labextension install @jupyter-widgets/jupyterlab-manager@1.1 --no-build
jupyter labextension install jupyterlab-plotly@4.6.0 --no-build
jupyter labextension install plotlywidget@4.6.0 --no-build
jupyter lab build
```

## To Get Data
To get a list of all European capitals with their geographical position (lattitude/longitude), you need to run the data_retrieval.py file:

```
python data_retrieval.py
```

This creates a CSV-file **EU_capitals.csv**.


## To Optimize the Model
The model can be found in **travel_europe.ipynb**.
The start and end point can be changed in the file:

```
start = 'Iceland'
end = 'Cyprus'
```

### Calulcate Distance Matrix
The Distance Matrix is calculated for all European capitals:

```python
dist = [[distance.distance((df.lat[i],df.long[i]),(df.lat[j],df.long[j])).km for j in range(len(df))] for i in range(len(df))]
```

### Define Model and Constraints
1. X represents a matrix of zeros and ones, which indicates if a vertix between two nodes/capitals (i,j) exists (=1) or not (=0)
2. Y represents a list of numbers, which indicate the 'traveling'-sequence of the nodes/capitals.

objective: the 'traveling'-route should have a minimized distance

contraints: 
- each node should only be entered once (except starting node is entered zero times)
- each node should only be left once (except end point is left zero times)
- it should be one route and no subroutes

```python
from itertools import product
from mip import Model, xsum, minimize, BINARY

n = len(dist) 
V = set(range(len(dist)))

model = Model()

x = [[model.add_var(var_type=BINARY) for j in V] for i in V]

y = [model.add_var() for i in V]

model.objective = minimize(xsum(dist[i][j]*x[i][j] for i in V for j in V))

for i in V-{id_end}:
    model += xsum(x[i][j] for j in V - {i}) == 1

for i in V-{0}:
    model += xsum(x[j][i] for j in V - {i}) == 1

for (i, j) in product(V - {0}, V - {0}):
    if i != j:
        model += y[i] - (n+1)*x[i][j] >= y[j]-n

model.optimize()
```


## To Visualize the Route
Ploty Scattermapbox is used to visualize the optimized route:

```python
import plotly
import plotly.graph_objects as go

fig = go.Figure(go.Scattermapbox(
    mode = "markers+lines",
    text = df.loc[order].capital,
    lon = df.loc[order].long,
    lat = df.loc[order].lat,
    marker = {'size': 10}))

fig.update_layout(
    margin ={'l':0,'t':0,'b':0,'r':0},
    mapbox = {
        'center': {'lon': df['long'].mean(), 'lat': df['lat'].mean()},
        'style': "stamen-terrain",
        'zoom': 2.3})
```
The results are shown here:

![alt text](assets/example.png "Example Route (Iceland-Cyprus)")