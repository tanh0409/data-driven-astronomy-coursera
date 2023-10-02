'''
Copy the optimised crossmatch solution from the previous exercise and modify it to use Astropy to perform the matching
'''

from astropy.coordinates import SkyCoord
from astropy import units as u
from time import time

def crossmatch(coords1, coords2, max_radius):
    start_time = time()
    matches = []
    no_matches = []

    # convert to astropy coordinates objects 
    cat1 = SkyCoord(coords1*u.degree, frame='icrs')
    cat2 = SkyCoord(coords2*u.degree, frame='icrs')

    # perform cross matching
    closest_ids, closest_distances, _ = cat1.match_to_catalog_sky(cat2)

    for id1, (closest_id2, distance) in enumerate(zip(closest_ids, closest_distances)):
        closest_distance = distance.value
        if closest_distance > max_radius:
            no_matches.append(id1)
        else:
            matches.append([id1, closest_id2, closest_distance])
    time_taken = time() - start_time
    return matches, no_matches, time_taken