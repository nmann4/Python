import time
import requests
import urllib
import bs4

start_url = "https://en.wikipedia.org/wiki/Special:Random"
target_url = "https://en.wikipedia.org/wiki/Philosophy"

def continue_crawl(search_history, target_url, max_steps=25):
    if len(search_history)>max_steps:
        print("Search has gone on too long, aborting the search!")
        return False
    elif search_history[-1] == target_url:
        print("we've found the target article!")
        return False
    elif search_history[-1] in search_history[:-1]:
        print("we're in a cycle, aborting the search!")
        return False
    else:
        return True

def find_first_link(url):
    # get the HTML from "url", use the request library
    response = requests.get(url)
    html = response.text
    soup = bs4.BeautifulSoup(html, "html.parser")

    # this div contains the article's body
    content_div = soup.find(id="mw-content-text")

    article_link = None
    
    for element in content_div.find_all("p", recursive=False):
        if element.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get("href")
            break

    if not article_link:
        return
    # return the first link as a string, or return None if there is no link
    first_link = urllib.parse.urljoin("https://en.wikipedia.org/", article_link)
    return first_link

def web_crawl():
    while continue_crawl(article_chain, target_url):
        # download html of last article in the article_chain
        # find the first link in that html
        first_link = find_first_link(article_chain[-1])
        # add the first link to the article chain
        article_chain.append(first_link)
        # delay for about two seconds
        time.sleep(2)

#Run the program
article_chain = [start_url]
while continue_crawl(article_chain, target_url):
    print(article_chain[-1])

    first_link = find_first_link(article_chain[-1])
    if not first_link:
        print("We have found an article with no links, aborting!")
        break

    article_chain.append(first_link)
    time.sleep(2)
    















