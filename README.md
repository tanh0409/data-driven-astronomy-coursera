# Data Driven Astronomy - Python & SQL Exercises

This repository contains exercises from the "Data Driven Astronomy" course offered by the University of Sydney

The schedule of the course and scope of each exercise are as follow:

1. Week 1 - Introduction to pulsars, numpy module, FITS files, and using stacking algorithms (mean and median) to detect pulsars

   1b - Exercises to find mean set of signals of FITS files to detect pulsars

   1c - Exercises to find median set of signals of FITS files to detect pulsars as median is a more robust statistic. Finding median can be heavily memory consuming so a more efficient algorithm to find an approximate median for larger datasets has been used.

2. Week 2 - Introduction to supermassive black holes and implementing cross-matching algorithm to combine radio and optical information to investigate how supermassive black holes regulate star formation

   2a - Exercise to import two different types of catalogues (AT20G BSS and SuperCOSMOS catalogues) and implement a crossmatching algorithm (simple for loop logic) to find out which were associated with the same physical object in space, to find closest matches within a given radius and their angular distance.
   NOTE: This is an inefficient algorithm as it can take a _very_ long time with bigger catalogues.

   2b - Exercise to crossmatch with k-d trees using the astropy module.

3. Week 3 - Introduction to exoplanets and use SQL to explore a database of exoplanets to determine how many earth sized exoplanets line the habitable zone of their host star.
