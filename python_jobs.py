import requests
from bs4 import BeautifulSoup

# f = open("python_jobs_results.txt", "w")
html = open("python_jobs.html", "w")
# page = requests.get(URL)

# print("Source: " + URL, file=f)
# print(file=f)

"""
def scrape_python_jobs():
    URL = "https://pythonjobs.github.io/"
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")

    job_listings = []

    listings = soup.find_all("div", class_="card-body")

    for listing in listings:
        title = listing.find("h2").text.strip()
        company = listing.find("h3").text.strip()
        location = listing.find("p", class_="location").text.strip()
        link = URL + listing.find("a")["href"]

        job_listings.append({
            "title": title,
            "company": company,
            "location": location,
            "link": link 
        })

    return job_listings 
"""

# results = soup.find(id="main") # Finds specific HTML element by its ID

# print(results.prettify(), file=html) # Prints all HTML in txt file

URL = "https://pythonjobs.github.io/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="main")

job_list = results.find("section", class_="job_list")

job_elements = job_list.find_all("div", class_="job")

print(job_list, file=html)

for job in job_elements:
    title_element = job.find("h1")
    
    print(title_element.text.strip())

"""
for job_element in job_elements:
    title_element = job_element.find("h1").find("a").string
    print(title_element)
"""

# print(results.prettify(), file=html)



"""
for job in jobs:
    print("Title:", job["title"])
    print("Company:", job["company"])
    print("Location:", job["location"])
    print("Link:", job["link"])
    print()
"""

# f.close()
html.close()
