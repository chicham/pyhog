from skimage import io
from skimage.util import img_as_float
import numpy as np
from pyhog import features_pedro, pyhog, hog_picture
import numpy as np


def main():
    img = img_as_float(io.imread("2007_006449.jpg"))
    fh = pyhog.hog_feature(img, 4)
    print fh.shape
    pic = hog_picture(fh)
    pic = (pic - pic.min()) / (pic.max() - pic.min())
    io.imsave("fh.jpg", pic)

if __name__ == '__main__':
    main()
