********
scraping
********

beautiful soup
==============

https://www.crummy.com/software/BeautifulSoup/bs4/doc/

setup bs4
---------

.. code-block:: python

   import sys
   !{sys.executable} -m pip install beautifulsoup4
   from bs4 import BeautifulSoup
   
   soup = BeautifulSoup(html_doc, "lxml")
   # In my file (becode.org) by looking at this html script We can see that the main title is arranged in the h1 tag
   
   for p in soup.find_all('h1'):
       # We only retrieve the content ==> .text
       print (p.text)
   # BeCode.org



find html elements
------------------

https://www.crummy.com/software/BeautifulSoup/bs4/doc/#a-regular-expression

.. code-block:: python

   from bs4 import BeautifulSoup
   soup = BeautifulSoup('<html><body><div>asdfasdf</div><p><a>foo</a></p></body></html>')
   soup.find_all(['a', 'div'])
   # [<div>asdfasdf</div>, <a>foo</a>]

   # using a regular expression to find tags that contain a or div:
   import re
   soup.find_all(re.compile("(a|div)"))

   # regex to search in attributes of tags
   soup.find_all('a', {'href': re.compile(r'crummy\.com/')})

   # regex to find all titles
   find_titles = re.compile("(h\d)")
   titles = soup.find_all(find_titles)
   print(titles)

   store_titles = []
   for elem in soup.find_all('a',attrs={"class" :"meta-title meta-title-link"}):
       store_titles.append(elem.get('href': re.compile("\d{4,7}.html"))
       # return a list
   """
   <a class="meta-title meta-title-link" href="/film/fichefilm_gen_cfilm=275354.html" title="Chacun chez soi">Chacun chez soi</a>
   <a class="meta-title meta-title-link" href="/film/fichefilm_gen_cfilm=272523.html" title="Des hommes">Des hommes</a>
   
   /film/fichefilm_gen_cfilm=275666.html
   /film/fichefilm_gen_cfilm=277756.html
   /film/fichefilm_gen_cfilm=44282.html
   /film/fichefilm_gen_cfilm=274345.html
   /film/fichefilm_gen_cfilm=281050.html
   /film/fichefilm_gen_cfilm=268680.html
   /series/ficheserie_gen_cserie=23474.html
   /series/ficheserie_gen_cserie=26101.html
   /series/ficheserie_gen_cserie=22429.html
   """
   get_titles = re.findall(re.compile("\d{4,7}.html")
   

apply regex on element string
-----------------------------

.. code-block:: python

   import re
   titles = []
   title_pattern = r"\d{4,7}\.html"
   for elem in soup.find_all('a',attrs={"class" :"meta-title meta-title-link"}):
       # results.append(elem.get('href'))
       title = elem.get('href')
       title = re.search(title_pattern, title)[0]
       titles.append(title)
   titles
   
   """
   ['275354.html',
    '272523.html',
    '274710.html',
    '261793.html',
    '265425.html',
    '24172.html',
    '25512.html',
    '25786.html',
    '25515.html']"""


slowly get url page content
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   import time
   import random
   from random import randint
   
   title=[]
   synopsis=[]
   
   for link in links_movie:
   
       url=link
       # I slow down the frequency of requests to avoid being identified and therefore ban from the site
       time.sleep(random.uniform(1.0, 2.0))
       r = requests.get(url)
       print(url, r.status_code)
       soup = BeautifulSoup(r.content,'lxml')
   
   
       for elem in soup.find_all('div', attrs={"class": "titlebar-title titlebar-title-lg"}):
           title.append(elem.text.strip())
   
       for elem in soup.find_all('div', attrs={"class": "content-txt"}):
           synopsis.append(elem.text.strip())
   
   # I check the length of the lists before creating the df
   len(title),len(synopsis),len(links_movie)
   
   
   """
   http://www.allocine.fr/film/fichefilm_gen_cfilm=275354.html 200
   http://www.allocine.fr/film/fichefilm_gen_cfilm=272523.html 200
   ...
   http://www.allocine.fr/film/fichefilm_gen_cfilm=281050.html 200
   http://www.allocine.fr/film/fichefilm_gen_cfilm=268680.html 200
   """

HTTP requests
-------------

`command` is the method to use, it specifies the type of request, it can have the values :


- `"GET"`
This is the most common way to request a resource. A GET request has no effect on the resource, it must be possible to repeat the request without effect.


- `"HEAD"`
This method only asks for information about the resource (the header), without asking for the resource itself.


- `"POST"`
This method must be used when a request modifies the resource.


- `"OPTIONS"`
This method allows you to obtain the communication options of a resource or the server in general.


- `"CONNECT"`
This method allows you to use a proxy as a communication tunnel.


- `"TRACE"`
This method asks the server to return what it has received, in order to test and diagnose the connection.


- `"PUT"`
This method allows you to add a resource to the server.


- `"DELETE"`
This method allows you to delete a resource from the server.

I will only discuss the most common ones here: HEAD, GET and POST.

store html in var
^^^^^^^^^^^^^^^^^

.. code-block:: python

   import requests
   # Url of website
   url='https://www.becode.org/about/'
   # I send my HTTP request with a "GET" to the site server to identify in the url
   r = requests.get(url)
   # I display the requested url and the return of the server
   print(url, r.status_code)
   # I ask beautifulSoup to keep in a soup variable the web page to scrape (url) an html script
   soup = BeautifulSoup(r.content,'lxml')
   soup  # prints all html code



selenium
========

https://selenium-python.readthedocs.io/installation.html#downloading-python-bindings-for-selenium/bin

.. note:: Linux: put your geckodriver in the equivalent path at home to /home/YOURNAME/.local/bin

handy libraries
---------------

.. code-block:: python

   import sys
   # !{sys.executable} -m pip install tabulate
   import bs4
   import requests
   from bs4 import BeautifulSoup
   import numpy as np
   import pandas as pd
   import json
   import re
   import lxml.html
   import time
   import random
   from random import randint
   import logging
   import collections
   from time import gmtime, strftime
   
   import re
   from tabulate import tabulate
   import os
   date=strftime("%Y-%m-%d")
   print(date)

scraping training
======================

inquisitive with bs4 & selenium
-------------------------------

.. code-block:: python

   from selenium import webdriver
   from selenium.webdriver import ActionChains
   from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
   from selenium.webdriver.support.ui import WebDriverWait
   from selenium.webdriver.support import expected_conditions as EC
   from selenium.webdriver.common.by import By
   from selenium.webdriver.remote.webelement import WebElement
   from selenium.webdriver.common.keys import Keys
   import urllib.parse
   import os
   import time
   import re
   import random
   import bs4
   import shelve
   from pprint import pprint as pp
   import requests
   import browser_cookie3
   
   # testing xpath -> web console -> $x("//a[@href='#ps-container']")
   # python3 -m seleniumwire extractcert
   # then manually import it under authorities
   
   
   def assert_level(level):
       allowed_levels = ["beginner", "intermediate", "advanced", None]
       assert level in allowed_levels, "allowed levels: 'beginner', 'intermediate', 'advanced', 'None (all levels)'"
       return level
   
   
   def assert_sort_on(sort_by):
       allowed_sort_by = ["relevance", "newest", "popularity"]
       assert sort_by in allowed_sort_by, 'allowed sorts: "relevance", "newest", "popularity"'
       return sort_by
   
   
   def assert_search_period(chosen_time_span):
       """choose between 6M, 1y, 2y or None='all dates'"""
       allowed_choices = ["6M", "1y", "2y", None]
       assert (chosen_time_span in allowed_choices), "allowed choices: 6M, 1y, 2y or None(all dates)"
       return chosen_time_span
   
   
   def url_prep(txt):
       return urllib.parse.quote_plus(txt)
   
   
   class ScrapeFirefox:
   
       def __init__(self, start_page, topics):
   
           self.home = os.getenv('HOME')
           self.start_page = start_page
           self.topics = topics
           self.urls_on_topic = {topic: [] for topic in self.topics}  # initialize dict with topics list
           # profile folder visible in "about:profiles"
           self.profile = webdriver.FirefoxProfile(self.home + '/.mozilla/firefox/mwnbnmdi.default-release')
           self.ff_binary = FirefoxBinary('/usr/bin/firefox')
           self.profile.DEFAULT_PREFERENCES['frozen']['extensions.autoDisableScopes'] = 0
           # find all configuration items here: http://kb.mozillazine.org/Firefox_:_FAQs_:_About:config_Entries
           self.profile.accept_untrusted_certs = True
           self.profile.set_preference('extensions.enabledScopes', 15)
           # http://kb.mozillazine.org/Network.proxy.type
           self.profile.set_preference("network.proxy.type", 5)
           self.download_location = self.home + "/cbts"
           self.profile.set_preference("browser.download.folderList", 2)  # don't use default Downloads directory
           self.profile.set_preference("browser.download.manager.showWhenStarting", False)  # turns of showing download progress
           self.profile.set_preference('browser.download.dir', self.download_location)  # sets the directory for downloads
           # automatically download the files of the selected mime-types
           self.profile.set_preference('browser.helperApps.neverAsk.saveToDisk',
                 'video/mp4,audio/mp4,video/webm,video/mp2t,audio/aac,application/x-mpegurl,application/vnd.apple.mpegurl')
           # self.profile.set_preference("browser.helperApps.alwaysAsk.force", False)
           # self.profile.set_preference("browser.download.panel.shown", False)
           # self.profile.set_preference("browser.download.manager.alertOnEXEOpen", False)
           # self.profile.set_preference("browser.download.manager.focusWhenStarting", False)
           # self.profile.set_preference("browser.download.manager.useWindow", False)
           # self.profile.set_preference("browser.download.manager.showAlertOnComplete", False)
           # self.profile.set_preference("browser.download.manager.closeWhenDone", True)  # Close the Download Manager when all downloads are complete
           self.ff_options = webdriver.FirefoxOptions()
           self.ff_options.set_preference("extensions.lastAppBuildId", "<appID> -1")
           self.driver = webdriver.Firefox(firefox_profile=self.profile, firefox_binary=self.ff_binary,
                                           options=self.ff_options)
           self.go_to(self.start_page)
           self.store = shelve.open("my_topic")
   
       def go_to(self, page):
           self.driver.get(page)
   
       def switch_frame(self, css_id):
           frame_to_use = self.driver.find_element_by_id(css_id)
           self.driver.switch_to.frame(frame_to_use)
   
       def save(self, k, v):
           self.store[k] = v
   
       def no_push_notifications(self):
           self.switch_frame("webpush-onsite")
           push_notifications = self.driver.find_element_by_xpath("//button[normalize-space()='No thanks']")
           push_notifications.click()
           self.driver.switch_to.default_content()
   
       def handle_notification_popup(self):
           notifications_frame = self.driver.find_elements_by_id("webpush-onsite")  # browse button/image
           if len(notifications_frame) > 0:
               self.wait_until_el_available_id("webpush-onsite")
               self.no_push_notifications()
           else:
               self.wait_until_el_available_id("prism-explore")
   
       def wait_until_el_available_id(self, css_id):
           element = WebDriverWait(driver=self.driver, timeout=5).until(EC.presence_of_element_located((By.ID, css_id)))
           "avoid elem not detected errors"
   
       def wait_until_el_available_select(self, css_select):
           element = WebDriverWait(driver=self.driver, timeout=5).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                                        css_select)))
   
       def wait_until_el_available_xpath(self, css_xpath):
           element = WebDriverWait(driver=self.driver, timeout=5).until(EC.presence_of_element_located((By.XPATH,
                                                                                                        css_xpath)))
   
       def get_pages_on(self, topic):
           search_bar = self.driver.find_element_by_xpath("//input[@id='prism-search-input']")
           search_bar.clear()
           self.slow_type(search_bar, topic, 0.122)
           search_bar.send_keys(Keys.RETURN)
   
       def right_click_on(self, element, move_up=1):
           act = ActionChains(self.driver)
           act.context_click(element)
           for up in range(0, move_up):
               act.send_keys(Keys.ARROW_DOWN)
           act.send_keys(Keys.RETURN).build().perform()
   
       def get_no_of_pages_on_topic(self, current_html):
           xpath_no_pages = "//a[@href='#ps-container']"
           regex_course_names = r"(?:<h3 class=\".+?\".*?100%;\">)(.*?)(?:</span><span)"
           no_of_courses = len(re.findall(regex_course_names, current_html))
           if 1 <= no_of_courses <= 25:
               no_pages_on_topic = 1
               return no_pages_on_topic
           else:
               no_pages_on_topic = len(self.driver.find_elements_by_xpath(xpath_no_pages))
               return no_pages_on_topic
