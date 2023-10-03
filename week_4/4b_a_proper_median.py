'''
Write a function called column_stats which calculates the mean and median of a selected column in either Star or Planet table. 

For this, let your function take two string arguments:
    the name of the table;
    the name of the column.
'''
import numpy as np
import psycopg2

def column_stats(table_name, col_name):
    cnx = psycopg2.connect(dbname='db', user='tan')
    cursor = cnx.cursor()

    query = 'SELECT ' + col_name + ' FROM ' + table_name + ';'
    cursor.execute(query)
    column = np.array(cursor.fetchall())
    return np.mean(column), np.median(column)