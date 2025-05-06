# 使用python爬虫，爬取笔趣阁小说（https://www.bqg128.com/)
"""
笔趣阁爬虫
"""
from requests_html import HTMLSession
import re
import time
import os


def get_chapter(chapter, name='novals', session=HTMLSession()):
    r = session.get(chapter)
    h1 = r.html.find('h1', first=True)
    title = h1.text
    chapter_content = r.html.find('#chaptercontent', first=True)
    pattern = r'请收藏本站：https://www.mac3.cc。笔趣阁手机版：https://m.mac3.cc|『点此报错』『加入书签』'
    clean_chapter = re.sub(pattern + r'\s*', "", chapter_content.text)
    # print(title)
    # print(clean_chapter)
    folder_path = 'novals'
    file_path = os.path.join(folder_path, name)
    os.makedirs(folder_path, exist_ok=True)
    with open(file_path + '.txt', 'a', encoding='utf-8') as f:
        f.write(title + '\n\n')
        f.write(clean_chapter)
    print(title + '已下载')

if __name__ == '__main__':
    url = 'https://www.mac3.cc/read/23235/'
    # name = input(f'请输入小说的名字：')
    time_start = time.time()
    session = HTMLSession()
    r = session.get(url)
    list_main = r.html.find('.listmain', first=True)
    name = r.html.find('h1', first=True).text
    chapters = list_main.absolute_links
    chapters = sorted(chapters, key=lambda x: int(x.split('/')[-1].split('.')[0]))
    print(f'共有：{len(chapters)}章\n\n')
    chapters_num = len(chapters)
    i = 1
    for chapter in chapters:
        print(f'第{i}章，剩余：{chapters_num - i}')
        try:
            get_chapter(chapter, name=name, session=session)
        except:
            c = input(f'第{i}章下载失败, 继续(1)还是停止(0):')
            if c == '1':
                continue
            elif c == '0':
                break
        i += 1
    session.close()
    time_end = time.time()
    print(f'总耗时：{time_end - time_start}s')