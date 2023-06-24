import requests
from bs4 import BeautifulSoup

f = open("python_jobs_results.txt", "w")
html = open("python_jobs.html", "w")

URL = "https://pythonjobs.github.io/"
page = requests.get(URL)

# print("Source: " + URL, file=f)
# print(file=f)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="main") # Finds specific HTML element by its ID

print(results.prettify(), file=html) # Prints all HTML in txt file

job_elements = results.find_all("div", class_="job")

f.close()
html.close()

