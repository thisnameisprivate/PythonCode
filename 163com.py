import os
import tkinter
import requests
from lxml import etree

flag = False

class MusicScript (object):
    def __init__(self):
        pass
    def download_songs(self):
        self.text = text
        self.entry = entry
        url = self.entry.get()
        url = url.replace('/#', '').replace('https', 'http')
        if url == '':
            self.text.insert(tkinter.END, 'Please Enter Your Need onLoad Url address!!!')
            return
        out_link = 'http://music.163.com/song/media/outer/ulr?id='
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36',
            'Referer': 'https://music.163.com/',
            'Host': 'music.163.com'
        }
        res = requests.get(url=url, headers=headers).text
        tree = etree.HTML(res)
        song_list = tree.xpath('//ul[@class="f-hide"]/li/a')
        artist_name_tree = tree.xpath('//h2[@id="artist-name"]/text()')
        artist_name = str(artist_name_tree[0]) if artist_name_tree else None
        song_list_name_tree = tree.xpath('//[contains[@class, "f-ff2"]]/text()')
        song_list_name = str(song_list_name_tree[0]) if song_list_name_tree else None
        folder = './' + artist_name if artist_name else './' + song_list_name
        if not os.path.exists(folder):
            os.mkdir(folder)
        for i,s in enumerate(song_list):
            href = str(s.xpath('./@href')[0])
            id = href.split('=')[-1]
            src = out_link + id
            title = str(s.xpath('./text()')[0])
            filename = title + '.mp3'
            filepath = folder + './' + filename
            data = requests.get(src).content
            info = 'Start Install %d Music:%s \n' % (i + 1, filename)
            if flag:
                self.text.insert(tkinter.END, info)
                self.text.see(tkinter.END)
                self.text.update()
                break
            self.text.insert(tkinter.END, info)
            self.text.see(tkinter.END)
            self.text.update()

            try:
                with open(filepath, 'wb') as f:
                    f.write(data)
            except Exception as e:
                print(e)
                self.text.insert(tkinter.END, e)
                self.text.see(tkinter.END)
                self.text.update()
        if not flag:
            self.text.insert(tkinter.END)
            self.text.see(tkinter.END)
            self.text.update()

class Application(object):
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title('网易云MusicInstall')
        self.center_window(self.window, 800, 500)
        self.fm1 = tkinter.Frame(self.window)
        self.fm2 = tkinter.Frame(self.window)
        self.fm3 = tkinter.Frame(self.window)
        self.fm4 = tkinter.Frame(self.window)
        self.fm1.pack()
        self.fm2.pack()
        self.fm3.pack()
        self.fm4.pack()


        self.label = tkinter.Label(self.fm1, text='输入你要下载的歌单的url,点击下载或者回车!', font=('微软雅黑', 15), width = 35)
        self.label.pack(fill=tkinter.X)
        self.entry = tkinter.Entry(self.fm2, width=46, bg='pink', font=('微软雅黑',20))
        self.entry.grid(row=0, column=0, rowspan=1, columspan=10, padx=0)
        self.entry.bind("<Key-Return>", self.press_enter)
        self.btn_download = tkinter.Button(self.fm2, text='Onload', command=self.crawl, bg='red', font=('微软雅黑',12))
        self.btn_download.grid(row=0, column=30, rowspan=1, columnspan=1, padx=5, pady=3)
        self.text = tkinter.Text(self.fm3, width=110, height=18, font=('微软雅黑', 10))
        self.text.pack(side=tkinter.LEFT, fill=tkinter.Y)
        self.scroll = tkinter.Scrollbar(self.fm3)
        self.scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.scroll.config(command=self.text.yview())
        self.text.config(yscrollcomman=self.scroll.set)
        btn_stop = tkinter.Button(self.fm4, text='Stop', command=self.stop, bg='gray', font=('微软雅黑', 16))
        btn_quit = tkinter.Button(self.fm4, text='Quit', command=self.window.quit, bg='gray', font=('微软雅黑', 16))
        btn_stop.pack(side='left', padx=100, pady=10)
        btn_quit.pack(side='right', padx=100, pady=10)
    def stop(self):
        global flag
        flag = True
        return flag
    def crawl(self):
        text = self.text
        entry = self.entry
        MusicScript.download_songs(self, text, entry)
    def press_enter(self, even):
        return self.crawl()
    def center_window(self, root, width, height):
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry
    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    app = Application()
    app.run()
    
    
    
    
    
    
    
    
    
