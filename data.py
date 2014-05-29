pdf_fields = ['Application No.', 'Date of filing of Application', 'Publication Date',
                'Title of the invention','Abstract :',
                'Name of Applicant', 'Name of Inventor',
                'International classification', 'Priority Document No',
                'International Application No', 'International Publication No' ]


text_fields = ['Application number', 'Date of filing of application number', 'Publication date',
               'Title', 'Abstract', 
               'Name of applicant', 'Name of inventor',
               'International Classification', 'Priority Doc No',
               'International Application Number', 'International Publication Number']


values = ['' for i in range(11)]

delimiter = ' => '

file_name = ''

file_contents = []

all_lines = []

all_pdf_fields = ['Application No.', 'Date of filing of Application', 'Publication Date',
                'Title of the invention','Abstract :',
                'Name of Applicant', 'Name of Inventor',
                'International classification', 'Priority Document No',
                'International Application No', 'International Publication No',
                'Priority Date', 'Name of priority country',
                'International Application No', 'Patent of Addition', 'Filing Date',
                'International Publication No', 'Divisional to Application']
