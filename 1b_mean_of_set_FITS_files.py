"""
Write a mean_fits function that takes a list of FITS files as an argument, reads them in, and returns the mean image data of the FITS files.
"""
from astropy.io import fits

# mean_fits function here

def mean_fits(files):
  n = len(files)
  if n > 0:
    hdulist = fits.open(files[0])
    data = hdulist[0].data
    hdulist.close()

    for i in range (1,n): 
      hdulist = fits.open(files[i])
      data += hdulist[0].data
      hdulist.close()

  mean = data / n
  return mean

if __name__ == '__main__':
  
  # Test your function with examples from the question
  data  = mean_fits(['image0.fits', 'image1.fits', 'image2.fits'])
  print(data[100, 100])
