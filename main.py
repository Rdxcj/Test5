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
    'videoId': 'WST_o-9Z49A',
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
pr = json.loads(response.text)["streamingData"]["hlsManifestUrl"]
#os.system(f"ffmpeg -re -i '{pr}' -vf \"transpose=1,transpose=1,transpose=1,transpose=1,drawtext=fontfile=_.ttf:text='FunnyBunny - YT':fontcolor=white:fontsize=68:box=1:boxcolor=black@0.5:boxborderw=5:x=w-tw:y=h-th\" -map 0:v:4 -map 0:a -threads 4 -crf 0 -b:v 10000k -c:a aac -g 30 -b:a 384k -f tee \"[select=v:4,a:1] rtmp://a.rtmp.youtube.com/live2/j32f-zj48-1axx-m9g1-1zms [select=v:4,a:1] rtmp://a.rtmp.youtube.com/live2/zvmf-1yjp-jzek-01pw-b4js\"")
os.system(f"ffmpeg -re -i 'https://rr2---sn-8vq54voxpo-pmhe.googlevideo.com/videoplayback?expire=1716539449&ei=2ftPZtOQMuG49fwP4O2akAM&ip=42.106.177.158&id=o-ADncyM9kxPLB7k4HXnqpoDfaXINy5jJ_XnmW8iPcdRoP&itag=160&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=PU&mm=31%2C29&mn=sn-8vq54voxpo-pmhe%2Csn-8vq54voxpo-h55l&ms=au%2Crdu&mv=m&mvi=2&pl=25&initcwndbps=627500&vprv=1&svpuc=1&mime=video%2Fmp4&rqh=1&gir=yes&clen=529334706&dur=41415.111&lmt=1713802882985600&mt=1716517523&fvip=8&keepalive=yes&c=IOS&txp=6309224&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cvprv%2Csvpuc%2Cmime%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRAIgONv3I9Gc6UyUulfuugcATAGiLyom_p320L2XSm0QLJgCIEjcqqYzfIseocHj8dm34puQkgsIDQ8fwKnUeimAYXU6&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AHWaYeowRQIgNsGMSU4hXNcZmOBOvOzhEl8uGb2Ok9cNNBj1snHksTgCIQDvJtFXsV1Lt2jI1HwDNV7qaHAmEjRI847PMrJ4Q2q1yw%3D%3D' -i 'https://rr2---sn-8vq54voxpo-pmhe.googlevideo.com/videoplayback?expire=1716539449&ei=2ftPZtOQMuG49fwP4O2akAM&ip=42.106.177.158&id=o-ADncyM9kxPLB7k4HXnqpoDfaXINy5jJ_XnmW8iPcdRoP&itag=140&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=PU&mm=31%2C29&mn=sn-8vq54voxpo-pmhe%2Csn-8vq54voxpo-h55l&ms=au%2Crdu&mv=m&mvi=2&pl=25&initcwndbps=627500&vprv=1&svpuc=1&xtags=drc%3D1&mime=audio%2Fmp4&rqh=1&gir=yes&clen=670259602&dur=41415.201&lmt=1713835733630188&mt=1716517523&fvip=8&keepalive=yes&c=IOS&txp=6308224&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cvprv%2Csvpuc%2Cxtags%2Cmime%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRQIhAJULbxm8YmsOYmDXBWhlSkGJN9Cu94rowof8FYmElqTYAiB5sWrLm0PrDXJFnjOdvTp7STYCSzkZB_-UMTZHFYE9zw%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AHWaYeowRQIgNsGMSU4hXNcZmOBOvOzhEl8uGb2Ok9cNNBj1snHksTgCIQDvJtFXsV1Lt2jI1HwDNV7qaHAmEjRI847PMrJ4Q2q1yw%3D%3D'-vf \"transpose=1,transpose=1,transpose=1,transpose=1,drawtext=fontfile=_.ttf:text='FunnyBunny - YT':fontcolor=white:fontsize=68:box=1:boxcolor=black@0.5:boxborderw=5:x=w-tw:y=h-th\" -threads 4 -crf 0 -b:v 10000k -c:a aac -g 30 -b:a 384k -f tee \"[f=flv:onfail=ignore] rtmp://a.rtmp.youtube.com/live2/j32f-zj48-1axx-m9g1-1zms [f=flv:onfail=ignore] rtmp://a.rtmp.youtube.com/live2/zvmf-1yjp-jzek-01pw-b4js\"")



#\"[f=flv:onfail=ignore]rtmp://a.rtmp.youtube.com/live2/j32f-zj48-1axx-m9g1-1zms|[f=flv:onfail=ignore]rtmp://a.rtmp.youtube.com/live2/zvmf-1yjp-jzek-01pw-b4js\"")

#-f flv rtmp://a.rtmp.youtube.com/live2/j32f-zj48-1axx-m9g1-1zms")

