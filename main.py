import requests
import json
import bs4

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}

channels = [
    {'title': '台視', 'id': '4gtv-4gtv066', 'image': 'https://cdnstatic.svc.litv.tv/pics/logo_litv_4gtv-4gtv066_tv.png'}, 
    {'title': '中視', 'id': '4gtv-4gtv040', 'image': 'https://cdnstatic.svc.litv.tv/pics/logo_litv_4gtv-4gtv040_tv.png'}, 
    {'title': '華視', 'id': '4gtv-4gtv041', 'image': 'https://cdnstatic.svc.litv.tv/pics/logo_litv_4gtv-4gtv041_tv.png'}, 
    {'title': '好消息2台', 'id': 'litv-ftv17', 'image': 'https://cdnstatic.svc.litv.tv/pics/logo_litv_litv-ftv17_tv.png'}, 
    {'title': '好消息', 'id': 'litv-ftv16', 'image': 'https://cdnstatic.svc.litv.tv/pics/logo_litv_litv-ftv16_tv.png'}, 
    {'title': 'ELTV生活英語台', 'id': 'litv-longturn20', 'image': 'https://cdnstatic.svc.litv.tv/pics/logo_litv_litv-longturn20_tv.png'}, 
    {'title': '龍華卡通台', 'id': 'litv-longturn01', 'image': 'https://cdnstatic.svc.litv.tv/pics/logo_4gtv_litv-longturn01_tv.png'}, 
    {'title': '哆啦Ａ夢台', 'id': 'ofiii22', 'image': 'https://cdnstatic.svc.litv.tv/pics/vod_channel/logo_litv-vchannel22_tv_20190902.png'}, 
    {'title': '亞洲旅遊台', 'id': 'litv-longturn17', 'image': 'https://cdnstatic.svc.litv.tv/pics/logo_4gtv_litv-longturn17_tv.png'}, 
    {'title': 'Smart知識台', 'id': 'litv-longturn19', 'image': 'https://cdnstatic.svc.litv.tv/pics/logo_litv_litv-longturn19_tv.png'}, 
    {'title': '年代MUCH綜藝台', 'id': 'ofiii38', 'image': 'https://cdnstatic.svc.litv.tv/pics/vod_channel/logo_litv-vchannel35_tv_20201019.png'}, 
    {'title': '龍華戲劇台', 'id': 'litv-longturn18', 'image': 'https://cdnstatic.svc.litv.tv/pics/logo_litv_litv-longturn18_tv.png'}, 
    {'title': '台灣戲劇台', 'id': 'litv-longturn22', 'image': 'https://cdnstatic.svc.litv.tv/pics/logo_litv_litv-longturn22_tv.png'}, 
    {'title': 'Focus風采戲劇台', 'id': 'ofiii42', 'image': 'https://cdnstatic.svc.litv.tv/pics/vod_channel/logo_litv-playout951_tv_20180522.png'}, 
    {'title': '東森購物1台', 'id': '4gtv-4gtv102', 'image': 'https://cdnstatic.svc.litv.tv/pics/logo_litv_4gtv-4gtv102_tv.png'}, 
    {'title': '龍華偶像台', 'id': 'litv-longturn12', 'image': 'https://cdnstatic.svc.litv.tv/pics/logo_litv_litv-longturn12_tv.png'}, 
    {'title': '龍華日韓台', 'id': 'litv-longturn11', 'image': 'https://cdnstatic.svc.litv.tv/pics/logo_litv_litv-longturn11_tv.png'}, 
    {'title': 'Yes娛樂', 'id': 'ofiii48', 'image': 'https://cdnstatic.svc.litv.tv/pics/vod_channel/logo_litv-vchannel050_tv.png'}, 
    {'title': '東森購物2台', 'id': '4gtv-4gtv103', 'image': 'https://cdnstatic.svc.litv.tv/pics/logo_litv_4gtv-4gtv103_tv.png'}, 
    {'title': '掏掏新聞', 'id': 'ofiii50', 'image': 'https://cdnstatic.svc.litv.tv/pics/vod_channel/logo_litv-playout50_tv_20211124.png'}, 
    {'title': '華視新聞', 'id': '4gtv-4gtv052', 'image': 'https://cdnstatic.svc.litv.tv/pics/logo_litv_4gtv-4gtv052_tv.png'}, 
    {'title': '寰宇財經台', 'id': 'litv-longturn23', 'image': 'https://cdnstatic.svc.litv.tv/pics/logo_litv_litv-longturn23_tv.png'}, 
    {'title': '台視新聞', 'id': '4gtv-4gtv051', 'image': 'https://cdnstatic.svc.litv.tv/pics/logo_litv_4gtv-4gtv051_tv.png'}, 
    {'title': '中視新聞', 'id': '4gtv-4gtv074', 'image': 'https://cdnstatic.svc.litv.tv/pics/logo_litv_4gtv-4gtv074_tv.png'}, 
    {'title': '中天新聞台', 'id': '4gtv-4gtv009', 'image': 'https://cdnstatic.svc.litv.tv/pics/logo_litv_4gtv-4gtv009_tv.png'}, 
    {'title': '寰宇新聞台灣台', 'id': 'litv-longturn15', 'image': 'https://cdnstatic.svc.litv.tv/pics/logo_litv_litv-longturn15_tv.png'}, 
    {'title': '寰宇新聞台', 'id': 'litv-longturn14', 'image': 'https://cdnstatic.svc.litv.tv/pics/logo_litv_litv-longturn14_tv.png'}, 
    {'title': '第1財經', 'id': 'ofiii64', 'image': 'https://cdnstatic.svc.litv.tv/pics/vod_channel/logo_ofiii64_tv_20221110.png'}, 
    {'title': '第1商業台', 'id': '4gtv-4gtv104', 'image': 'https://cdnstatic.svc.litv.tv/pics/logo_litv_4gtv-4gtv104_tv.png'},
    {'title': '國會頻道1台', 'id': '4gtv-4gtv084', 'image': 'https://cdnstatic.svc.litv.tv/pics/logo_litv_4gtv-4gtv084_tv.png'}, 
    {'title': '國會頻道2台', 'id': '4gtv-4gtv085', 'image': 'https://cdnstatic.svc.litv.tv/pics/logo_litv_4gtv-4gtv085_tv.png'}, 
    {'title': '龍華經典台', 'id': 'litv-longturn21', 'image': 'https://cdnstatic.svc.litv.tv/pics/logo_litv_litv-longturn21_tv.png'}, 
    {'title': '龍華電影台', 'id': 'litv-longturn03', 'image': 'https://cdnstatic.svc.litv.tv/pics/logo_litv_litv-longturn03_tv.png'}, 
    {'title': '歐飛電影台', 'id': 'ofiii74', 'image': 'https://cdnstatic.svc.litv.tv/pics/vod_channel/logo_ofiii74_tv_20230116.png'}, 
    {'title': 'Focus探索新知台', 'id': 'ofiii82', 'image': 'https://cdnstatic.svc.litv.tv/pics/vod_channel/logo_ofiii82_tv_20221213.png'}, 
    {'title': '東森購物快閃台', 'id': 'ofiii87', 'image': 'https://cdnstatic.svc.litv.tv/pics/vod_channel/logo_ofiii87_tv_20221110.png'}, 
    {'title': 'LiTV 好康優惠', 'id': 'ofiii98', 'image': 'https://cdnstatic.svc.litv.tv/pics/vod_channel/logo_ofiii98_tv_20230412.png'}, 
    {'title': '銀髮聚樂部', 'id': 'ofiii99', 'image': 'https://cdnstatic.svc.litv.tv/pics/vod_channel/logo_ofiii99_tv_20221110.png'}, 
    {'title': '琅琊榜', 'id': 'ofiii101', 'image': 'https://cdnstatic.svc.litv.tv/pics/vod_channel/logo_ofiii101_tv_20230329.png'}, 
    {'title': '山河月明', 'id': 'ofiii102', 'image': 'https://cdnstatic.svc.litv.tv/pics/vod_channel/logo_ofiii102_tv_20230329.png'}, 
    {'title': '三十而已', 'id': 'ofiii115', 'image': 'https://cdnstatic.svc.litv.tv/pics/vod_channel/logo_ofiii115_tv_20230329.png'}, 
    {'title': '去有風的地方', 'id': 'ofiii116', 'image': 'https://cdnstatic.svc.litv.tv/pics/vod_channel/logo_ofiii116_tv_20230329.png'}, 
    {'title': '綜藝玩很大', 'id': 'ofiii130', 'image': 'https://cdnstatic.svc.litv.tv/pics/vod_channel/logo_ofiii130_tv_20230329.png'}, 
    {'title': '全民星攻略', 'id': 'ofiii131', 'image': 'https://cdnstatic.svc.litv.tv/pics/vod_channel/logo_ofiii131_tv_20230329.png'}, 
    {'title': '台灣1001個故事', 'id': 'ofiii132', 'image': 'https://cdnstatic.svc.litv.tv/pics/vod_channel/logo_ofiii132_tv_20230329.png'}, 
    {'title': '台灣啟示錄', 'id': 'ofiii133', 'image': 'https://cdnstatic.svc.litv.tv/pics/vod_channel/logo_ofiii133_tv_20230329.png'}, 
    {'title': '歡迎來到第2人生', 'id': 'ofiii146', 'image': 'https://cdnstatic.svc.litv.tv/pics/vod_channel/logo_ofiii146_tv_20221111.png'}, 
    {'title': '大發不動產', 'id': 'ofiii147', 'image': 'https://cdnstatic.svc.litv.tv/pics/vod_channel/logo_ofiii147_tv_20221111.png'}, 
    {'title': '檢法男女2', 'id': 'ofiii148', 'image': 'https://cdnstatic.svc.litv.tv/pics/vod_channel/logo_ofiii151_tv_20221115.png'}, 
    {'title': '台灣X檔案', 'id': 'ofiii151', 'image': 'https://cdnstatic.svc.litv.tv/pics/vod_channel/logo_ofiii165_tv_20221111.png'}, 
    {'title': '大叔的愛', 'id': 'ofiii161', 'image': 'https://cdnstatic.svc.litv.tv/pics/vod_channel/logo_ofiii175_tv_20221111.png'}, 
    {'title': 'SiCAR愛車酷', 'id': 'ofiii181', 'image': 'https://cdnstatic.svc.litv.tv/pics/vod_channel/logo_litv-vchannel181_tv_20221227.png'},
    {'title': 'Auto-Online 汽車線上情報誌', 'id': 'ofiii182', 'image': 'https://cdnstatic.svc.litv.tv/pics/vod_channel/logo_litv-vchannel182_tv_20221227.png'}, 
    {'title': '統哥 嗜駕Pit63', 'id': 'ofiii183', 'image': 'https://cdnstatic.svc.litv.tv/pics/vod_channel/logo_litv-vchannel183_tv_20221226.png'}, 
    {'title': 'CARLINK鏈車網', 'id': 'ofiii184', 'image': 'https://cdnstatic.svc.litv.tv/pics/vod_channel/logo_litv-vchannel184_tv_20230214.png'}, 
    {'title': '蒙福人生', 'id': 'ofiii191', 'image': 'https://cdnstatic.svc.litv.tv/pics/vod_channel/logo_ofiii185_tv_20221110.png'}, 
    {'title': '生命的贏家', 'id': 'ofiii192', 'image': 'https://cdnstatic.svc.litv.tv/pics/vod_channel/logo_ofiii192_tv_20230329.png'}
]

def get4gtvM3u8(mediaType,id):
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

def getOfiiiM3u8(id):
    url = "https://www.ofiii.com/_next/data/VAtIX7CyM9AiV-IIonkJK/channel/watch/%s.json?contentId=%s" % (id,id)
    try:
        resp = requests.get(url, headers=HEADERS)
    except Exception as e:
        print(e)    
    j = json.loads(resp.text)
    c = j["pageProps"]["channel"]

    title = c["title"]
    content_id = c["content_id"]
    mediaType = c["content_type"]
    id = content_id+"#"+c["vod_channel_schedule"]["focus_program"]["asset_id"]
    # print(mediaType,id)
    m3u8 = get4gtvM3u8(mediaType,id)
    return m3u8

def main():
    out = '#EXTM3U url-tvg="http://epg.51zmt.top:8000/e.xml"\n'
    txt = '歐飛頻道,#genre#\n'
    for a in channels:
        title = a['title']
        id = a['id']
        image = a['image']
        if 'ofiii' not in id:
            mediaType = "channel"
            m3u8 = get4gtvM3u8(mediaType,id)
        else:
            mediaType = "vod-channel"
            m3u8 = getOfiiiM3u8(id)
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
        link = j['VideoURL'].replace("master.m3u8", "stream2.m3u8")
        image = "https://www.ftv.com.tw/images/Ch_"+id+".png"
        
        link = 'https://pkj99.github.io/ofiii/'+title+'.m3u8'
        
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


