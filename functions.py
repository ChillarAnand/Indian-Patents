# import regular expressions
import re

# import all variables from data.py
import data



# read file and save contents to a list
def read_file( text_file ):
    data.all_lines = open(text_file).read().splitlines()

    # to remove un wanted spaces
    for i in range(len(data.all_lines)):
        line = data.all_lines[i] 
        line = remove_spaces(line)
        data.all_lines[i] = line



# get application number, filing date, publication date
def get_app_num_pub_filing_date():

    file_contents = data.all_lines

    for line in file_contents:

        if data.pdf_fields[0] in line:
            dot_position = line.index('.') + 1
            data.values[0] = line[dot_position:] 

        if data.pdf_fields[1] in line:
            colon_position = line.index(':') + 1
            data.values[1] = line[colon_position:colon_position+11]  

        if data.pdf_fields[2] in line:
            line = line[colon_position+11:]  
            colon_position = line.index(':') + 1
            data.values[2] = line[colon_position:]



def get_title():

    try:
        file_contents = data.all_lines

        title = ''
        title_start = title_end = False

        for num, line in enumerate (file_contents, start=1):

            if data.pdf_fields[3] in line:
                colon_position = line.index(':') + 1
                title = line[colon_position:]
                title_start = True 
                continue

            if title_start:
                if ('International' or 'classification' in line) and re.search('[(][0-9][0-9][)]', line[:4]):
                    break
                else:
                    title += ' ' + str(line)
            
        data.values[3] =  title

    except:
        print 'Error in extracting. Title'



def get_abstract():

    try:

        file_contents = data.all_lines

        abstract = ''
        abstract_start = abstract_end  = False

        for num, line in enumerate (file_contents, start=1):

            if data.pdf_fields[4] in line:
                colon_position = line.index(':') + 1
                abstract = line[colon_position:]
                abstract_start = True 
                continue

            if abstract_start:
                if not line.strip() or ( re.search('No. of Pages', line) and re.search('No. of Claims', line) ):
                    break
                else:
                    abstract += ' ' + str(line)

        data.values[4] =  abstract

    except:
        print 'Error in extracting. Abstract'



def get_name_of_applicant():

    try:

        file_contents = data.all_lines

        address_of_applicant = False
        name_of_applicant = ''

        for num, line in enumerate (file_contents, start=1):
            if data.pdf_fields[5] in line:
                name_of_applicant_start = num 

        for line in file_contents[name_of_applicant_start:]:

            if line[4:].strip() in data.all_pdf_fields:
                continue

            if ( not line.strip() ) or ( data.pdf_fields[6] in line ):
                break

            elif ( 'Address of Applicant' in line or address_of_applicant ):  # to skip the address of the applicant
                address_of_applicant = True
                if data.pdf_fields[6] in line:
                    address_of_applicant = False
                elif '2)' in line.strip():
                    address_of_applicant = False
                    name_of_applicant += ' ' + line
                continue

            else:
                name_of_applicant += ' ' + line

        data.values[5] = name_of_applicant
#        print data.values[5]


    except:
        print 'Error in extracting. Name of applicant'



def get_name_of_inventor():

    try:

        file_contents = data.all_lines

        name_of_inventor = ''

        for num, line in enumerate (file_contents, start=1):
            if data.pdf_fields[6] in line:
                name_of_inventor_start = num 

        for line in file_contents[name_of_inventor_start:]:
            if line[4:].strip() in data.all_pdf_fields:
                break
            if  line.strip():
                name_of_inventor += ' ' + line
            else:
                break

        data.values[6] = name_of_inventor

    except:
        print 'Error in extracting. Name of inventor'


# get 
def get_int_class_priorty_doc_num():

    try:
    
        file_contents = data.all_lines
        int_classification_status = False
        int_classification = ''
        priority_doc_num_status = False
        priority_doc_num = ''

        for num, line in enumerate (file_contents, start=1):
            if re.search("[:][a-zA-Z][0-9][0-9][a-zA-Z]", line.strip() ) or re.search("[:][a-zA-Z][  ][0-9][0-9][  ][a-zA-Z]", line.strip() ):
                int_classification_status = True
                colon_position = line.index(':') + 1
                int_classification += ' ' + line[colon_position:]
                int_classification_status = True
                continue
            
            if int_classification_status:
                # if re.match('[(][0-9][0-9][)]', line[:4]):
                if 'Priority' in line: 
                    break
                else:
                    int_classification += ' ' + line


        data.values[7] = int_classification

    except:
        print 'Error in extracting. International Classification.'



    try:

        colon_position = ''
        for num, line in enumerate (file_contents, start=1):

            if data.pdf_fields[8] in line:
                if ':' in line:
                    colon_position = line.index(':') + 1
                    priority_doc_num = line[colon_position:]
                    break
                else:
                    priority_doc_num = file_contents[num] + file_contents[num+1] + file_contents[num+2]

        if priority_doc_num.strip() != 'N/A' or priority_doc_num.strip() != 'NA':
            data.values[8] = priority_doc_num

    except:
        print 'Error in extracting. Priority Document Number'



def get_int_app_pub_num():

    try:

        int_app_num = ''
        file_contents = data.all_lines
        for num, line in enumerate (file_contents, start=1):
            if re.match("[:][pP][cC][tT]", line.strip() ):
                int_app_num = line[1:]

        data.values[9] = int_app_num

    except:
        print 'Error in extracting. International Application Number'



    try:
        int_pub_num = ''
        int_pub_start = -2
        file_contents = data.all_lines
        for num, line in enumerate (file_contents, start=1):
            if re.search("[:][wW][oO]", line.strip() ):
                colon_position = line.index(':') + 1
                int_pub_num = ' ' + line[colon_position:]
                int_pub_start = num
                continue

            if num == int_pub_start + 1 and len(line) >= 2:
                if (line[0] != '(') and (line == 'A1' or 'A2' or line[:3] == '20[0-9][0-9]'):
                    int_pub_num += ' ' + line
                    int_pub_start = False
                    break


        data.values[10] = int_pub_num

    except:
        print 'Error in extracting. International Publication Number'


def remove_spaces( line ):
        return ' '.join(line.split())


def validate():
    for i in range(11):
        for j in range(11):
            if data.pdf_fields[j] in data.values[i]:
                print 'Error in extracting. Lines combined'

def print_data():
    validate()
    for i in range(11):
        data.values[i] = remove_spaces(data.values[i])
        if i == 4:
            continue
        print data.text_fields[i], data.delimiter, data.values[i], '\n'

    print data.text_fields[4], data.delimiter, data.values[4], '\n' # to print abstract in the end

