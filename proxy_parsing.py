import mitmproxy.http, os

class bljiex:
    def request(self, flow: mitmproxy.http.HTTPFlow):
        pass
    def response(self, flow: mitmproxy.http.HTTPFlow):
        if 'm3u8' in flow.request.url:
            url = flow.request.url
            # url = url.split('?')[0]
            with open('get_url.txt', 'w') as f:
                f.write(url)
            # down_cmd = f'ffmpeg -i {url} -c copy  output.mp4'
            # os.system(down_cmd)
addons = [
    bljiex()
]
# https://migu.vod.pptv.com/640ba7eb491fa4f5c1eaa44f7b07f0c4.m3u8?h5vod.ver=2.1.3&k=966fa1bc557474a27328238815549aa6-3ede-1618048154%26bppcataid%3D980&type=mhpptv
# ffmpeg -i 'https://play.cdn-ch2.webcg.top/qy/bf44e678c4187afaae2c1c74a1a2897b.m3u8?t=1618036350' -c copy  output.mp4