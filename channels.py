import requests
import json

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}

with open("channels.json",'r',encoding='utf-8') as f:
    channels = json.loads(f.read())
f.close()

def genChannels():
    token = 'oK2bzPGMGTx-jovo-bgGA'
    vodChannels = []
    for a in channels:
        title = a['title']
        id = a['id']
        image = a['image']
        print(title,id)

        url = "https://www.ofiii.com/_next/data/%s/channel/watch/%s.json?contentId=%s" % (token,id,id)
        try:
            resp = requests.get(url, headers=HEADERS)
        except Exception as e:
            print(e)
            continue

        j = json.loads(resp.text)
        c = j["pageProps"]["channel"]

        # title = c["title"]
        # content_id = c["content_id"]
        content_type = c["content_type"]

        if content_type == 'channel':
            vod = ''
            seq = 0
        else:
            vodString = c["vod_channel_schedule"]["focus_program"]["asset_id"]
            vod = vodString.split('-')[0]
            seq = int(vodString.split('-')[1].split('M')[0])
            # idstr = content_id+"#"+vodString  # sample: ofiii146#vod40413-000023M001

        item = {}
        item['title'] = title
        item['id'] = id
        item['content_type'] = content_type
        item['image'] = image
        item['vod'] = vod
        item['seq'] = seq
        vodChannels.append(item)

    # print(vodChannels)
    with open("channels.json",'w',encoding='utf-8') as f:
        f.write(json.dumps(vodChannels, ensure_ascii=False))
    f.close()

    return


if __name__ == "__main__":
    genChannels()
