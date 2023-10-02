'''
We can improve on the previous algorithm further by stopping the search once it gets past declination of the object to be matched and by starting the search as close as possible to the object.
To summarise, the modification is:
    - Sort the second catalogue objects by order of declination;
    - Start the search loop at the first second catalogue object with declination greater than delta - max_radius
    - Finish the search loop at the last second catalogue object with declination less than delta + max_radius

If a list is sorted, it can be much faster to find the index of some element using a binary search, rather than doing comparisons on every element in the list.

A binary search splits the list in half repeatedly, continuing the search in the half that may contain the target element.

NumPy provides binary search with the searchsorted function

Rather than searching for a specific element, searchsorted finds the insertion position of the target (actually the index after) that would maintain the sorted order

Modify your crossmatch function to loop through objects in the second catalogue with declinations between dec1 - max_radius and dec1 + max_radius using binary search
'''

# Write your crossmatch function here.
import time, numpy as np

def angular_distance(r1, d1, r2, d2):
  a = np.sin(np.abs(d1 - d2)/2)**2
  b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1 - r2)/2)**2
  return 2*np.arcsin(np.sqrt(a + b))

def crossmatch(cat1, cat2, max_radius):
  start_time = time.perf_counter()
  max_radius = np.radians(max_radius)

  matches = []
  no_matches = []

  cat1 = np.radians(cat1)
  cat2 = np.radians(cat2)

  # find ascending declination order of second catalogue 
  asc_dec_cat2 = np.argsort(cat2[:,1]) # ordered by declination
  cat2_sorted = cat2[asc_dec_cat2]
  dec2_sorted = cat2_sorted[:,1]

  for id1, (ra1, dec1) in enumerate(cat1):
    min_distance = np.inf
    min_id2 = None

    # declination search box 
    min_dec = dec1 - max_radius
    max_dec = dec1 + max_radius

    # start and end indices of the search 
    start = dec2_sorted.searchsorted(min_dec, side ='left')
    end = dec2_sorted.searchsorted(max_dec, side = 'right')

    for s_id2, (ra2, dec2) in enumerate(cat2_sorted[start:end+1], start):
      distance = angular_distance(ra1, dec1, ra2, dec2)
      if distance < min_distance:
        min_sorted_id2 = s_id2
        min_distance = distance  
    if min_distance > max_radius:
      no_matches.append(id1)
    else:
      min_id2 = asc_dec_cat2[min_sorted_id2]
      matches.append((id1, min_id2, np.degrees(min_distance)))

  time_taken = time.perf_counter() - start_time
  return matches, no_matches, time_taken
