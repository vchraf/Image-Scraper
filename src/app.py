from bs4 import *
import requests 
import os 
from urllib.parse import urlparse
from urlextract import URLExtract
from datetime import datetime


def download_images(images, folder_name): 

    #print(f"Total {len(images)} Image Found!") 
    timestamp = str(datetime.timestamp(datetime.now())).replace(".","")
    if len(images) != 0: 
        for i, image in enumerate(images): 
            image_link = image["data-src"]
            if image_link != "" and ".gif" not in image_link and "badges" not in image_link:
                with open(f"{folder_name}/IMG{timestamp}{i+1}.jpg", "wb+") as f:
                    im = requests.get(image_link)
                    f.write(im.content)
                    print(f"Download : IMG{timestamp}{i+1}")

   
    

def main(): 
    folder_name = input("Enter Folder Name:- ") 
    if not os.path.exists(folder_name):
        os.mkdir(folder_name) 
        nbr=1
    for i in range(1,nbr+1):
        url ="https://www.jumia.ma/pulls-gilets-hommes/?page="+str(nbr)+"#catalog-listing"
        r = requests.get(url) 
        soup = BeautifulSoup(r.text , 'html.parser')
        images =   soup.find_all("img")
        download_images(images, folder_name) 
        print("done with page : ", i)

if __name__ == '__main__': 
       main()