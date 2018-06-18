from scipy import misc
import matplotlib.pyplot as plt
import numpy as np

def read_img(path):
    """
    returns a numpy array containing the image
    """
    return misc.imread(path)

def show_img(img):
    height, width = img.shape
    # What size does the figure need to be in inches to fit the image?  
    dpi = 80
    figsize = width / float(dpi), height / float(dpi)
    
    fig = plt.figure(figsize=figsize)
    plt.imshow(img, cmap=plt.cm.gray)
    plt.show()
    return

    
def rgb2gray(rgb):
    return np.dot(rgb, [0.299, 0.587, 0.114])

def read_gray(path):
    return rgb2gray(misc.imread(path))


def show_histo(img_gray):
    temp1 = np.rint(img_gray)
    temp1 = np.reshape(temp1, (-1))

    import collections
    counter=collections.Counter(temp1)
    histogram = (list(counter.values()))

    import matplotlib.pyplot as plt
    plt.plot(histogram)
    plt.ylabel('some numbers')
    plt.show()

def get_avg( img, x, y ):
    suma = 0
    for i in range(x-2, x+3):
        for j in range(y-2, y+3):
            suma += img[i][j]
    return suma/(5*5)

def get5x5_mean(img_gray):
    mean_5x5 = np.array(img_gray)
    for i in range(2, len(mean_5x5) - 2):
        for j in range(2, len(img_gray[0]) - 2):
            mean_5x5[i][j] = get_avg( img_gray, i, j )
    return mean_5x5
