import click, requests, colorama
from bs4 import BeautifulSoup as b
from urllib.parse import urljoin

@click.command()
@click.argument("target")
def crawl(target):
 click.echo(colorama.Fore.GREEN + r"""
  ________  ________  ___  ________  _______   ________  ___       __   _______   ________     
|\   ____\|\   __  \|\  \|\   ___ \|\  ___ \ |\   __  \|\  \     |\  \|\  ___ \ |\   __  \                              
\ \  \___|\ \  \|\  \ \  \ \  \_|\ \ \   __/|\ \  \|\  \ \  \    \ \  \ \   __/|\ \  \|\ /_   
 \ \_____  \ \   ____\ \  \ \  \ \\ \ \  \_|/_\ \   _  _\ \  \  __\ \  \ \  \_|/_\ \   __  \  
  \|____|\  \ \  \___|\ \  \ \  \_\\ \ \  \_|\ \ \  \\  \\ \  \|\__\_\  \ \  \_|\ \ \  \|\  \ 
    ____\_\  \ \__\    \ \__\ \_______\ \_______\ \__\\ _\\ \____________\ \_______\ \_______\
   |\_________\|__|     \|__|\|_______|\|_______|\|__|\|__|\|____________|\|_______|\|_______|
   \|_________|                                                                               
 
 - Python Crawler

 """)
 # List of links to crawl
 queue = [target]
 # Make a set, where we'll stock the visited links
 visited = set()
 # Do the following code only if queue isn't empty
 while queue:
  # Get the first element of the queue and delete it
  url = queue.pop(0)
  # If the url has been visited, restart the boucle
  if url in visited:
     continue
  # Add the url as a visited url
  visited.add(url)
  # Print the url
  click.echo(colorama.Fore.GREEN + "[+] Crawling " + colorama.Fore.WHITE + url)
  # Get the HTML of the page
  page = requests.get(url)
  soup = b(page.text, "html.parser")
  # Get all the links in the HTML
  links = soup.find_all("a")
  for link in links:
    # For example, if the link is "/page", this line add the base of the url before "/page"
    new_url = urljoin(url, link["href"])
    # Check if the url is'nt alredy in the queue or is alredy visited
    if new_url not in queue and new_url not in visited:
          # If the url is'nt alredy in the queue, this line add it to the queue
      queue.append(new_url)


    
    



if __name__ == "__main__":
    crawl()