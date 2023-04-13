#!/usr/bin/python3
#Resume_Scanner_Python
#Resume Scanner

# Import required libraries
from PyPDF2 import PdfReader
import textract
import re
import string
import pandas as pd
import matplotlib.pyplot as plt

# Open pdf file
pdfFileObj = open('/Users/.../Resume_2023.pdf','rb')

# Read file
pdfReader = PdfReader(pdfFileObj)

# Get total number of pages
num_pages = len(pdfReader.pages)

# Initialize a count for the number of pages
count = 0

# Initialize a text empty etring variable
text = ""

# Extract text from every page on the file
while count < num_pages:
    pageObj = pdfReader.pages[count]
    count +=1
    text += pageObj.extract_text()

#View Text and Page Count
print("The number of pages:",count)
print(text)

# Convert all strings to lowercase
text = text.lower()

# Remove numbers
text = re.sub(r'\d+','',text)

# Remove punctuation
text = text.translate(str.maketrans('','',string.punctuation))

#View new resume for matching keyterms
print(text)

#KeyTerms for Industrial Engineering Resumes
#Change Job Posting with new content from Job_Posting_Keyterms.py

terms = {'Quality/Six Sigma':['black belt','capability analysis','control charts','doe','dmaic','fishbone',
                              'gage r&r', 'green belt','ishikawa','iso','kaizen','kpi','lean','metrics',
                              'pdsa','performance improvement','process improvement','quality',
                              'quality circles','quality tools','root cause','six sigma',
                              'stability analysis','statistical analysis','tqm'],      
        'Operations management':['automation','bottleneck','constraints','cycle time','efficiency','fmea',
                                 'machinery','maintenance','manufacture','line balancing','oee','operations',
                                 'operations research','optimization','overall equipment effectiveness',
                                 'pfmea','process','process mapping','production','resources','safety',
                                 'stoppage','value stream mapping','utilization'],
        'Supply chain':['abc analysis','apics','customer','customs','delivery','distribution','eoq','epq',
                        'fleet','forecast','inventory','logistic','materials','outsourcing','procurement',
                        'reorder point','rout','safety stock','scheduling','shipping','stock','suppliers',
                        'third party logistics','transport','transportation','traffic','supply chain',
                        'vendor','warehouse','wip','work in progress'],
        'Project management':['administration','agile','budget','cost','direction','feasibility analysis',
                              'finance','kanban','leader','leadership','management','milestones','planning',
                              'pmi','pmp','problem','project','risk','schedule','scrum','stakeholders'],
        'Data analytics':['analytics','api','aws','big data','busines intelligence','clustering','code',
                          'coding','data','database','data mining','data science','deep learning','hadoop',
                          'hypothesis test','iot','internet','machine learning','modeling','nosql','nlp',
                          'predictive','programming','python','r','sql','tableau','text mining',
                          'visualuzation'],
        'Healthcare':['adverse events','care','clinic','cphq','ergonomics','healthcare',
                      'health care','health','hospital','human factors','medical','near misses',
                      'patient','reporting system'],
        'Job Posting': ['BA/BS', 'degree', 'in', 'Statistics,', 'Data', 'Science,', 'Mathematics,', 'Economics,', 'Computer', 'Marketing,', 'or', 'any', 'related', 'field', 'Experience', 'working', 'as', 'an', 'analyst', 'a', 'direct', 'response', 'marketing', 'business', 'team', 'Expertise', 'Tableau,', 'Datorama,', 'Google', 'Studio,', 'SAP', 'Analytics', 'Cloud', 'other', 'similar', 'data', 'visualization', 'software', 'with', 'within', 'Analytics,', 'Facebook', 'Ads', 'Manager,', 'and', 'Salesforce', 'Marketing', 'automation', 'using', 'Tag', 'Manager', 'SQL,', 'R,', 'Python', 'Outstanding,', 'expert-level', 'statistical', 'analysis', 'mathematics', 'skills', 'Highly', 'skilled', 'Excel', 'to', 'do', 'complex', 'calculations,', 'produce', 'dashboard-ready', 'tables', 'charts,', 'create', 'financial', 'modeling', 'Strong', 'technical', 'aptitude,', 'ability,', 'desire', 'learn', 'quickly', 'Self-motivated', 'the', 'ability', 'take', 'direction', 'work', 'independently', 'little', 'supervision', 'Solid', 'understanding', 'of', 'database', 'technology,', 'systems,', 'processes.', 'Passion', 'for', 'big', 'data,', 'science,', 'and/or', 'marketing/business', 'analytics', 'Ability', 'make', 'formal', 'informal', 'presentations', 'groups', 'inside', 'outside', 'organization', 'Flexible', 'able', 'shift', 'mindset', 'change', 'priorities', 'fast', 'paced', 'environment']
        }
        
# Initializie score counters for each area
quality = 0
operations = 0
supplychain = 0
project = 0
data = 0
healthcare = 0
jobposting = 0

# Create an empty list where the scores will be stored
scores = []

# Obtain the scores for each area
for area in terms.keys():
        
    if area == 'Quality/Six Sigma':
        for word in terms[area]:
            if word in text:
                quality +=1
        scores.append(quality)
        
    elif area == 'Operations management':
        for word in terms[area]:
            if word in text:
                operations +=1
        scores.append(operations)
        
    elif area == 'Supply chain':
        for word in terms[area]:
            if word in text:
                supplychain +=1
        scores.append(supplychain)
        
    elif area == 'Project management':
        for word in terms[area]:
            if word in text:
                project +=1
        scores.append(project)
        
    elif area == 'Data analytics':
        for word in terms[area]:
            if word in text:
                data +=1
        scores.append(data)
    elif area == 'Job Posting':
        for word in terms[area]:
            if word in text:
                jobposting +=1
        scores.append(jobposting)
    else:
        for word in terms[area]:
            if word in text:
                healthcare +=1
        scores.append(healthcare)
# Create a data frame with the scores summary
summary = pd.DataFrame(scores,index=terms.keys(),columns=['score']).sort_values(by='score',ascending=False)
print(summary)

# Create pie chart visualization
pie = plt.figure(figsize=(10,10))
plt.pie(summary['score'], labels=summary.index, explode = (0.1,0,0,0,0,0,0), autopct='%1.0f%%',shadow=True,startangle=90)
plt.title('Data Analysis and Industrial Engineering Candidate - Resume Decomposition by Areas')
plt.axis('equal')
plt.show()

# Save pie chart as a .png file
pie.savefig('resume_screening_results.png')
