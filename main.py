import requests
from bs4 import BeautifulSoup

apn = "https://www.apnews.com"
reut = "https://www.reuters.com"
cnbc = "https://www.cnbc.com"
npr = "https://www.npr.org"
bbc = "https://www.bbc.com/news"



def newssite():
  sites = {
  'ap' : "https://www.apnews.com",
  'reut' : "https://www.reuters.com",
  'cnbc' : "https://www.cnbc.com",
  'npr' : "https://www.npr.org",
  'bbc' : "https://www.bbc.com/news"
  }
  return sites

########################################################################


def getapn():
  stories = {}

  page = requests.get(apn)
  soup = BeautifulSoup(page.content, 'html.parser')

  story1 = soup.find("div", {"class": "CardHeadline"})
  story1link = story1.find('a').get('href')
  story1title = story1.find('h1').text
  stories[story1title] = apn + story1link

  story2 = soup.findAll("div", {"class": "RelatedStory"})

  for i in story2:
    link = i.find("a").get("href")
    title = i.find("div").text
    
    stories[title] = apn + link

  return stories


########################################################################


def getreut():
  stories = {}

  page = requests.get(reut)
  soup = BeautifulSoup(page.content, 'html.parser')

  story1 = soup.find("section", {"id": "topStory"})
  story1a = story1.find("h2", {"class": "story-title"})
  story1link = story1a.find("a").get("href")
  story1title = story1a.find("a").text

  stories[story1title] = reut + story1link


  story2 = soup.find("div", {"class": "news-headline-list"})
  links = story2.findAll("a")

  for i in links:
    title = i.find("h3").text.strip()
    link = i.get("href")
    stories[title] = reut + link

  return stories

########################################################################


def getcnbc():
  stories = {}

  page = requests.get(cnbc)
  soup = BeautifulSoup(page.content, 'html.parser')

  story1 = soup.find("h2", {"class": "HeroLedePlusThreeLeadItem-title"})
  story1link = story1.find("a").get("href")
  story1title = story1.find("div").text
  stories[story1title] = story1link

  story2 = soup.find("div", {"class": "HeroLedePlusThreeDeck-stories"})
  links = story2.findAll("div", {"class": "HeroLedePlusThreeDeckItem-descriptionContainer"})


  for i in links:
    title = i.find("a").get("title")
    link = i.find("a").get("href")
    stories[title] = link

  return stories

##########################################################################


def getnpr():
  stories = {}

  page = requests.get(npr)
  soup = BeautifulSoup(page.content, 'html.parser')

  story1 = soup.find("div", {"class": "story-wrap"})
  story1a = story1.find("div", {"class": "story-text"})
  story1title = story1a.find("h3", {"class": "title"}).text
  story1link = story1a.findAll("a")
  
  stories[story1title] = story1link[1].get("href")
  

  story2 = soup.find("section", {"class": "featured-group"})

  story2links = story2.findAll("div", {"class": "story-text"})
  story2titles = story2.findAll("h3", {"class": "title"})



  for i in range(len(story2links)):
    links = story2links[i].findAll("a")
    link = links[1].get("href")
    stories[story2titles[i].text] = link

  return stories


##########################################################################


def getbbc():
  stories = {}
  page = requests.get(bbc)
  soup = BeautifulSoup(page.content, 'html.parser')

  story1 = soup.find("div", {"class": "nw-c-top-stories--international"})

  for i in story1:
    if i.find("a") != None:
      link = i.find("a")
      link1 = link.get("href")
      title = link.find("h3").text

      if link1[:5] != 'https':
        site = bbc.replace('/news', '') + link1
        stories[title] = site
      else:
        stories[title] = link1

  return stories


# print(getapn())
# print(getreut())
# print(getcnbc())
# print(getnpr())
# print(getbbc())