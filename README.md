# Travel-Optimizer

In this Repo, I use MIP to find the shortest way to visit all European capitals. This is done in two steps:

1. Get all European Capitals and their geographical position (lattitude/longitude)
2. Optimize a MIP to find the shortest route to visit all capitals
3. Visualize the Route on a map using Plotly

## To Get Started

First create an environment (for example using conda) and install` the required packages from requirements.txt:

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

This create a CSV-file **EU_capitals.csv**.
