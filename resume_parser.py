from datetime import datetime
import numpy as np

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

industries = []
sectors = []
for job in work_hist['employmentHistoryList']:
    classified = process_text(job['description'])
    industries.append((top_taxonomy(classified))['mainTopic'])
    sectors.append((top_taxonomy(classified))['subTopic'])

titles = []
for job in work_hist['employmentHistoryList']:
    titles.append(job['title'])

org_name = []
for job in work_hist['employmentHistoryList']:
    org_name.append(job['employerOrgName'])

position = []
for job in work_hist['employmentHistoryList']:
    position.append(job['sovPositionId'])

time = []
for job in work_hist['employmentHistoryList']:
    start = job['startDate']
    end = job['endDate']
    length = days_between(start,end)
    years = np.ceil(length/ (365.25))
    time.append(years)

workHistory = []
for x in range(0, len(work_hist['employmentHistoryList'])):
    job = {}
    job['Title'] = titles[x]
    job['Organization'] = org_name[x]
    job['Industry'] = industries[x]
    job['Sector'] = sectors[x]
    job['Position'] = position[x]
    job['Time'] = time[x]
    workHistory.append(job)

##########################################################################################

deg_name = []
for school in ed_hist['educationHistoryList']:
    deg_name.append(school['degreeName'])

deg_type = []
for school in ed_hist['educationHistoryList']:
    deg_type.append(school['degreeType'].title())

major = []
for school in ed_hist['educationHistoryList']:
    major.append(school['majorName'])

school_name = []
for school in ed_hist['educationHistoryList']:
    school_name.append(school['degreeName'])

position = []
for school in ed_hist['educationHistoryList']:
    position.append(school['sovPositionId'])

education = []
for x in range(0, len(ed_hist['educationHistoryList'])):
    school = {}
    school['Degree Name'] = deg_name[x]
    school['Degree Type'] = deg_type[x]
    school['Major'] = major[x]
    school['School'] = school_name[x]
    school['Position'] = position[x]
    education.append(school)
