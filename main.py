from bs4 import BeautifulSoup
import requests
import webbrowser as wb


def list_image_links(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    
    # Separation of download links
    image_links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href is not None and 'attach' in href and href.endswith('image')==False:
            image_links.append(href)
    
    # Writing links in a txt file
    with open('my_file.txt', 'a') as my_file:
        for branch in image_links:
            my_file.write(branch + '\n')
            print('File created')
    
def download_links():
    # Download all links
    with open('my_file.txt')as f:
        a = f.readlines()
        for b in a:
            wb.open(b)

i = 0
# Browse through different pages of the topic
while i <= 5175:
    list_image_links(f'https://forum.ubuntu.ir/index.php?topic=211.{i}')
    i = i+15
# Download all of them
download_links()