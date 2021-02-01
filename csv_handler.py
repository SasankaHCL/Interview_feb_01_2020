#Author: sj.sasanka@gmail.com
#Date  : 01 Feb 2021
#This script is going to merg all the csv files.
#As data sorting is not specefied in requirement and can be achive easily.
###########################################################################
import pandas as pd
import glob
Output_file = 'Unified_csv.csv'

def get_all_csv():
    """
    'Unified_csv.csv' : Output file
    all_files : return list of csv files
    This function is going to feth all the csv file from the
    current directory excluded by 'Unified_csv.csv'.
    It will take n number of csv files as input.
    """
    all_files = []
    for files in glob.glob("*.csv"):
        if not files.startswith('Unified'):
            all_files.append(files)
    return (all_files)


if __name__ == '__main__':
    combined_csv = pd.concat( [ pd.read_csv(f) for f in get_all_csv() ] )
    combined_csv.to_csv( Output_file, index=False )
