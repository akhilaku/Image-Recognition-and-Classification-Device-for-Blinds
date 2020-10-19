#Read and resize image[image size is defined during training]
img = print_img = skimage.io.imread(IMAGES_PATH);
img = skimage.transform.resize(img,IMAGE_DIM, preserve_range = True);
#Convert RGB to BGR [skimage reads image in RGB, but Caffe uses BGR]
img = img[:, :, ::-1];
#Mean subtraction and scaling [A common technique used to center the data]
img = img.astype(numpy.float32);
img = ( img - IMAGE_MEAN )*IMAGE_STDDEV;
