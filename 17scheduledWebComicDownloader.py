#! python3
# # scheduledWebComicDownloader - checks websites of web comic, and
# # automatically downloads image if site was updated since last visit.

import requests, os, bs4, threading
os.makedirs('xkcd', exist_ok=True)    # store comics in ./xkcd


# Downloads comic image if not found already in directory.
def check_for_update(comicUrl):
    # Get image filename.
    fileName = os.path.basename(comicUrl)

    # Check if today's comic exists in directory.
    if fileName in os.listdir('xkcd'):
        print('No updates today. Most recent comic is at %s.' % comicUrl)

    # Else download today's comic.
    else:
        print('Downloading %s...' % comicUrl)

        res = requests.get(comicUrl)
        res.raise_for_status()
        imageFile = open(os.path.join('xkcd', fileName), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

# Get XKCD comics
def downloadXkcd():
    # Download the page.
    print('Downloading page https://xkcd.com/')
    res = requests.get('https://xkcd.com/')
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = comicElem[0].get('src')
        check_for_update(comicUrl)

downloadXkcd()

'''# Create and start the Thread objects.
downloadThreads = []             # a list of all the Thread objects
for i in range(0, 140, 10):    # loops 14 times, creates 14 threads
    start = i
    end = i + 9
    if start == 0:
        start = 1 # There is no comic 0, so set it to 1.
    downloadThread = threading.Thread(target=downloadXkcd, args=(start, end))
    downloadThreads.append(downloadThread)
    downloadThread.start()
# Wait for all threads to end.
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')'''