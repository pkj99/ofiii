import requests
import json
import bs4

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}

with open("channels.json",'r',encoding='utf-8') as f:
    channels = json.loads(f.read())
f.close()

def getOfiiiM3u8(mediaType,id):
    url = 'https://api.ofiii.com/cdi/v3/rpc'
    payload = {"jsonrpc":"2.0","id":123,"method":"LoadService.GetURLs","params":{"device_type":"pc"}}
    payload["params"]["media_type"]=mediaType
    payload["params"]["asset_id"]=id
    # print(payload)
    try:
        resp = requests.post(url,json=payload, headers=HEADERS)
    except Exception as e:
        print(e)

    j = json.loads(resp.text)
    # print(j)
    m3u8 = ''
    if j.get('result','') != '':
        m3u8 = j.get('result','').get('asset_urls','')[0]
    return m3u8


def main():
    out = '#EXTM3U url-tvg="http://epg.51zmt.top:8000/e.xml"\n'
    txt = '歐飛頻道,#genre#\n'
    for a in channels:
        title = a['title']
        id = a['id']
        content_type = a['content_type']
        image = a['image']
        vod = a['vod']
        seq = a['seq']

        if content_type != 'channel':
            id = id+"#"+vod+"-"+str(seq).zfill(6)+"M001"

        m3u8 = getOfiiiM3u8(content_type,id)

        out = out+'#EXTINF:-1 tvg-logo="'+ image + '" tvg-name="'+title+'" group-title="歐飛頻道",'+title+'\n'+m3u8 + '\n'
        txt += title + ','+ m3u8 + '\n'

        outFile = title+'.m3u8'
        f = open(outFile,'w',encoding='utf-8')
        f.write(f'#EXTM3U\n')
        f.write(f'#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2048000,RESOLUTION=1920x1080\n')
        f.write(f'{m3u8}\n')
        f.close()

    txt += '民視頻道,#genre#\n'
    ftvchannels = [['FTV', '01', '民视'],['FMTV', '02', '民视第一台'],['FTTV', '03', '民视台湾台'],['FTVNews', '04', '民视新闻台'],['FTVDrama', '05', '民視影劇台'],['FTVVariety', '06', '民视综艺台'],['FTVTravel', '07', '民视旅游台']]
    for ch in ftvchannels:
        v = ch[0]
        id = ch[1]
        title = ch[2]

        url = "https://app.4gtv.tv/Data/GetChannelURL_Mozai.ashx?Channelname="+v
        try:
            resp = requests.get(url, headers=HEADERS)
        except Exception as e:
            print(e)
        data = resp.text
        x = data.replace("channelname(", "").replace(")", "")
        j = json.loads(x)
        # link = j['VideoURL'].replace("master.m3u8", "stream2.m3u8")
        link = j['VideoURL']

        image = "https://www.ftv.com.tw/images/Ch_"+id+".png"
        

        out += '#EXTINF:-1 tvg-name="'+title+'" tvg-logo="'+image + '" group-title="民視頻道",'+title+'\n'+link + '\n'
        txt += title + ','+ link + '\n'

        outFile = title+'.m3u8'
        f = open(outFile,'w',encoding='utf-8')
        f.write(f'#EXTM3U\n')
        f.write(f'#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2048000,RESOLUTION=1920x1080\n')
        f.write(f'{link}\n')
        f.close()

    with open("tv.m3u",'w',encoding='utf-8') as f:
        f.write(out)
    f.close()

    with open("tv.txt",'w',encoding='utf-8') as f:
        f.write(txt)
    f.close()


if __name__ == "__main__":
    main()
