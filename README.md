# **Image Recognition and Classification Device for Blind People**

## **STUDENT CODE-IN**

### **About Student Code-In** 

**[Student Code-In](https://scodein.tech) is a global program that helps students grow with Open Source. It is a 2 months long Open-Source initiative which provides you the best platform to improve your skills and abilities by contributing to vast variety of Open Source Projects. In this, all the registered participants would get an exquisite opportunity to interact with the mentors and the Organizing Team.**

<p align="center">
  <kbd><img src="https://github.com/StudentCode-in/Image-Recognition-and-Classification-Device-for-Blind-People/blob/master/images/Student%20Code-In%20logo.jpg" ></kbd>
  </p>

---

**Project idea is to implement an image recognition and classification device in their pocket with a camera in spectacles of blind people, so that it can recognize and classify the things (visuals) in front of them. It also helps to identify the people in front of them with the help of face recognition. The classified or recognized image will be converted into speech so that the Blinds can listen and understand what is in front of them with the help of a headset.**

<p align="center">
<kbd><img src=https://github.com/akhilaku/Image-Recognition-and-Classification-Device-for-Blind-People/blob/master/images/Project-Theme.jpg width=800 height=369 /></kbd>
  </p>
  
**The project is developed till its image recognition and classification process, and I'm under developing its classified image text to speech process so that Blind people can know what is in front of them through their earphones connected to the device.**
With the help of Intel Movidius NCS we can run any complex pre-trainet Networks in the processors with low processing capability.
This NCS functions as an efficient external processor for performing any complex neural architectures.

**Intel Movidius Neural Compute Stick(NCS)** can be used as an **external GPU** for the systems which cannot support for artificial intelligence based projects.
They are less-cost comparing other GPU's and can be used efficiently for most of the Deep Learning, Machine Learning and Artificial Intelligence Based Projects 

---

## 🚩  Vision
### Goals of this project:
- **To reduce the difficulties faced by the blind people in their daily life** by creating a device which will tell them what is in front of them(includes identifying the people in front of them using Face recognition)
- **To make the blind people forget about their disabilities.**

---

### Hardware component required for this projects:

- [**Intel Movidius Neural Compute Stick(NCS) 2**](https://software.intel.com/content/www/us/en/develop/hardware/neural-compute-stick.html)
- [**Raspberry pi-3** ](https://www.raspberrypi.org/documentation/)
- [**Raspberry pi-camera**](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/8)
- **Headset-** Click [here](https://www.hackster.io/youness/connect-bluetooth-headset-to-raspberry-pi-3-a2dp-and-hsp-56ec2f) to see how to connect your headset with Raspberry Pi-3.
- **Power-Bank**

### Softwares Requirements:

- **Python**- Click [here](https://www.python.org/downloads/) to download
- **OpenVino Tool Kit**- Click [here](https://software.seek.intel.com/openvino-toolkit?cid=diad&source=hackster&campid=WW_Q2_2020_IoTG-DE_OpenVI%20NO-DA&content=dev-challenge) to download

---

## Building the main part "Image Recognition and Classification System"

<p align="center">
<kbd><img src=https://github.com/akhilaku/Image-Recognition-and-Classification-Device-for-Blind-People/blob/master/images/IMNCS.png width=800 height=369 /></kbd>
  </p>
  
### Overview / Usage

The **Intel Movidius Neural Compute Stick(NCS)** is produced by Intel and can be run without an internet connection. This Movidius NCS's compute capability comes from its Myriad 2 Vision Processing Unit(VPU).

Profiling, tuning and compiling a DNN on a development computer with the tools are provided in the Intel and can be run without an Internet connection. The Movidius NCS's compute capability comes from its **Myriad 2 VPU(Vision Processing Unit)**. Running Deep Learning (DL) models efficiently on a low capacity graphic processors is very difficult. Movidius allows us to optimize the operation of large models such as GoogleNet with multi-use support. It's an easy to use kit that allows you to design and implement applications such as **classification and object recognition** on physical products.

We can simply think of Movidius NCS's as a Graphic Processing Unit(GPU) running on a USB. Model training isn't performed on device, but a trained model can work optimally on the unit, which is intended to be used in physical environments for resting purposes.

## Methodology / Approach

With the help of Intel Movidius Neural Compute USB Stick with Raspberry Pi-3 we are using it for image classification and an object recognizing application. The frameworks, standards, technique used are:

It can be used in **Ubuntu 16.04 or Raspberry Pi-3.**
It is compatible with two **DNN frameworks** such as **TensorFlow** and **Caffe**
Movidius Myriad 2 Vision Processing Unit(VPU) works with Caffe based Convolutional Neural Networks(CNN).
We can also run complex Deep Learning(DL) pre-trained models like **GoogleNet, SqueezeNet, AlexNet** on systems with low processing capability.

## Approach:

It's very simple to run inference on an image classification demo model. We can use the NC App Zoo repo for classifying an image. We need to take the graph file to activate the application of the Movidius NCS. It has a compiled GoogleNet model for ready to run. This application needs some files. The **make command** is used for creating the files that Movidius needs as a graph file. The graph files is a demo of image-classifier.

**View the steps below for a quick application:**

**STEPS:**

1. **Step 01:** For using the property of the NCSDK API add (import) the mvnc library.

    ```python
       import mvnc.mvncapi as mvnc

1. **Step 02:** You can access the Movidius NCS using an API like any other USB device. Also you can use parallel Movidius devices at once if you need more capacity to compute your model. For now, one kit is enough for this application. Select and open process.
    ```python
       #then look for the enumerated Intel Movidius NCS Device(), quit program if none found.
       devices = mvnc.EnumerateDevice();
       if len(devices) == 0:
           print("No Devices Found");
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
       #For clear and shutting down the Movidius NCS device for using it again.
       graph.DeallocateGraph();
       device.CloseDevice();
       
---

### Getting Started

**1.** Fork [this](https://github.com/StudentCode-in/Image-Recognition-and-Classification-Device-for-Blind-People) repository.
Click on the <a href="https://github.com/StudentCode-in/Image-Recognition-and-Classification-Device-for-Blind-People/"><img src="https://img.icons8.com/ios/24/000000/code-fork.png"></a> symbol at the top right corner.

**2.** Clone the forked repository.

```bash
git clone https://github.com/<your-github-username>/Image-Recognition-and-Classification-Device-for-Blind-People-Using-Intel-NCS-2.git
```

**3.** Navigate to the project directory.

```bash
cd Image-Recognition-and-Classification-Device-for-Blind-People-Using-Intel-NCS-2/
```

**4.** Create a new branch.

```bash
git checkout -b <your_branch_name>
```

**5.** Make changes in source code.

**6.** Add your changes and commit

```bash
#Add changes to Index
git add .

#Commit to the local repo
git commit -m "<your_commit_message>"
```
**7.** Push your local commits to your repository.

```bash
git push -u origin <your_branch_name>
```
#### Create a Pull-Request(PR) to merge your changes into the original repository(write a simple description about the changes you made)

---

### :warning:  Issues

Always feel free to **file a new issue** with a respective title and description on the [Image-Recognition-and-Classification-Device-for-Blind-People-Using-Intel-NCS-2](https://github.com/akhilaku/Image-Recognition-and-Classification-Device-for-Blind-People-Using-Intel-NCS-2/issues) repository.

### :handshake:  Contribution

If you have any great ideas which can make this project more better, you can make changes and send me a Pull Request(PR) with a respective title and description on the [Image-Recognition-and-Classification-Device-for-Blind-People-Using-Intel-NCS-2](https://github.com/akhilaku/Image-Recognition-and-Classification-Device-for-Blind-People-Using-Intel-NCS-2) repository, I will definitely review your pull request.

---
  
### Project Admin

| ![](https://github.com/akhilaku/Image-Recognition-and-Classification-Device-for-Blind-People-Using-Intel-NCS-2/blob/master/akhildasKs%20(2).jpg) |
| :------------------------: |
| **AKHILDAS KS**  |

[![GitHub followers](https://img.shields.io/github/followers/akhilaku.svg?label=Follow%20@akhilaku&style=social)](https://github.com/akhilaku/) [![Twitter Follow](https://img.shields.io/twitter/follow/KsAkhildas?style=social)](https://twitter.com/KsAkhildas)

[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/akhildasks/)

![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)

---

## Contributors ✨



<table>
  <tr>
    <td align="center"><a href="https://www.linkedin.com/in/ashwini-jha-259147159/"><img src="https://github.com/akhilaku/Image-Recognition-and-Classification-Device-for-Blind-People-Using-Intel-NCS-2/blob/master/Ashwini.jpg" width="150px;" alt="https://github.com/ashwinijha6"/><br /><sub><b>Ashwini Jha</b></sub></a><br /><a href="https://github.com/ashwinijha6/Image-Recognition-and-Classification-Device-for-Blind-People-Using-Intel-NCS-2.git" title="Code">Repo Link</a><br /></td>
    <td align="center"><a href="https://www.linkedin.com/in/bhanvi-menghani/"><img src="https://github.com/akhilaku/Image-Recognition-and-Classification-Device-for-Blind-People-Using-Intel-NCS-2/blob/master/Bhanvi.jpg" width="150px;" alt="https://github.com/bhanvimenghani"/><br /><sub><b>Bhanvi Menghani</b></sub></a><br /><a href="https://github.com/bhanvimenghani/Image-Recognition-and-Classification-Device-for-Blind-People-Using-Intel-NCS-2.git" title="Code">Repo Link</a></td>
   
  </tr>
</table>

[![GitHub followers](https://img.shields.io/github/followers/ashwinijha6.svg?label=Follow%20@ashwinijha6&style=social)](https://github.com/ashwinijha6/) [![GitHub followers](https://img.shields.io/github/followers/bhanvimenghani.svg?label=Follow%20@bhanvimenghani&style=social)](https://github.com/bhanvimenghani/)







