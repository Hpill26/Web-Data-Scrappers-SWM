# %% [markdown]
# ### Import necessary Packages:

# %%
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
import pandas as pd
from selenium.webdriver.common.by import By

# %% [markdown]
# ### Setup Web-Driver:

# %%
search_query = 'https://www.indeed.com/jobs?q=python&l=&from=searchOnHP'
s = Service(r'C:\\Users\\Rohit Reddy\\Downloads\\chrome-win64\\chromedriver.exe')
driver = webdriver.Chrome(executable_path="C:\\Users\\Rohit Reddy\\Downloads\\chrome-win64\\chromedriver.exe")

driver.get(search_query)
driver.maximize_window()

time.sleep(5)

# %% [markdown]
# ### Scrape data from the web-page:

# %%
job_details = []
job_info = []

#list of all jobs with their elements

job_list = driver.find_elements("xpath", "//div[@class='job_seen_beacon']")

for job in job_list:
    
    #job Title
    title = job.find_element(By.CLASS_NAME, "jobTitle").text
    
    #Company Name
    company=job.find_element(By.CLASS_NAME, "company_location").text.split("\n")[0]

    #rating = job.find_elements_by_xpath(".//span[@class='ratingNumber']/span")[0]
    
    #Job Location
    location= job.find_element(By.CLASS_NAME, "company_location").text.split("\n")[1:]
    
    #Job Summary
    summary = job.find_element(By.CLASS_NAME, "job-snippet").text
    
    job_info = [title, company, location, summary]

    job_details.append(job_info)

# %%
# next_page_button = driver.find_element(By.CLASS_NAME, 'pn')

# %%
#construct the dataframe
df = pd.DataFrame(job_details, columns= ['Job Title', 'Company', 'Location', 'Description'])

#close the driver
driver.quit()

# %%
df.to_excel('Indeed_DataScientist_Jobs.xlsx', index= False)


