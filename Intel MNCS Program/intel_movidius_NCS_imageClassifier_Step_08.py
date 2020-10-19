#For claer and shutdowning the Movidius NCS device for using it gain.
graph.DeallocateGraph();
device.CloseDevice();
