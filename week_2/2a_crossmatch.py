'''
Write a crossmatch function that crossmatches two catalogues within a maximum distance.
It should return a list of matches and non-matches for the first catalogue against the second.
The list of matches contains tuples of the first and second catalogue object IDs and their distance. 
The list of non-matches contains the unmatched object IDs from the first catalogue only.
Both lists should be ordered by the first catalogue's IDs.

The BSS and SuperCOSMOS catalogues will be given as input arguments, each in the format you've seen previously. 
The maximum distance is given in decimal degrees

'''
# Write your crossmatch function here.
import numpy as np

def hms2dec(hr, m, s):
  right_ascension = 15 * (hr + m/60 + s/3600)
  return right_ascension

def dms2dec(deg, m, s):
  sign = deg/abs(deg)
  declination = abs(deg) + m/60 + s/3600
  return declination*sign

def import_bss():
  cat =[]
  data = np.loadtxt('bss.dat', usecols=range(1,7))
  for i, row in enumerate(data, 1):
    cat.append((i, hms2dec(row[0], row[1], row[2]), dms2dec(row[3], row[4], row[5])))
  return cat

def import_super():
  cat = []
  data = np.loadtxt('super.csv', delimiter=',', skiprows=1, usecols=[0, 1])
  for i, row in enumerate(data, 1):
    cat.append((i, row[0], row[1]))
  return cat

def angular_distance(ra1, dec1, ra2, dec2):
   # convert to radians for numpy trig functions 
   d1 = np.radians(dec1)
   d2 = np.radians(dec2)
   r1 = np.radians(ra1)
   r2 = np.radians(ra2)
   a = np.sin(np.abs(d1 - d2)/2)**2
   b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1 - r2)/2)**2
   d = 2*np.arcsin(np.sqrt(a + b))
   # convert back to decimal degrees
   d = np.degrees(d)
   return d

def crossmatch(cat1, cat2, max_radius):
  matches = []
  no_matches= []
  for id1, ra1, dec1 in cat1:
    closest_distance = np.inf
    closest_id2 = None
    for id2, ra2, dec2 in cat2:
      distance = angular_distance(ra1, dec1, ra2, dec2)
      if distance < closest_distance:
        closest_id2 = id2
        closest_distance = distance
    if closest_distance > max_radius:
      no_matches.append(id1)
    else:
      matches.append((id1, closest_id2, closest_distance))
  
  return matches, no_matches


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  bss_cat = import_bss()
  super_cat = import_super()

  # First example in the question
  max_dist = 40/3600
  matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  print(matches[:3])
  print(no_matches[:3])
  print(len(no_matches))

  # Second example in the question
  max_dist = 5/3600
  matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  print(matches[:3])
  print(no_matches[:3])
  print(len(no_matches))
