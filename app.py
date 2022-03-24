import requests
import json
from bs4 import BeautifulSoup
import requests
import subprocess

# save_data = []

url = 'https://api.si.edu/openaccess/api/v1.0/search?'
starts = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]
#starts = [0, 1000]
for s in starts:
    payload = {
            'api_key': 'zspEuNL8WScYkEhKp2tYR1SkpCMYVDdKN3I0RWcN',
            'start': s,
            'rows': 1000,
            'q': 'space' # SEARCH QUERY !!!
    }

    r = requests.get(url, params=payload)

    data = json.loads(r.text)

    for item in data ['response']['rows']:
        if 'online_media_type' in item['content']['indexedStructured']:
            if 'guid' in item['content']['descriptiveNonRepeating']:
               # save_data.append(item)
                print(item['content']['descriptiveNonRepeating']['guid'])
                url = item['content']['descriptiveNonRepeating']['guid']
                print("bs url ==>")
                print(url)
                html = requests.get(url).text
                soup = BeautifulSoup(html, "lxml")

                imgs = soup.findAll("a", {'class':'fullImageLink'})
                for img in imgs:
                    imgUrl = img['href']
                    print('final wget img url ==>')
                    print(imgUrl.replace(" ",""))
                    #cmd = ['wget',imgUrl,'-O '+imgUrl.replace(" ","")+'.jpg']
                    cmd = ['wget', imgUrl]
                    subprocess.Popen(cmd)
                    subprocess.Popen(cmd).communicate()



    #with open('data.json', 'w') as out:
    #    json.dump(save_data,out,indent=2)
