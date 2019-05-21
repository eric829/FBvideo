import requests
import re
from flask import Flask, request, send_file,make_response
import shutil
import mimetypes
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) 
def download():
    if request.method == 'POST': 
        res = requests.get(request.values['url'])
        s = re.search('hd_src:"(https://.*?)",',res.text)
        res2 = requests.get(s.group(1),stream =True)
        response = make_response(res2.content)
        mime_type = mimetypes.guess_type(request.values['filename']+'.mp4')[0]
        response.headers['Content-Type'] = mime_type
        response.headers['Content-Disposition'] = 'attachment; filename={}'.format(request.values['filename']+'.mp4'.encode().decode('latin-1'))
        return response

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
    app.run(host='0.0.0.0', debug=True)
