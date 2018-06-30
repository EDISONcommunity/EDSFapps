
#  Matching CVs based on EDISON Data Science Competencies (CF-DS): Back end
This is the back end component of the full implementation. 
It is fully written in Python and contains the following files:
 
    - cv_info_extractor.py
    - similarity_calc.py
    - server.py
It returns a post request when called with a CV document that contains the following things:
30 document similarity scores, extracted text, and a CV info object that contains information about the jobs that were found in the CV.

# Python Dependencies
Before running the project, install the following dependencies with `pip install 'dependency_name'`

    - flask_cors
    - flask
    - scipy
    - tika
	- nltk
	- sklearn
	- openpyxl

# Running the server

Simply use `python server.py` from a terminal to start the server.
Invoke it by making a post request that contains a PDF document as parameter.
