
import sys
import os
import subprocess


file_name = sys.argv[1]

# get number of pages in a pdf
output = subprocess.check_output("pdfinfo " + file_name + " | grep 'Pages'", shell=True)
num_of_pages = int( output[6:] )

dir_name = os.path.dirname(os.path.abspath(file_name)) + '/'

root_dir = "/home/anand/git/indian-patents"

for i in range(1,num_of_pages):
    i = str(i)
    command = "java -jar " + root_dir + "/pdfbox-app-1.8.5.jar ExtractText " + file_name + " " + dir_name + i + "-extracted.txt -startPage " + i + " " + "-endPage " + i


    subprocess.check_output(command, shell=True)

    try:
        output = subprocess.check_output("python " + root_dir + "/pdfbox/process_text.py " + dir_name  + i +"-extracted.txt", shell=True)
    except:
        output = "Error in extracting"

    if output.strip() == "Not a patent":
        continue
    else:
       subprocess.check_output("python " + root_dir + "/pdfbox/process_text.py " + dir_name  + i +"-extracted.txt > " + dir_name + i + "-processed.txt", shell=True)



for i in range(1,num_of_pages):
    try:
        com4 = "rm " + dir_name + i + "-extracted.txt"
        subprocess.check_output(com4, shell=True)
    except:
        a = 'a'
