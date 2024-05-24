import requests
import json
import os
cookies = {
    'PREF': 'hl=en&tz=UTC',
    'SOCS': 'CAI',
    'GPS': '1',
    'YSC': 'ypCO9qGoKSY',
    'VISITOR_INFO1_LIVE': 'qBJvehrqV6s',
    'VISITOR_PRIVACY_METADATA': 'CgJJThIEGgAgKA%3D%3D',
}
headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'com.google.ios.youtube/19.09.3 (iPhone14,3; U; CPU iOS 15_6 like Mac OS X)',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-us,en;q=0.5',
    'Sec-Fetch-Mode': 'navigate',
    'X-Youtube-Client-Name': '5',
    'X-Youtube-Client-Version': '19.09.3',
    'Origin': 'https://www.youtube.com',
}
params = {
    'key': 'AIzaSyB-63vPrdThhKuerbB2N_l7Kwwcxj6yUAc',
    'prettyPrint': 'false',
}
json_data = {
    'context': {
        'client': {
            'clientName': 'IOS',
            'clientVersion': '19.09.3',
            'deviceModel': 'iPhone14,3',
            'userAgent': 'com.google.ios.youtube/19.09.3 (iPhone14,3; U; CPU iOS 15_6 like Mac OS X)',
            'hl': 'en',
            'timeZone': 'UTC',
            'utcOffsetMinutes': 0,
        },
    },
    'videoId': '3jc1Q_RRxgI',
    'playbackContext': {
        'contentPlaybackContext': {
            'html5Preference': 'HTML5_PREF_WANTS',
        },
    },
    'contentCheckOk': True,
    'racyCheckOk': True,
}
response = requests.post(
    'https://www.youtube.com/youtubei/v1/player',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
)
#pr = json.loads(response.text)["streamingData"]["hlsManifestUrl"]

pr = response.json()['streamingData']["adaptiveFormats"]
l = []
for __ in pr:
    if "1080p" in str(__) and "mp4" in str(__):
        l.append(__)
    if "AUDIO_QUALITY_MEDIUM" in str(__) and not 'isDrc' in str(__):
        l.append(__)
video = l[0]['url']
audio = l[-1]['url']

#os.system(f"ffmpeg -re -i '{pr}' -vf \"transpose=1,transpose=1,transpose=1,transpose=1,drawtext=fontfile=_.ttf:text='FunnyBunny - YT':fontcolor=white:fontsize=68:box=1:boxcolor=black@0.5:boxborderw=5:x=w-tw:y=h-th\" -map 0:v:4 -map 0:a -threads 4 -crf 0 -b:v 10000k -c:a aac -g 30 -b:a 384k -f tee \"[select=v:4,a:1] rtmp://a.rtmp.youtube.com/live2/j32f-zj48-1axx-m9g1-1zms [select=v:4,a:1] rtmp://a.rtmp.youtube.com/live2/zvmf-1yjp-jzek-01pw-b4js\"")


#os.system(f"ffmpeg -re -i '{video}' -i '{audio}' -vf \"transpose=1,transpose=1,transpose=1,transpose=1,drawtext=fontfile=_.ttf:text='FunnyBunny - YT':fontcolor=white:fontsize=68:box=1:boxcolor=black@0.5:boxborderw=5:x=w-tw:y=h-th\" -threads 4 -crf 0 -b:v 10000k -c:a aac -g 30 -b:a 384k -f flv rtmp://a.rtmp.youtube.com/live2/j32f-zj48-1axx-m9g1-1zms -vcodec copy -acodec copy -f flv rtmp://a.rtmp.youtube.com/live2/zvmf-1yjp-jzek-01pw-b4js")


os.system(f"ffmpeg -re -i '{video}' -i '{audio}' -vf \"transpose=1,drawtext=fontfile=_.ttf:text='FunnyBunny - YT':fontcolor=white:fontsize=68:box=1:boxcolor=black@0.5:boxborderw=5:x=w-tw:y=h-th\" -threads 4 -crf 0 -b:v 10000k -c:a aac -g 30 -b:a 384k -f flv rtmp://edgetee-upload-maa2-1.xx.fbcdn.net:443/rtmp/17858955786159906?s_bl=1&s_fbp=tir3-1&s_prp=maa2-1&s_spl=1&s_sw=0&s_tids=1&s_vt=ig&a=AbwpnI3c31kiAZoN")


#\"[f=flv:onfail=ignore]rtmp://a.rtmp.youtube.com/live2/j32f-zj48-1axx-m9g1-1zms|[f=flv:onfail=ignore]rtmp://a.rtmp.youtube.com/live2/zvmf-1yjp-jzek-01pw-b4js\"")

#-f flv rtmp://a.rtmp.youtube.com/live2/j32f-zj48-1axx-m9g1-1zms")

