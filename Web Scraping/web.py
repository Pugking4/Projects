import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Firefox(executable_path='/nix/path/to/webdriver/executable')
driver.get('https://heritagenursery.com.au/pages/careers')

results = []

content = driver.page_source
soup = BeautifulSoup(content)

# Change ‘list-item’ to ‘title’.
for element in soup.findAll(attrs={'class': 'rte'}):
    name = element.find('p')
    # Add the object of “name” to the list “results”.
    # `<element>.text` extracts the text in the element, omitting the HTML tags.

    if name not in results:
        results.append(name.text)

df = pd.DataFrame({'text': results})
df.to_excel('text.xlsx', index=False, encoding='utf-8')
