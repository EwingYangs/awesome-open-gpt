import pandas as pd
import requests
from bs4 import BeautifulSoup

# 获取给定URL的Star数
def get_star_count(url):
    api_url = url.replace("github.com", "api.github.com/repos")
    response = requests.get(api_url)
    if response.ok:
        return response.json()[0]["stargazers_count"]
    else:
        return None

def do_auto_update_star():

    # 读取Markdown文件并解析为HTML
    with open("./README.md", "r") as f:
        html = "".join(f.readlines())
    soup = BeautifulSoup(html, "html.parser")

    # 提取所有表格
    tables = soup.find_all("table")

    # 处理每个表格
    for table in tables:
        # 将HTML表格解析为dataframe
        df = pd.read_html(str(table))[0]

        # 提取所有github地址
        github_urls = df[df.columns[-2]].str.extract("(https://github.com/[^)]+)")[0].tolist()

        # 获取每个GitHub项目的Star数量
        star_counts = [get_star_count(url) for url in github_urls]

        # 将Star数量添加为新列
        df["Stars"] = star_counts

        # 将结果写回HTML表格
        html_table = df.to_html(index=False)
        new_table = BeautifulSoup(html_table, "html.parser")
        table.replace_with(new_table)

    # 将HTML保存回Markdown文件
    with open("output.md", "w") as f:
        f.write(str(soup))


if __name__ == '__main__':
    do_auto_update_star()