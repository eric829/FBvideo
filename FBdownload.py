import requests
import re
from flask import Flask, request
import shutil

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) 
def download():
    if request.method == 'POST': 
        res = requests.get(request.values['url'])
        s = re.search('hd_src:"(https://.*?)",',res.text)
        res2 = requests.get(s.group(1),stream =True)
        f = open(request.values['filename']+'.mp4','wb')
        shutil.copyfileobj(res2.raw,f)
        f.close
        return 'Download is finish'

    return "</br>" \
            "</br>" \
            "</br>" \
            "</br>" \
            "</font><form align='center' method='post' action='/'><font size='7' color='blue'>Url     <input type='text' name='url' />" \
            "</br>"\
            "<font size='7' color='blue'>Filename</font> <form align='center' method='post' action='/'> <input type='text' name='filename' />" \
            "</br>" \
            "<button type='submit'>Submit</button></form>"

if __name__ == '__main__':
    app.run()
