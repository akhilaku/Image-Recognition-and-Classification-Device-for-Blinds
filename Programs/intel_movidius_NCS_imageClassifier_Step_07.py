#Print the results
print('\n ----predictions----');
labels = numpy.loadtxt(LABELS_FILE_PATH,str,delimiter = '\t');
order = output.argsort()[::-1][:6];
for i in range(0,5);
print ('prediction' + str(i) 'is' + labels[order[i]));
#Display the image on which inference was performed
skimage.io.imshow(IMAGES_PATH);
skimage.io.show();
