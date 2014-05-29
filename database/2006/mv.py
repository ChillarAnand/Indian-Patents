import glob
import os
import string
import subprocess

pdf_files = glob.glob( '/home/anand/git/indian-patents/pdfbox/database/2006/*.pdf' )



for fileName in pdf_files:

    baseName = os.path.basename(fileName)

    all = string.maketrans('','')
    nodigs = all.translate(all, string.digits)
    dirName =  baseName.translate(all, nodigs)
    subprocess.call("mkdir " + dirName, shell=True)
    subprocess.call("mv " + fileName + " " + dirName, shell=True)

