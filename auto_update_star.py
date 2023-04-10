import pandas as pd
import requests
from bs4 import BeautifulSoup
import markdown
import re
import os
from dotenv import load_dotenv

# 获取给定URL的Star数
def get_star_count(url):
    proxy = {
        "http":"http://127.0.0.1:7890"
    }
    access_token = os.getenv("GITHUB_ACCESS_KEY")
    headers = {'Authorization': access_token}
    api_url = url.replace("github.com", "api.github.com/repos")
    response = requests.get(api_url, proxies=proxy, headers=headers)
    if response.ok:
        star_count = response.json()["stargazers_count"]
        if star_count >= 1000:
            star_count_str = f'{star_count / 1000:.1f}k'
        else:
            star_count_str = str(star_count)
        return star_count_str
    else:
        return None

def do_auto_update_star():

    # 读取Markdown文件并解析为HTML
    # with open("./README.md", "r") as f:
    #     html = "".join(f.readlines())

    # 读取md文件的内容
    with open("./README.md", 'r', encoding='utf-8') as f:
        content = f.read()

    html = markdown.markdown(content, extensions=['markdown.extensions.tables'])

    soup = BeautifulSoup(html, "html.parser")

    # 提取所有表格
    tables = soup.find_all("table")

    # 处理每个表格
    for table in tables:
        rows = table.find_all('tr')
        links = []
        # 指定要提取超链接的列的索引
        link_col_index = 1
        for row in rows[1:]:
            cells = row.find_all('td')
            link_cell = cells[link_col_index]
            match = re.search(r'<a href="(.*?)">', str(link_cell))
            if match:
                links.append(match.group(1))

        # 将HTML表格解析为dataframe
        df = pd.read_html(str(table), match='a')[0]

        # 获取每个GitHub项目的Star数量
        star_counts = [get_star_count(url) for url in links]

        # 将Star数量添加为新列
        df["点赞数"] = star_counts

        last_col_name = df.columns[-1]
        index_of_github = df.columns.get_loc('github地址')

        # 将最后一列从DataFrame中删除，然后将其插入到所需的位置
        last_col = df.pop(last_col_name)
        df.insert(index_of_github + 1, last_col_name, last_col)

        # 将结果写回HTML表格
        html_table = df.to_html(index=False)
        new_table = BeautifulSoup(html_table, "html.parser")
        table.replace_with(new_table)

    # 将HTML保存回Markdown文件
    with open("output.md", "w") as f:
        f.write(str(soup))


if __name__ == '__main__':
    # 加载.env文件
    load_dotenv()
    do_auto_update_star()