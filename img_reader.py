from scipy import misc
import matplotlib.pyplot as plt

def read_img(path):
    """
    returns a numpy array containing the image
    """
    return misc.imread(path)

def show_img(img):
    plt.imshow(img, cmap=plt.cm.gray)
    plt.show()
