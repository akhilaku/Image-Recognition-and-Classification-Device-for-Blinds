#Read the graph file into a buffer.
with open(GRAPH_PATH, mode = 'rb') as f:
    blob = f.read();
#Load the graph buffer into the NCS.
graph = device.AllocateGraph(blob);
