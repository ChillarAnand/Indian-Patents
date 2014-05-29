import glob
import os
import string
import subprocess

pdf_files = glob.glob( '/home/anand/git/indian-patents/database/2013/*.pdf' )



for fileName in pdf_files:

    baseName = os.path.basename(fileName)

    all = string.maketrans('','')
    nodigs = all.translate(all, string.digits)
    dirName =  baseName.translate(all, nodigs)
    subprocess.call("mkdir " + dirName, shell=True)

