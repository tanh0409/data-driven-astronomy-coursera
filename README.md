# Data Driven Astronomy - Python & SQL Exercises

This repository contains exercises from the "Data Driven Astronomy" course offered by the University of Sydney

The schedule of the course and scope of each exercise are as follow:

1. Week 1 - Introduction to pulsars, numpy module, FITS files, and using stacking algorithms (mean and median) to detect pulsars

   - 1b - Exercises to find mean set of signals of FITS files to detect pulsars

   - 1c - Exercises to find median set of signals of FITS files to detect pulsars as median is a more robust statistic. Finding median can be heavily memory consuming so a more efficient algorithm to find an approximate median for larger datasets has been used.

2. Week 2 - Introduction to supermassive black holes and implementing cross-matching algorithm to combine radio and optical information to investigate how supermassive black holes regulate star formation

   - 2a - Exercise to import two different types of catalogues (AT20G BSS and SuperCOSMOS catalogues) and implement a crossmatching algorithm (simple for loop logic) to find out which were associated with the same physical object in space, to find closest matches within a given radius and their angular distance.
     NOTE: This is an inefficient algorithm as it can take a _very_ long time with bigger catalogues.

   - 2b - Exercise to crossmatch with k-d trees using the astropy module.

3. Week 3 - Introduction to exoplanets and use SQL to explore a database of exoplanets to determine how many earth sized exoplanets line the habitable zone of their host star.

4. Week 4 - Introduction to the lifecycle of stars and set up a database to store combined Hypothos data with cluster membership list for VizieR which will give the probability of each star being physically asssociated with that cluster.

   - A schema to represent the data is also designed as part of the exercises of this week.
   - This week's exercises also involve combining SQL and Python.

5. Week 5 - Introduction to cosmological distances and methods of calculating them (parallax, red shift), and using machine learning to determine the redshifts of galaxies from their photometric colours.

   - 5a - Exercises to build a regression classifier using decision tree algorithms and make colour-colour redshift plot.

   - 5b - Exercises to validate and improve algorithms from 5a exercises (using k-fold cross validation, constraining tree depth to account for overfitting) to estimate redshifts using regression.

6. Week 6 -
