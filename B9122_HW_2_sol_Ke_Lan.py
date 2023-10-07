#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import urllib.request
import requests
from bs4 import BeautifulSoup


# In[2]:


url = "https://press.un.org/en"


# In[3]:


def is_press_release(soup):
    press_release_tag = soup.find('a', {'href': '/en/press-release', 'hreflang': 'en'})
    if press_release_tag:
        return True
    else:
        return False


# In[4]:


def is_plenary_session(soup):
    tag = soup.find('span', class_="ep_name", string="Plenary session")
    if tag:
        return True
    else:
        return False


# In[5]:


def contains_crisis(soup):
    if 'crisis' in soup.get_text().lower():
        return True
    else:
        return False


# In[36]:


def add_link(link, visited, q):
    link_url = link['href']
    if link_url.startswith('/'):
        if q == 'Q1':
            link_url = 'https://press.un.org' + link_url
        elif q == 'Q2':
            link_url = 'https://www.europarl.europa.eu' + link_url
    if not link_url.startswith('#') and link_url not in visited:
        return link_url
    return None


# In[38]:


def find_press_release(url, visited, q):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
    except requests.RequestException:
        return None, []

    press_release = None
    if q == 'Q1' and is_press_release(soup) and contains_crisis(soup):
        press_release = url
    elif q == 'Q2' and is_plenary_session(soup) and contains_crisis(soup):
        press_release = url

    links = []
    for link in soup.find_all('a', href=True):
        new_link = add_link(link, visited, q)
        if new_link:
            links.append(new_link)

    return press_release, links


# In[37]:


def get_press_releases(seed_url, q, print = False):
    visited = set()
    to_visit = [seed_url]
    press_releases = []
    max_ = 800
    now = 0
    while to_visit and len(press_releases) < 10 and now < max_:
        url = to_visit.pop(0)
        if url in visited:
            continue
        visited.add(url)
        if print == True:
            print(url)

        press_release, links = find_press_release(url, visited, q)
        if press_release:
            press_releases.append(press_release)
        to_visit.extend(links)
        now += 1

    return press_releases


# # Q1

# In[24]:


urls_1 = get_press_releases('https://press.un.org/en' , 'Q1')


# In[26]:


for u in urls_1:
    print(u)


# # Q2

# In[33]:


urls_2 = get_press_releases('https://www.europarl.europa.eu/news/en/press-room', 'Q2')


# In[40]:


for u in urls_2:
    print(u)

