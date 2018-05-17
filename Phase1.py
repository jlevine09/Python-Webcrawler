from bs4 import BeautifulSoup
import sys
import webbrowser
import mechanize
import string
import time
import os


br = mechanize.Browser()
br.set_handle_equiv(False)
br.set_handle_robots(False)
br.set_handle_referer(False)

br.open('https://ciwqs.waterboards.ca.gov/ciwqs/readOnly/CiwqsReportServlet?reportID=744288&reportName=RegulatedFacilityDetail&inCommand=displayCriteria')

print ("What regions information would you like?")
print ("1: North Coast")
print ("2: San Francisco Bay")
regionInput = raw_input ("Enter number:" )



br.select_form(name='regFacilityCriteriaForm')
typename = 'Wastewater Treatment Facility'
br['typeDrop'] = [typename]
br['regDrop'] = [regionInput]


response = br.submit() 
        
if (regionInput == '1'):
    br.follow_link(nr=13)
    
if (regionInput ==  '2'):
    br.follow_link(nr=19)

print br.geturl()



response2 = br.follow_link(text = '[VIEW PRINTER FRIENDLY VERSION]')


data = response2.read()
soup = BeautifulSoup(data)


tme = time.localtime()
current_time = time.strftime("%m.%d.%y", tme)
output_name = '{}_Orders_{}.txt'.format(regionInput,current_time)
myfile = open(output_name , 'w')
myfile.truncate()
    

tables = [el.text for el in soup("a","ciwqsReportColumnName")]
content_Head = str(tables)
print content_Head
myfile.write(content_Head)
rows = [el.text for el in soup("span","ciwqsReportColumnData")]
content_Body = str(rows)
print content_Body
myfile.write(content_Body)

myfile.close()

