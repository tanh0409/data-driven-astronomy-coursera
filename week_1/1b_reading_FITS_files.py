"""
Write a load_fits function that loads in a FITS file and finds the position of the brightest pixel (i.e. the maximum value) in its image data.
"""
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

# load_fits function
def load_fits(filename):
  hdulist = fits.open(filename)
  data = hdulist[0].data
  max_index = np.argmax(data)
  # max position in coordinates
  max_coordinates = np.unravel_index(max_index, data.shape)
  return max_coordinates

if __name__ == '__main__':
  # Run your `load_fits` function with examples:
  bright = load_fits('image1.fits')
  print(bright)

  # You can also confirm your result visually:
  hdulist = fits.open('image1.fits')
  data = hdulist[0].data

  # Plot the 2D image data
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show() 
