import os
import sys
import pydicom
import subprocess
import numpy as np

from itertools import chain

def os_command(command):
    sp = subprocess.Popen(["/bin/bash", "-i", "-c", command])
    sp.communicate()

if __name__ == "__main__":
  
    # retrieve the dicom path
    try:
    
        if len(sys.argv) < 2:
            raise IndexError("No dicom-path provided.")

        dicom_path = sys.argv[1]

    except IndexError as e:
        print("Error: ", e)

    
    # get the series
    series = np.array([[(os.path.join(dp, f),  pydicom.dcmread(os.path.join(dp, f), stop_before_pixels =True)) for f in files]
                         for dp, _, files in os.walk(dicom_path) if len(files) != 0])

    # check the different series
    series_desc = [s[0][1].SeriesDescription for s in series]
    
    print(f"List of series: {series_desc}")

    # retrieve FLAIR series
    flair_series = [s for s in series if "FLAIR" in s[0][1].SeriesDescription]

    print(f"Number of FLAIR series: {len(flair_series)}")

    # count of studies in the FLAIR series
    print(f"Number of studies in the FLAIR series: {len(list(chain(*flair_series)))}")

    if len(flair_series) != 1:
        exit("Error: more than more FLAIR series candidates.")

    command = f"storescu localhost 109 -v -aec TESTSCU +r +sd \"{os.path.dirname(flair_series[0][0][0])}\""
    
    os_command(command)

