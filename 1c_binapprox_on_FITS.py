'''
Use the binapprox algorithm to efficiently estimate the median of each pixel from a set of astronomy images in FITS files.
Write median_bins_fits and median_approx_fits functions that take a list of FITS filenames and the number of bins. 
Your task is to write two functions:
    1. median_bins to calculate the mean, standard deviation and the bins (steps 1-6 on the previous slide);
    2. median_approx which calls median_bins and then calculates the approximated median (steps 7-8).

To calculate the mean and standard deviation of the FITS files, we've given you a running_stats helper function which calculates them in a single pass without holding the images in memory. It returns a tuple of the mean and standard deviation.
'''

import numpy as np
from astropy.io import fits
from helper import running_stats


def median_bins_fits(files, B):
  # Calculate the mean and standard dev using function in helper.py
  mean, std = running_stats(files)
    
  dim = mean.shape # Dimension of the FITS file arrays
    
  # Initialise bins
  left_bin = np.zeros(dim)
  bins = np.zeros((dim[0], dim[1], B))
  width = 2 * std / B 

  # Loop over all FITS files
  for file in files:
      hdulist = fits.open(file)
      data = hdulist[0].data

      # Loop over every point in the 2D array
      for i in range(dim[0]):
        for j in range(dim[1]):
          value = data[i, j]
          mean_ = mean[i, j]
          std_ = std[i, j]

          if value < mean_ - std_:
            left_bin[i, j] += 1
                
          elif value >= mean_ - std_ and value < mean_ + std_:
            bin = int((value - (mean_ - std_))/width[i, j])
            bins[i, j, bin] += 1

  return mean, std, left_bin, bins


def median_approx_fits(files, B):
  mean, std, left_bin, bins = median_bins_fits(files, B)
    
  dim = mean.shape # Dimension of the FITS file arrays
  
  n = len(files)
  midpoint = (n + 1)/2
	
  width = 2*std / B
  # Calculate the approximated median for each array element
  median = np.zeros(dim)   
  for i in range(dim[0]):
    for j in range(dim[1]):    
      count = left_bin[i, j]
      for b, bincount in enumerate(bins[i, j]):
        count += bincount
        if count >= midpoint:
          # Stop when the cumulative count exceeds the midpoint
          break
      median[i, j] = mean[i, j] - std[i, j] + width[i, j]*(b + 0.5)
      
  return median

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with examples from the question.
  mean, std, left_bin, bins = median_bins_fits(['image0.fits', 'image1.fits', 'image2.fits'], 5)
  median = median_approx_fits(['image0.fits', 'image1.fits', 'image2.fits'], 5)
