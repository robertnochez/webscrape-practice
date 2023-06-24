import requests
from bs4 import BeautifulSoup

f = open("python_jobs_results.txt", "w")
html = open("python_jobs.html", "w")

URL = "https://pythonjobs.github.io"
page = requests.get(URL)

print("Source: "+URL+"/"+"\n", file=f)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="main")

job_list = results.find("section", class_="job_list")

job_elements = job_list.find_all("div", class_="job")

print(job_list, file=html)

for job in job_elements:
    title_element = job.find("h1")
    info = job.find_all("span", class_="info")
    location = info[0].text.strip()
    time = info[1].text.strip()
    company = info[3].text.strip()
    link_url = job.find_all("a")[1]["href"]

    print(title_element.text.strip(), file=f)
    print(company, file=f)
    print(location, file=f)
    print(time, file=f)
    print("Job listing: "+URL+link_url, file=f)
    print(file=f)

f.close()
html.close()
