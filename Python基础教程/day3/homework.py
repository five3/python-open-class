import requests
"""
作业内容：
    实现一个图片下载器，读取url文件内容，顺序下载图片，支持通过len()、str()、iter()等函数。使用效果如下：
    e.g. 
        imagedownloader = ImageDownloader('url.txt')
        imagedownloader.run()
        print(len(imagedownloader))     #=> 打印下载成功的图片数量
        print(imagedownloader)          #=> 打印类名 和 url文件的路径信息。 如：<ImageDownloader /path/to/url/text>
        for img in imagedownloader:
            print(img)      # 打印图片保存地址

要求：
    基于如下已有代码进行功能实现，其中图片内容下载相关代码已经实现。需要自己保存并维护图片文件路径。其它方法和属性需要自行添加。
"""


class ImageDownloader(object):
    def __init__(self, url_file_name='url.txt'):
        self.url_file_name = url_file_name

    @staticmethod
    def download_image_by_url(url):
        try:
            rep = requests.head(url)
            if not rep.headers.get('content-type').startswith('image/'):
                return

            imgage_bytes = requests.get(url).content
            # TODO: Save image and record the image path into list
        except:
            print(f'Request Fail For URL {url}')
            return
