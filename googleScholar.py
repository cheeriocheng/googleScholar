#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import csv
import random


driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

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
		writer.writerow([str(index)] + [title])
		writer.writerow([authors])
		writer.writerow('\n') #spacer between entries
		index += 1


'''
EXPORT CSV
'''

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
		file.write(str(index) + ' "' + title.encode('utf-8').strip() + '"')
		file.write('\n')
		file.write(authors.encode('utf-8').strip())
		file.write('\n')
		file.write('\n')
		print("Citations found: " + str(index))
		index += 1

def loadAllCitationsFromLink(link):
	#the first page of the scholar citation page
	driver.get(link)
	raw_input("when webpage is ready, click enter: ")
	while True:
		webToTXT()
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		sleep(random.random()*50) #time for the page to scroll down and make the next button visiable
		# click next button
		try:
			# Note that when debug window is open on the side, the HTML elements are different!
			# Use debug window on the bottom to identify the class name.
			next_button = driver.find_element_by_class_name("gs_ico_nav_next")
			next_button.click()
		except:
			break


'''
EXPORT TXT
'''
with open('citations.txt', 'w') as file:
	#this is the main google scholar profile page
	driver.get("https://scholar.google.com/citations?user=aaTHLnkAAAAJ&hl=en&oi=sra")
	raw_input("when webpage is ready, click enter.")
	#find all citation links
	links = []
	for l in driver.find_elements_by_xpath('.//a[@class="gsc_a_ac gs_ibl"]'):
		if l.text != '' :
			print(l.get_attribute('href'))
			links.append(l.get_attribute('href'))

	for l in links:
		sleep(random.random()*30)
		loadAllCitationsFromLink(l)

	file.close()
	driver.close()



