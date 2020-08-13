#then look for the enumerated Intel Movidius NCS Device();quite program if none found.
devices = mvnc.EnumerateDevice();
if len(devices) == 0:
    print("No any Devices found");
    quit;
#Now get a handle to the first enumerated device and open it.
device = mvnc.Device(devices[0]);
device.OpenDevice();
