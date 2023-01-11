import requests
from bs4 import BeautifulSoup


URL = "https://www.joblist.com/ca/search?l="

location = "blank"
while (True):
    location = input("Enter location: (Toronto, Vancouver, Ottawa):")
    if (location != "Toronto" and location != "Vancouver" and location != "Ottawa"):
        print("Invalid location")
        continue
    break

job = "blank"
jobs = []
check = "0"
while (True):
    job = input("Enter job description(one word): ")
    jobs.append(job)
    for j in jobs:
        print(j, end=' ')
    print()
    while (True):
        check = input("Enter '1' if you want to enter additional description. Otherwise, enter '0':")
        if (check != "1" and check != "0"):
            print("Invalid input")
            continue
        break
    if (check == "1"):
        continue
    elif (check == "0"):
        break

jobs_str = ""
for i in jobs:
    jobs_str += i + ' '

URL += location + "%2C+ON&q=" + jobs_str + "&lr=ANY_LOCATION"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="JobContainer")
job_elements = results.find_all("div", class_="job-item")

print()
print("Found " + str(len(job_elements)) + " results")
print()

for job_element in job_elements:
    title_element = job_element.find("h2", class_="itemHeaderUi")
    company_element = job_element.find("div", class_="itemMetaUi")
    location_element = job_element.find_all("div", class_="itemMetaUi")
    print(title_element.text)
    print(company_element.text)
    print(location_element[1].text)
    print()