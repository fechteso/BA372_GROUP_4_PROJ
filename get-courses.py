#!!!Note: this service only works for the current academic term; change the program accordingly !!!
import requests
import json

#OSU course catalog URL
url = "https://classes.oregonstate.edu/api/?page=fose&route=search"

#https://catalog.oregonstate.edu/college-departments/business/#coursestext SOURCE for couse codes
cob_couse_codes= {'BA', 'ACTG', 'BANA','BIS', 'DSGN', 'FIN', 'HM', 'MRKT', 'MGMT','SCLM'}
#Set up the query
for course_code in cob_couse_codes:
    
    query_dict = {
        #TODO  replace static 202403 string with dynamic user text entry
    "other" : {"srcdb": "202403"},  #Spring (03) of academic year 2023-24
    "criteria" : [ {"field" : "subject", "value" : course_code } ] 
    }

    #Convert query_dict into string
    query_str = json.dumps(query_dict)

    #print("query_str: ", query_str)
    try:
    #Make POST request; pass query_str as data
        response = requests.post(url, data=query_str, timeout=10)
    except:
        print("Error... API call failed")
        exit(1)

    #print(response.status_code)
    print(response.text)#todo parse output as JSON and store each course in the same dictionary
    

    