import requests
from bs4 import BeautifulSoup

f = open("fake_jobs_results.txt", "w")
html = open("fake_jobs_webpage.html", "w")

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

print("Source: " + URL, file=f)
print(file=f)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer") # Finds specific HTML element by its ID

print(results.prettify(), file=html) # Prints all HTML contained within the <div>

job_elements = results.find_all("div", class_="card-content")

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    time_element = job_element.find("time")
    link_url = job_element.find_all("a")[1]["href"]
    
    print(title_element.text.strip(), file=f)
    print(company_element.text.strip(), file=f)
    print(location_element.text.strip(), file=f)
    print(time_element.text.strip(), file=f)
    print(f"Apply here: {link_url}\n", file=f)

f.close()