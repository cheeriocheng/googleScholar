#!/Users/xx/.local/share/virtualenvs/googleScholar-cO_WMZC9/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep 
import csv

driver = webdriver.Chrome()
driver.get("https://scholar.google.com/scholar?cites=7079466816456614288&as_sdt=2005&sciodt=0,5&hl=en")
# assert "Python" in driver.title
#gs_ri  citation
#<h3 class="gs_rt" ontouchstart="gs_evt_dsp(event)"><a href="https://dl.acm.org/citation.cfm?id=2557005" data-clk="hl=en&amp;sa=T&amp;ct=res&amp;cd=1&amp;ei=ygPAWuXMNqvXjgTTx62gBg">faBrickation: fast 3D printing of functional objects by integrating construction kit building blocks</a></h3>
#gs_a authors 


index = 1 

def webToCSV():
	global index
	citations = driver.find_elements_by_class_name("gs_ri")
	for c in citations:
		title = c.find_element_by_xpath('.//h3[@class="gs_rt"]')
		# authors = c.find_elements_by_xpath('.//div[@class="gs_a"]/a')  #dont include the procceding name 
		authors = c.find_elements_by_xpath('.//div[@class="gs_a"]')
		s=''
		for a in authors: 
			s += a.text 
		writer.writerow([str(index)] + [title.text] + [s] )
		index += 1


with open('citations.csv', 'w') as csvfile:
	writer = csv.writer(csvfile, delimiter=' ')
	while True: 
		webToCSV()
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		sleep(2)
		# click next button
		# submit_button = driver.find_elements_by_xpath('//*[@id="gs_nm"]/button')[1] #  button for next page
		try:
			next_button = driver.find_element_by_class_name("gs_ico_nav_next")
			next_button.click()
		except:
			driver.close()
			break





	# citations = driver.find_elements_by_class_name("gs_ri")
	# for c in citations:
	# 	title = c.find_element_by_xpath('.//h3[@class="gs_rt"]')
	# 	# authors = c.find_elements_by_xpath('.//div[@class="gs_a"]/a')  #dont include the procceding name 
	# 	authors = c.find_elements_by_xpath('.//div[@class="gs_a"]')
	# 	s=''
	# 	for a in authors: 
	# 		s += a.text 
	# 	writer.writerow([str(index)] + [title.text] + [s] )
	# 	index += 1

 



# persons.append({'title': title, 'company': company})
