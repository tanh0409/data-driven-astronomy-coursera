'''
Write a median_fits function which takes a list of FITS filenames, loads them into a NumPy array, and calculates the median image (where each pixel is the median of that pixel over every FITS file).
Your function should return a tuple of the median NumPy array, the time it took the function to run, and the amount of memory (in kB) used to store all the FITS files in the NumPy array in memory.
'''
import time, numpy as np
from astropy.io import fits

# Write your function median_FITS here:
def median_fits(files):
  # start timer here
  start = time.time()

  # read FITS files and store in list
  FITS_list = []
  for file in files:
    hdulist = fits.open(file)
    FITS_list.append(hdulist[0].data)
    hdulist.close()
  
  # stack image arrays in a 3D array to calculate median
  FITS_3D_arr = np.dstack(FITS_list)

  # median 
  median = np.median(FITS_3D_arr, axis=2)

  # memory needed 
  memory = FITS_3D_arr.nbytes

  # stop timer 
  stop = time.time() - start
  return median, stop, memory


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with first example in the question.
  result = median_fits(['image0.fits', 'image1.fits'])
  print(result[0][100, 100], result[1], result[2])
  
  # Run your function with second example in the question.
  result = median_fits(['image{}.fits'.format(str(i)) for i in range(11)])
  print(result[0][100, 100], result[1], result[2])