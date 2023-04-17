import openai
import re

# 设置OpenAI API密钥
openai.api_key = "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"

# 定义将中文翻译成英文的函数
def translate_text(text):
    if '-' in text:
        return
    result = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Translate the following Chinese text to English:\n{text}\n",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text.strip()

    return result

# 读取md文件
with open('README_en.md', mode='r', encoding='utf-8') as file:
    md_data = file.read()

# 利用正则表达式提取表格数据
table_data_pattern = r'\|(.*)\|\n(\|.*\|)+'
table_matches = re.finditer(table_data_pattern, md_data)
for match in table_matches:
    table_data = match.group(0)
    # 将表格数据转化为二维列表
    rows = table_data.strip().split('\n')
    table = [row.strip().split('|') for row in rows]
    # 遍历表格数据并翻译中文
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j].strip() != '':
                table[i][j] = translate_text(table[i][j].strip())

    # 将更新后的数据更新到md文件
    table_data_english = '\n'.join(['|'.join(row) + '|' for row in table])
    md_data = md_data.replace(match.group(0), table_data_english)

# 替换md文件中的中文文本为英文文本
chinese_pattern = r'[\u4e00-\u9fff]+'
chinese_matches = re.findall(chinese_pattern, md_data, re.UNICODE)
for match in chinese_matches:
    english_text = translate_text(match)
    md_data = md_data.replace(match, english_text)

# 将更新后的md文件写入输出文件中
with open('README_en.md', mode='w', encoding='utf-8') as file:
    file.write(md_data)
