# Image-Classifier-using-Intel-Movidius-NCS-
This project is based on using Intel Movidius Neural Compute Stick (NCS) with Raspberry Pi-3 for Image Classification Application.
With the help of Intel Movidius NCS we can run any complex pre-trainet Networks in the processors with low processing capability.
This NCS functions as an efficient external processor for performing any complex neural architectures.

**Intel Movidius Neural Compute Stick(NCS)** can be used as an external GPU for the systems which cannot support for artificial intelligence based projects.
They are less-cost comparing other GPU's and can be used efficiently for most of the Deeo Learning, Machine Learning and Artificial Intelligence Based Projects 
![](https://github.com/akhilaku/Image-Classifier-using-Intel-Movidius-NCS-/blob/master/IMNCS.png)

**Overview / Usage**
The Intel Movidius Neural Compute Stick(NCS) is produced by Intel and can be run without an internet connection. This Movidius NCS's compute capability comes from its Myriad 2 Vision Processing Unit(VPU).

Profiling, tuning and compiling a DNN on a development computer with the tools are provided in the Intel and can be run without an Internet connection. The Movidius NCS's compute capability comes from its Myriad 2 VPU(Vision Processing Unit). Running Deep Learning (DL) models efficiently on a low capacity graphic processors is very difficult. Movidius allows us to optimize the operation of large models such as GoogleNet with multi-use support. It's an easy to use kit that allows you to design and implement applications such as **classification and object recognition** on physical products.

We can simply think of Movidius NCS's as a Graphic Processing Unit(GPU) running on a USB. Model training isn't performed on device, but a trained model can work optimally on the unit, which is intended to be used in physical environments for resting purposes.

Methodology / Approach
With the help of Intel Movidius Neural Compute USB Stick with Raspberry Pi-3 we are using it for image classification and an object recognizing application. The frameworks, standards, technique used are:

It can be used in **Ubuntu 16.04 **or Raspberry Pi-3.
It is compatible with two DNN frameworks such as **TensorFlow **and Caffe
Movidius Myriad 2 Vision Processing Unit(VPU) works with Caffe based Convolutional Neural Networks(CNN).
We can also run complex Deep Learning(DL) pre-trained models like GoogleNet, SqueezeNet, AlexNet on systems with low processing capability.
Approach:

It's very simple to run inference on an image classification demo model. We can use the NC App Zoo repo for classifying an image. We need to take the graph file to activate the application of the Movidius NCS. It has a compiled GoogleNet model for ready to run. This application needs some files. The **make command** is used for creating the files that Movidius needs as a graph file. The graph files is a demo of image-classifier.

**View the steps below for a quick application:**

**STEPS:**

**Step 01:** For using the property of the NCSDK API add (import) the mvnc library.

**Step 02:** You can access the Movidius NCS using an API like any other USB device. Also you can use parallel Movidius devices at once if you need more capacity to compute your model. For now, one kit is enough for this application. Select and open process.

**Step 03:** We will use a pre-trained GoogleNet model for using a compiled graph file.

**Step 04:** We also need to do some pre-processing before loading the image into our Movidius NCS.

**Step 05:** Use LoadTensor() to load the image into the Movidius.

**Step 06:** Give the input image to the pre-trained model and get the output by using GetResult().

**Step 07:** Print the prediction of the model's output and corresponding labels. Here we also display the input image at the same time.

**Step 08:** For the last step, we clear and shutdown the Movidius NCS device for using it again.

**Technologies Used**
Intel Technologies used(as external hardware):

Intel Movidius Neural Compute Stick

**Software used:**

Python 3 Software

**Hardware technology used other than Intel:**

Raspberry Pi-3

**Screenshots of image classifications and Recognitions**
![](https://github.com/akhilaku/Image-Classifier-using-Intel-Movidius-NCS-/blob/master/images(Screenshots)/Cat%20Variety%20Classification%20and%20Recognition.png)

![](https://github.com/akhilaku/Image-Classifier-using-Intel-Movidius-NCS-/blob/master/images(Screenshots)/Dog%20Variety%20Recognition.png)

![](https://github.com/akhilaku/Image-Classifier-using-Intel-Movidius-NCS-/blob/master/images(Screenshots)/Image%20Recognition%20in%20Linux(ubantu).png)

![](https://github.com/akhilaku/Image-Classifier-using-Intel-Movidius-NCS-/blob/master/images(Screenshots)/Hardware%20Setup.jpeg)
