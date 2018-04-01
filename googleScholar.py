#!/Users/xx/.local/share/virtualenvs/googleScholar-cO_WMZC9/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep 
import csv

driver = webdriver.Chrome()
#the first page of the scholar citation page
driver.get("https://scholar.google.com/scholar?cites=7079466816456614288&as_sdt=2005&sciodt=0,5&hl=en")


#gs_ri  citation
#gs_rt titles
#gs_a authors 


index = 1 

def dequote(s):
    """
    If a string has single or double quotes around it, remove them.
    Make sure the pair of quotes match.
    If a matching pair of quotes is not found, return the string unchanged.
    """
    if (s[0] == s[-1]) and s.startswith(("'", '"')):
        return s[1:-1]
    return s

def webToCSV():
	global index
	citations = driver.find_elements_by_class_name("gs_ri")
	for c in citations:
		title = c.find_element_by_xpath('.//h3[@class="gs_rt"]').text
		title = dequote(title)
		
		authors = c.find_elements_by_xpath('.//div[@class="gs_a"]')[0].text
		'''authors = c.find_elements_by_xpath('.//div[@class="gs_a"]/a')  #dont include the procceding name 
		s=''
		for a in authors: 
			s += a.text 
			s += ', '
		if len(authors)>0:
			s = s[0:-2]
		'''
		writer.writerow([str(index)] + [title])
		writer.writerow([authors])
		writer.writerow('\n') #spacer between entries
		index += 1



# with open('citations.csv', 'w',newline='') as csvfile:

# 	writer = csv.writer(csvfile)
# 	while True: 
# 		webToCSV()
# 		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# 		sleep(1) #time for the page to scroll down and make the next button visiable
# 		# click next button
# 		try:
# 			# Note that when debug window is open on the side, the HTML elements are different! 
# 			# Use debug window on the bottom to identify the class name.
# 			# submit_button = driver.find_elements_by_xpath('//*[@id="gs_nm"]/button')[1] #  button for next page
# 			next_button = driver.find_element_by_class_name("gs_ico_nav_next")
# 			next_button.click()
# 		except:
# 			driver.close()
# 			break

def webToTXT():
	global index
	citations = driver.find_elements_by_class_name("gs_ri")
	for c in citations:
		title = c.find_element_by_xpath('.//h3[@class="gs_rt"]').text
		title = dequote(title)
		
		authors = c.find_elements_by_xpath('.//div[@class="gs_a"]')[0].text
		'''authors = c.find_elements_by_xpath('.//div[@class="gs_a"]/a')  #dont include the procceding name 
		s=''
		for a in authors: 
			s += a.text 
			s += ', '
		if len(authors)>0:
			s = s[0:-2]
		'''
		file.write(str(index) + ' "' + title + '"')
		file.write('\n')
		file.write(authors)
		file.write('\n')
		file.write('\n')

		index += 1


with open('citations.txt', 'w') as file:
# with open('citations.csv', 'w',newline='') as csvfile:

	while True: 
		webToTXT()
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		sleep(1) #time for the page to scroll down and make the next button visiable
		# click next button
		try:
			# Note that when debug window is open on the side, the HTML elements are different! 
			# Use debug window on the bottom to identify the class name.
			# submit_button = driver.find_elements_by_xpath('//*[@id="gs_nm"]/button')[1] #  button for next page
			next_button = driver.find_element_by_class_name("gs_ico_nav_next")
			next_button.click()
		except:
			driver.close()
			break



