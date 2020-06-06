# Image-Classifier-using-Intel-Movidius-NCS-2

**This project is based on helping the blind people to identify, recognize and classify the things in front of them using Intel Movidius Neural Compute Stick(NCS) with Raspberry Pi-3.**

**The project is developed till its image recognition and classification process, and I'm under developing its classified image text to speech process so that Blind people can know what is in front of them through their earphones connected to the device.**
With the help of Intel Movidius NCS we can run any complex pre-trainet Networks in the processors with low processing capability.
This NCS functions as an efficient external processor for performing any complex neural architectures.

**Intel Movidius Neural Compute Stick(NCS)** can be used as an **external GPU** for the systems which cannot support for artificial intelligence based projects.
They are less-cost comparing other GPU's and can be used efficiently for most of the Deeo Learning, Machine Learning and Artificial Intelligence Based Projects 
![](https://github.com/akhilaku/Image-Classifier-using-Intel-Movidius-NCS-/blob/master/IMNCS.png)

## Overview / Usage

The Intel Movidius Neural Compute Stick(NCS) is produced by Intel and can be run without an internet connection. This Movidius NCS's compute capability comes from its Myriad 2 Vision Processing Unit(VPU).

Profiling, tuning and compiling a DNN on a development computer with the tools are provided in the Intel and can be run without an Internet connection. The Movidius NCS's compute capability comes from its **Myriad 2 VPU(Vision Processing Unit)**. Running Deep Learning (DL) models efficiently on a low capacity graphic processors is very difficult. Movidius allows us to optimize the operation of large models such as GoogleNet with multi-use support. It's an easy to use kit that allows you to design and implement applications such as **classification and object recognition** on physical products.

We can simply think of Movidius NCS's as a Graphic Processing Unit(GPU) running on a USB. Model training isn't performed on device, but a trained model can work optimally on the unit, which is intended to be used in physical environments for resting purposes.

## Methodology / Approach

With the help of Intel Movidius Neural Compute USB Stick with Raspberry Pi-3 we are using it for image classification and an object recognizing application. The frameworks, standards, technique used are:

It can be used in Ubuntu 16.04 or Raspberry Pi-3.
It is compatible with two DNN frameworks such as **TensorFlow** and **Caffe**
Movidius Myriad 2 Vision Processing Unit(VPU) works with Caffe based Convolutional Neural Networks(CNN).
We can also run complex Deep Learning(DL) pre-trained models like GoogleNet, SqueezeNet, AlexNet on systems with low processing capability.

## Approach:

It's very simple to run inference on an image classification demo model. We can use the NC App Zoo repo for classifying an image. We need to take the graph file to activate the application of the Movidius NCS. It has a compiled GoogleNet model for ready to run. This application needs some files. The **make command** is used for creating the files that Movidius needs as a graph file. The graph files is a demo of image-classifier.

**View the steps below for a quick application:**

**STEPS:**

1. **Step 01:** For using the property of the NCSDK API add (import) the mvnc library.

    ```python
       import mvnc.mvncapi as mvnc

1. **Step 02:** You can access the Movidius NCS using an API like any other USB device. Also you can use parallel Movidius devices at once if you need more capacity to compute your model. For now, one kit is enough for this application. Select and open process.
    ```python
       #then look for the enumerated Intel Movidius NCS Device();quite program if none found.
       devices = mvnc.EnumerateDevice();
       if len(devices) == 0:
           print("No any Devices found");
           quit;
       #Now get a handle to the first enumerated device and open it.
       device = mvnc.Device(devices[0]);
       device.OpenDevice();

1. **Step 03:** We will use a pre-trained GoogleNet model for using a compiled graph file.
    ```python
       #Read the graph file into a buffer.
       with open(GRAPH_PATH, mode = 'rb') as f:
           blob = f.read();
       #Load the graph buffer into the NCS.
       graph = device.AllocateGraph(blob);

1. **Step 04:** We also need to do some pre-processing before loading the image into our Movidius NCS.
    ```python
       #Read and resize image[image size is defined during training]
       img = print_img = skimage.io.imread(IMAGES_PATH);
       img = skimage.transform.resize(img,IMAGE_DIM, preserve_range = True);
       #Convert RGB to BGR [skimage reads image in RGB, but Caffe uses BGR]
       img = img[:, :, ::-1];
       #Mean subtraction and scaling [A common technique used to center the data]
       img = img.astype(numpy.float32);
       img = ( img - IMAGE_MEAN )*IMAGE_STDDEV;

1. **Step 05:** Use LoadTensor() to load the image into the Movidius.
    ```python
       #Load the image as a half-precision floating point array.
       graph.LoadTensor( img.astype( numpy.float16 ), 'user object' );

1. **Step 06:** Give the input image to the pre-trained model and get the output by using GetResult().
    ```python
       #Get the results from NCS
       output, userobj = graph.GetResult();

1. **Step 07:** Print the prediction of the model's output and corresponding labels. Here we also display the input image at the same time.
    ```python
       #Print the results
       print('\n ----predictions----');
       labels = numpy.loadtxt(LABELS_FILE_PATH,str,delimiter = '\t');
       order = output.argsort()[::-1][:6];
       for i in range(0,5):
         print ('prediction' + str(i) 'is' + labels[order[i]));
       #Display the image on which inference was performed
       skimage.io.imshow(IMAGES_PATH);
       skimage.io.show();

1. **Step 08:** For the last step, we clear and shutdown the Movidius NCS device for using it again.
    ```python
       #For clear and shutdowning the Movidius NCS device for using it gain.
       graph.DeallocateGraph;
       device.CloseDevice();

---

## Technologies Used
Intel Technologies used **(as external hardware):**

   **Intel Movidius Neural Compute Stick**

---

## Software used:

   **Python 3 Software**
 
---

## Hardware technology used other than Intel:

   **Raspberry Pi-3**
   
---

## Screenshots of image classifications and Recognitions

![](https://github.com/akhilaku/Image-Classifier-using-Intel-Movidius-NCS-/blob/master/images(Screenshots)/Cat%20Variety%20Classification%20and%20Recognition.png)

---

![](https://github.com/akhilaku/Image-Classifier-using-Intel-Movidius-NCS-/blob/master/images(Screenshots)/Dog%20Variety%20Recognition.png)

---

## Project done in Linux(Ubuntu) Operating System

![](https://github.com/akhilaku/Image-Classifier-using-Intel-Movidius-NCS-/blob/master/images(Screenshots)/Image%20Recognition%20in%20Linux(ubantu).png)

---

![](https://github.com/akhilaku/Image-Classifier-using-Intel-Movidius-NCS-/blob/master/images(Screenshots)/Hardware%20Setup.jpeg)

---

### Project Admin

| ![](https://github.com/akhilaku/Image-Classifier-using-Intel-Movidius-NCS-2/blob/master/akhildasKs%20(2).jpg) |
| :------------------------: |
| **AKHILDAS KS**  |

![GitHub followers](https://img.shields.io/github/followers/akhilaku.svg?label=Follow%20@akhilaku&style=social) [![Twitter Follow](https://img.shields.io/twitter/follow/KsAkhildas?style=social)](https://twitter.com/KsAkhildas)

[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/akhilaku/)

![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)

---
