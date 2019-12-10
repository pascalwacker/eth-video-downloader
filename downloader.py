import json
import requests
from pprint import pprint
from robobrowser import RoboBrowser
import re
import os
from urllib.request import urlretrieve

def dlProgress(count, blockSize, totalSize):
    print('\r' + str(round(count * blockSize * 100 / totalSize)) + '%: ' + str('#' * round(count * blockSize * 100 / totalSize / 5)) + str('_' * (20-round(count * blockSize * 100 / totalSize / 5))), end="")

def main():
    data = json.load(open('/app/config.json'))

    mode = 'skip'
    if data['existing'] and data['existing'] == 'overwrite':
        mode = 'overwrite'

    if len(data['targets']):
        s = requests.Session()
        s.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'
        s.headers['Host'] = 'video.ethz.ch'
        s.headers['DNT'] = '1'
        s.headers['Upgrade-Insecure-Requests'] = '1'
        browser = RoboBrowser(history=True,session=s)
        
        for target in data['targets']:
            try:
                browser.open(target['url'])

                entries = browser.select('#filter-container > .newsListBox .info > a')
                for anker in entries:
                    browser.follow_link(anker)

                    video = {}
                    videoName = browser.select('.accordion-details > div.accordionContent > h3')[0].text
                    video['name'] = re.sub('[^0-9A-Za-z-_\.]+', '', re.sub(' ', '-', videoName))
                    video['src'] = browser.select('.accordion-media .mmp-downloads ul > li.video > a')[0]['href']
                    videoOriginalDate = re.sub('[^0-9\.]+', '', (browser.select('.accordion-details > div.accordionContent > p')[2].text))
                    videoDate = (videoOriginalDate).split('.')
                    video['date'] = videoDate[2] + '-' + videoDate[1] + '-' + videoDate[0]

                    if not os.path.exists('/app/downloads/' + video['name']):
                        os.makedirs('/app/downloads/' + video['name'])
                    
                    if mode == 'overwrite' or not os.path.exists('/app/downloads/' + video['name'] + '/' + video['name'] + '_' + video['date'] + '.mp4'):
                        print('\ndownloading ' + videoName + ' ' + videoOriginalDate + ': ' + video['src'])
                        urlretrieve(video['src'], '/app/downloads/' + video['name'] + '/' + video['name'] + '_' + video['date'] + '.mp4', reporthook=dlProgress)
            except:
                print('error at ' + target['url'])
    else:
        print('no targets given')

if __name__ == '__main__':
    main()
