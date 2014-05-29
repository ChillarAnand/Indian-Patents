#! usr/bin/python

import sys

# import functions from functions.py
import functions
import data

def main():
    
    try:

        functions.read_file(sys.argv[1])
        functions.get_app_num_pub_filing_date()    

        if data.values[0] and data.values[1] != '': # to check if the page is a patent or not
            functions.get_title()
            functions.get_abstract()
            functions.get_name_of_applicant()
            functions.get_name_of_inventor()
            functions.get_int_class_priorty_doc_num()
            functions.get_int_app_pub_num()
            functions.print_data()
        else:
            print 'Not a patent'

    except:
        print "Error in extracting"

if __name__ == "__main__": 
    main()
    
