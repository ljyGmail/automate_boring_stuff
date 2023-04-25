import requests
import os
import bs4

url = 'https://xkcd.com'  # starting url
destFolder = r'data/ch12/xkcd'

os.makedirs(destFolder, exist_ok=True)  # store comics in /data/ch12/xkcd

while not url.endswith('#'):
    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')

    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'https:'+comicElem[0].get('src')
        # Download the image.
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

        # Save the image to /data/ch12/xkcd.
        imageFile = open(os.path.join(destFolder,
                         os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com'+prevLink.get('href')


print('Done.')
