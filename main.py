import requests
import re
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
    'videoId': 'iOqPkwC7NAM',
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

#pr = response.json()['streamingData']["adaptiveFormats"]
#l = []
#for __ in pr:
#    if "1080p" in str(__) and "mp4" in str(__):
#        l.append(__)
#    if "AUDIO_QUALITY_MEDIUM" in str(__) and not 'isDrc' in str(__):
#        l.append(__)
#video = l[0]['url']
#audio = l[-1]['url']
#print(video)
#print(audio)



#os.system(f"ffmpeg -re -i '{pr}' -vf \"transpose=1,transpose=1,transpose=1,transpose=1,drawtext=fontfile=_.ttf:text='FunnyBunny - YT':fontcolor=white:fontsize=68:box=1:boxcolor=black@0.5:boxborderw=5:x=w-tw:y=h-th\" -map 0:v:4 -map 0:a -threads 4 -crf 0 -b:v 10000k -c:a aac -g 30 -b:a 384k -f tee \"[select=v:4,a:1] rtmp://a.rtmp.youtube.com/live2/j32f-zj48-1axx-m9g1-1zms [select=v:4,a:1] rtmp://a.rtmp.youtube.com/live2/zvmf-1yjp-jzek-01pw-b4js\"")


#os.system(f"ffmpeg -re -i '{video}' -i '{audio}' -vf \"transpose=1,transpose=1,transpose=1,transpose=1,drawtext=fontfile=_.ttf:text='FunnyBunny - YT':fontcolor=white:fontsize=68:box=1:boxcolor=black@0.5:boxborderw=5:x=w-tw:y=h-th\" -threads 4 -crf 0 -b:v 10000k -c:a aac -g 30 -b:a 384k -f flv rtmp://a.rtmp.youtube.com/live2/zvmf-1yjp-jzek-01pw-b4js -vcodec copy -acodec copy -f flv ")


#os.system(f"ffmpeg -rtbufsize 256M -re -i '{pr}' -vf \"transpose=1,drawtext=fontfile=_.ttf:text='FunnyBunny - YT':fontcolor=white:fontsize=68:box=1:boxcolor=black@0.5:boxborderw=5:x=w-tw:y=h-th\" -threads 4 -map 0:p:5 -crf 0 -b:v 10000k -c:a aac -g 30 -b:a 384k -f flv \"rtmps://edgetee-upload-maa2-1.xx.fbcdn.net:443/rtmp/17936757614744903?s_bl=1&s_fbp=tir3-1&s_prp=maa2-1&s_spl=1&s_sw=0&s_tids=1&s_vt=ig&a=AbyZGAvU6xCVbZ-U\"")


#os.system(f"ffmpeg -re -i '{pr}' -vf transpose=1 -map 0:p:5 -pix_fmt yuv420p -threads 4 -vb 400k -deinterlace -c:v libx264 -c:a aac -g 30 -b:a 384k -f flv \"rtmp://edgetee-upload-maa2-1.xx.fbcdn.net:443/rtmp/17936757614744903?s_bl=1&s_fbp=tir3-1&s_prp=maa2-1&s_spl=1&s_sw=0&s_tids=1&s_vt=ig&a=AbyZGAvU6xCVbZ-U\"")







from pathlib import Path
import json
import requests
session = requests.session()

#path = Path("C.json")
Cookies = {'csrftoken': 'p8iGdJiFBzQZ6HjvW0Sn6ksBob9BXWLu', 'rur': '"PRN\\0546049028904\\0541748703571:01f77fd1d76b4bc32fbf3eb54367042b24be2c562d9f74125fdb00e867b7828ab0fa21b2"', 'mid': 'ZkMXSgABAAG79YazZZHgTeF9XTVM', 'ds_user_id': '6049028904', 'ig_did': 'FE5CE32B-19AD-4C1D-A5A7-0558304197FF', 'sessionid': '6049028904%3A5prK54orcy4nAI%3A1%3AAYdboek4ImZ4nzz2bgamWmfRgbIgGBTM2Yla-jnPsw', 'datr': 'SRdDZm6LjndXwTVI4jb_5qaY', 'ig_nrcb': '1', 'ig_lang': 'en', 'no_restriction': '1', 'ps_l': '1', 'ig_direct_region_hint': '"ASH\\05451941737982\\0541748243307:01f77445d6f6ca9c27e5671f5349acaecf644f69edcb09ad4a3884450f4dfd8580c5887e"', 'dpr': '2.3135459423065186', 'wd': '1048x2022', 'shbid': '"12619\\0546049028904\\0541748703511:01f7bb09cd5c9ce999bb1f3c76265bb381780f2b74e414762a67c277e40091574b491e58"', 'shbts': '"1717167511\\0546049028904\\0541748703511:01f7c3659e0d3c5d800e44b4553d00755c3266a674645f172f4053f8a71c294ab760beb4"'}  #json.loads(json.dumps(path.read_bytes()))


csrf = Cookies["csrftoken"]
id = Cookies["ds_user_id"]

print(csrf)
print(id)
#print(cookies)  # save them to file as JSON
cookies = requests.utils.cookiejar_from_dict(Cookies)
#print(cookies)
session.cookies.update(cookies)
#print(session.headers) # load cookiejar to current session
#print(session.get("https://www.instagram.com/settings/help/account_status/?hl=en").text)  # te
#import requests


headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache',
    'Priority': 'u=1, i',
    'Referer': 'https://www.instagram.com/settings/help/account_status/?hl=en',
    'sec-ch-prefers-color-scheme': 'light',
#    'sec-ch-ua': '"Chromium";v="125", "Not.A/Brand";v="24"',
#    'sec-ch-ua-full-version-list': '"Chromium";v="125.0.6422.60", "Not.A/Brand";v="24.0.0.0"',
#    'sec-ch-ua-mobile': '?0',
#    'sec-ch-ua-model': '""',
#    'sec-ch-ua-platform': '"Linux"',
#    'sec-ch-ua-platform-version': '"4.19.191"',
#    'sec-fetch-dest': 'empty',
#    'sec-fetch-mode': 'cors',
#    'sec-fetch-site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
#    'x-asbd-id': '129477',
    'x-csrftoken': f'{csrf}',
    'x-ig-app-id': '936619743392459',
#    'x-ig-app-id': '743845927482847',
 #   'x-ig-www-claim': 'hmac.AR1_ueWdmxzSLaL-obCxlwYWH_OHumpsDQC2featPzTqv7Ay',
    'X-Requested-With': 'XMLHttpRequest',
}

session.headers = headers
#print(session.headers)
#session.headers.update({"x-csrftoken": f"{csrf}"})

params = {
    'target_user_id': f'{id}',
    'hl': 'en',
}
#print(session.headers)
#session.cookies.update({"wd": "1280x720", "locale": "en_US", })
#print(session.cookies)
#response = session.get('https://www.instagram.com/api/v1/live/web_info/', params=params)
#print(response.text)
data = {
    'broadcast_message': 'pubg live',
    'internal_only': 'false',
    'source_type': '203',
    'broadcast_type': 'RTMP',
    'visibility': '0',
#    'disable_speed_test': '1',
#    'is_premium': '1'
}


res = session.post("https://www.instagram.com/api/v1/live/create/", params={'hl': 'en'}, data=data)
p6 = res.json()
broadcastid = p6['broadcast_id']
upload_url = p6['upload_url']
print(upload_url)
print('braodcast : ', broadcastid)





#dat ={'should_send_notifications': 1}

rr = session.post(f"https://www.instagram.com/api/v1/live/{broadcastid}/start/", data={'should_send_notifications': 1})
print(rr.text)



#t5 = session.post("https://www.instagram.com/api/v1/live/{b}/start/")
#t5 = session.post("https://www.instagram.com/api/v1/live/18024036962482997/end_broadcast/")
#print(t5.text)



#os.system(f"ffmpeg -re -i '{video}' -i '{audio}' -vf transpose=1 -c:v libx264 -g 30 -c:a aac -f flv '{upload_url}'")

#rt = requests.get(pr)


#import requests

headerszzz = {
    'User-Agent': 'Instagram 332.0.0.38.90 Android (34/14; 396dpi; 1080x2238; vivo; V2311; V2225; mt6833; en_IN; 601420827)',
    'X-IG-App-Locale': 'en_IN',
    'X-IG-Device-Locale': 'en_IN',
    'X-IG-Mapped-Locale': 'en_US',
#    'X-Pigeon-Session-Id': 'UFS-02903322-bed8-4b37-8d5c-f96479db3fa1-3',
    'X-Pigeon-Rawclienttime': '1717007056.986',
    'X-IG-Bandwidth-Speed-KBPS': '1536.000',
    'X-IG-Bandwidth-TotalBytes-B': '0',
    'X-IG-Bandwidth-TotalTime-MS': '0',
    'X-Bloks-Version-Id': '1d85eb04419079358b68b92be6f523d99f895154273fd6dd5eb7d3df20e4453c',
#    'X-IG-WWW-Claim': 'hmac.AR2j_aJEeP4IOD_V9ZkjM_PDbpowSWqTx36KewZPXCJoUEwO',
    'X-Bloks-Is-Prism-Enabled': 'true',
    'X-Bloks-Prism-Button-Version': 'CONTROL',
    'X-Bloks-Prism-Colors-Enabled': 'false',
    'X-Bloks-Prism-Font-Enabled': 'false',
    'X-Bloks-Is-Layout-RTL': 'false',
    'X-IG-Device-ID': 'b210e33c-e663-413f-8f7e-4dad05d5e905',
    'X-IG-Family-Device-ID': '9737c626-f220-4885-a90e-64f87ab67dcc',
    'X-IG-Android-ID': 'android-1909c08fe2b2aea3',
    'X-IG-Timezone-Offset': '19800',
#    'X-IG-Nav-Chain': 'MainFeedFragment:feed_timeline:1:cold_start:1717006919.1:::1717006919.1,GalleryPickerFragment:gallery_picker:2:camera_tab_bar:1717006963.978:::1717006963.978,GalleryPickerFragment:gallery_picker:3:button:1717006965.962:::1717006965.962,QuickCaptureFragment:live_precapture_camera:4:button:1717006985.125:::1717007050.924,IgLiveCaptureFragment:live_broadcast:8:button:1717007056.699:::1717007056.699',
    'X-IG-CLIENT-ENDPOINT': 'IgLiveCaptureFragment:live_broadcast',
#    'X-IG-SALT-IDS': '332021232,974466465,332016876,332012435',
#    'X-IG-SALT-LOGGER-IDS': '926483817,20119555,17631244,20133815,321323009,3213622,883764695,25625981,915222759,76221888,25952257,42991646',
    'X-FB-Connection-Type': 'MOBILE.LTE',
    'X-IG-Connection-Type': 'MOBILE(LTE)',
    'X-IG-Capabilities': '3brTv10=',
    'X-IG-App-ID': '567067343352427',
    'Priority': 'u=3',
    'X-FB-HTTP-Engine': 'Liger',
    'Accept-Language': 'en-IN, en-US',
    'Authorization': 'Bearer IGT:2:eyJkc191c2VyX2lkIjoiNjA0OTAyODkwNCIsInNlc3Npb25pZCI6IjYwNDkwMjg5MDQlM0FvOXVlTzNzSHRrOVc4eiUzQTYlM0FBWWZlb2Z1TUpUN0pjNTdDbXpLdHM3cFNqcnhqc0F5WGRiX2lidlV3VncifQ==',
    'X-MID': 'ZlnQKgABAAEhSwL9ZL9G2FUg_73h',
#    'IG-U-IG-DIRECT-REGION-HINT': 'ASH,51941737982,1748541502:01f7fc4095173790b593d391c7102f67582d335bd4d9d67643cfa67fe84f563c6805014d',
    'IG-U-DS-USER-ID': '6049028904',
    'IG-INTENDED-USER-ID': '6049028904',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Connection': 'Keep-Alive',
}

datasss = {
    'user_pay_enabled': 'false',
#    'camera_session_id': 'b4787b89-0861-49fe-ac6d-dd9786cbb35b',
    'source_type': '5',
    'preview_height': '1920',
#    '_uuid': 'b210e33c-e663-413f-8f7e-4dad05d5e905',
#    'should_use_rsys_rtc_infra': 'false',
    'broadcast_type': 'RTMP',
    'broadcast_message': 'Pubg Live',
    'preview_width': '1080',
    'sup_active': 'false',
    'internal_only': '0',
    'visibility': '0',
}

#sponse = requests.post('https://i.instagram.com/api/v1/live/create/', headers=headerszzz, data=datasss).json()

#broacast = sponse["broadcast_id"]
#rtmp = sponse["upload_url"]
#resd = requests.post(f'https://i.instagram.com/api/v1/live/{broacast}/start/', #headers=headerszzz)
#print(resd.text)





#RES = re.findall("\d{2,}x([0-9]+)", requests.get(pr).text).index('1080')
#os.system(f"ffmpeg -rtbufsize 1G -re -i '{pr}' -map 0:p:{int(RES)} -vf transpose=1 -vcodec libx264 -acodec copy -g 30 -f flv '{upload_url}'")
#os.system(f"ffmpeg -rtbufsize 1G -re -i '{pr}' -map 0:p:{int(RES)-1} -vf transpose=1 -acodec aac -g 30 -f flv 'rtmp://a.rtmp.youtube.com/live2/qtaa-xx6x-h99h-hjtp-1wf1' -vcodec copy -acodec copy -f flv '{rtmp}'")
os.system(f"ffmpeg -re -i '{pr}' -map 0:p:4 -vf \"transpose=1,transpose=1,transpose=1,transpose=1\" -c:v libx264 -threads 4 -crf 0 -b:v 10000k -c:a aac -g 30 -b:a 384k -f flv 'rtmp://a.rtmp.youtube.com/live2/qtaa-xx6x-h99h-hjtp-1wf1' -vcodec copy -acodec copy -f flv '{upload_url}'")
