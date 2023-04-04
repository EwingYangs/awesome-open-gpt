<h2 align="center">awesome-open-gpt/gpt相关开源项目合集</h2>
        
<div align="center">

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()
</div>


![ChatGPT](https://cdn-hoodp.nitrocdn.com/HhPZwyEPNMbxJwQocjPNMHNUjcddXQui/assets/images/optimized/rev-c6b2313/app/uploads/2023/02/chatgpt.jpeg)

- **awesome-open-gpt**是关于GPT开源精选项目的合集 🚀，其中包括了一些GPT镜像、GPT增强、GPT插件、GPT工具、GPT平替的聊天机器人、开源大语言模型等等。
- awesome-list的目的是为了让所有GPT关注者更好地关注GPT模型的应用，同时也为想要学习和使用GPT模型的人提供了一些有用的资源。
- awesome-open-gpt会持续更新，希望有更多优秀的GPT相关项目涌现！！！


<!-- TOC -->
  * [精选开源项目合集](#精选开源项目合集)
    * [GPT镜像平替](#gpt镜像平替)
    * [GTP编程语言客户端](#gtp编程语言客户端)
    * [第三方机器人接入](#第三方机器人接入)
    * [GPT工具](#gpt工具)
      * [GPT工具-文档](#gpt工具-文档)
      * [GPT工具-编程](#gpt工具-编程)
      * [GPT工具-通用](#gpt工具-通用)
      * [GPT工具-音视频](#gpt工具-音视频)
      * [GPT工具-其他](#gpt工具-其他)
    * [GPT插件](#gpt插件)
      * [GPT插件-官方](#gpt插件-官方)
      * [GPT插件-浏览器](#gpt插件-浏览器)
      * [GPT插件-第三方应用](#gpt插件-第三方应用)
    * [GPT开源平替机器人](#gpt开源平替机器人)
    * [专业领域机器人](#专业领域机器人)
    * [Prompt对话指令](#prompt对话指令)
    * [其他（平台、逆向工程）](#其他平台逆向工程)
  * [相关资料](#相关资料)
  * [贡献](#贡献)
<!-- TOC -->

## 精选开源项目合集

### GPT镜像平替

| 名称                | github地址                                                                    | 简介                                                      | 功能                                                                                                                                                                                                      |
|-------------------|-----------------------------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ChatGPT桌面版-01     | [lencx-ChatGPT](https://github.com/lencx/ChatGPT)                           | ChatGPT桌面版(Windows、macOS和Linux)                         | 1.导出聊天记录(PNG, PDF和Markdown) <br/>2.支持斜杠调出常用Prompts(awesome-chatgpt-prompts )<br/>3.网页登录模式                                                                                                               |
| ChatGPT桌面版-02     | [chat-ai-desktop](https://github.com/sonnylazuardi/chat-ai-desktop)         | 非官方的ChatGPT桌面应用程序(Windows、macOS和Linux)                  | 1.支持API模式，免登录<br/>2.支持在Windows和Mac的菜单栏显示                                                                                                                                                                |
| ChatGPT桌面版-03     | [ChatGPT-Desktop](https://github.com/Synaptrix/ChatGPT-Desktop)             | ChatGPT 跨平台客户端(Windows、macOS和Linux)                     | 1.支持设置对话角色<br/>2.支持文生图                                                                                                                                                                                  |
| ChatGPT桌面版-04     | [chatbox](https://github.com/Bin-Huang/chatbox)                             | 开源的ChatGPT桌面应用，prompt 开发神器                              | 1.支持 Windows、Mac 和 Linux<br/> 2.更自由、更强大的 Prompt 能力<br/>  3.支持 GPT-4 和其他模型<br/>  4.更多功能：Markdown、消息引用、字数与token估算、夜间模式……                                                                                  |
| NewBing桌面版        | [BingGPT](https://github.com/dice2o/BingGPT)                             | 新必应人工智能聊天桌面应用程序（Windows、macOS 和 Linux）                              | 1.无需安装 Microsoft Edge 或浏览器插件即可与新 Bing 聊天<br/>2.将完整对话导出为 Markdown、PNG 或 PDF<br/>3.自定义外观（主题和字体大小）                                                                                                                       |
| ChatGPT-mac菜单版    | [chatgpt-mac](https://github.com/vincelwt/chatgpt-mac)                      | 使ChatGPT生活在你的Mac菜单栏                                     | 1.在Mac菜单栏显示显示ChatGPT<br/>2.使用Cmd+Shift+G在任何地方唤起ChatGPT                                                                                                                                                  |
| ChatGPT-web加强版-01 | [ChatGPT-Next-Web](https://github.com/Yidadaa/ChatGPT-Next-Web)             | 一键拥有你自己的 ChatGPT 网页服务                                   | 1.在 1 分钟内使用 Vercel 免费一键部署，并且支持容器部署<br/>2.海量的内置 prompt 列表，来自中文和英文<br/>3.一键导出聊天记录，完整的 Markdown 支持                                                                                                         |
| ChatGPT-web加强版-02 | [EX-chatGPT](https://github.com/circlestarzero/EX-chatGPT)                  | Ex-ChatGPT 使得 ChatGPT 能够调用外部 API，例如 WolframAlpha、Google 和 WikiMedia，以提供更准确和及时的答案 | 1.语音对话功能，使用微软 Azure API，优化响应速度 ( 1-2 秒左右 ) ，包含语音识别和文字转语音，支持多种音色和语言，自定义声音。<br/>2.docker 和 proxy 支持。<br/>3.对 Google 搜索结果进行数据清洗, 减少token占用。<br/>4.允许 ChatGPT 调用外部 API 接口 ( Google,WolframAlpha,WikiMedia ) |
| ChatGPT-web加强版-03 | [chatbot-ui](https://github.com/mckaywrigley/chatbot-ui)                    | 搭建属于自己的 ChatGPT 网站: ChatBot-UI                          | 1.支持Prompt模版<br/>2.支持搜索聊天内容<br/>3.支持GPT-4<br/>4.支持代码高亮显示<br/>5.支持Markdown输出                                                                                                                             |
| ChatGPT-web加强版-04 | [BetterChatGPT](https://github.com/ztjhz/BetterChatGPT)                     | 一个惊人的开源web应用程序，具有更好的UI，用于探索OpenAI的ChatGPT API                         | 1.支持自定义提示词资料库<br/>2.支持使用文件夹整理聊天<br/>3.支持自定义用户/助理/系统身份<br/>4.支持将聊天保存为 Markdown/图片/JSON                                                                                                                   |
| ChatGPT-web加强版-05 | [chatgpt-web](https://github.com/Chanzhaoyu/chatgpt-web)                    | 用 Express 和 Vue3 搭建的 ChatGPT 演示网页                       | 1.支持下载对话内容<br/>2.支持Prompt模版                                                                                                                                                                             |
| ChatGPT-web加强版-06 | [ChuanhuChatGPT](https://github.com/GaiZhenbiao/ChuanhuChatGPT)             | 轻快好用的ChatGPT Web图形界面                                    | 1.实时回复<br/>2.无限对话<br/>3.保存对话记录<br/>4.预设Prompt集<br/>5.联网搜索<br/>6.根据文件回答                                                                                                                                  |
| ChatGPT-web加强版-07 | [yakGPT](https://github.com/yakGPT/yakGPT)                                  | 一个简单的，本地运行的ChatGPT UI，使您的文本生成更快，聊天更吸引人!                 | 1.支持api调用<br/>2.支持语音输入                                                                                                                                                                                  |
| ChatGPT-web加强版-08 | [chatgpt-php-web](https://github.com/dirk1983/chatgpt)                      | PHP版调用OpenAI最新接口和模型gpt-3.5-turbo进行问答的Web                             | 1.增加了一些预设话术<br/>2.对手机浏览器进行了适配优化                                                                                                                                                                         |
| ChatGPT-web加强版-09 | [multimedia-gpt](https://github.com/fengyuli-dev/multimedia-gpt) | 为您的ChatGPT提供图像、视频和音频输入                                                | 1.将OpenAI GPT与视觉和音频连接起来。您现在可以使用OpenAI API密钥发送图像、音频记录和pdf文档，并获得文本和图像格式的响应。目前正在增加对视频的支持。 |
| ChatGPT-web加强版-10 | [visual-chatgpt](https://github.com/microsoft/visual-chatgpt) | 微软开源的一款工具，可以为 ChatGPT 添加图片能力                                             | 1.支持文生图<br/>2.支持文改图                                                                                            |
| ChatGPT-web加强版-11 | [chatgpt_academic](https://github.com/binary-husky/chatgpt_academic) | ChatGPT 学术优化                                                             | 1.支持一键润色、一键查找论文语法错误<br/>2.一键中英互译<br/> 3.可以正确显示代码、解释代码<br/> 4.一键可以剖析其他Python/C++项目 <br/> 5.可以输出支持GPT的markdown表格 |
| ChatGPT-文心一言开源版   | [visual-openllm](https://github.com/visual-openllm/visual-openllm)          | 文心一言的开源版，基于 ChatGLM + Visual ChatGPT + Stable Diffusion | 1.画图+聊天                                                                                                                                                                                                 |
| ChatGPT-命令行版+语音   | [chatgpt-conversation](https://github.com/platelminto/chatgpt-conversation) | 在命令行用你的声音与ChatGPT对话，并让它回应                               | 1.在cli命令行和ChatGPT语音交谈                                                                                                                                                                                   |
| ChatGPT-命令行版-01   | [shell_gpt](https://github.com/TheR1D/shell_gpt)                            | 在Shell中使用ChatGPT                                        | 1.支持api调用<br/>2.支持上下文                                                                                                                                                                                   |
| ChatGPT-命令行版-02   | [aichat](https://github.com/sigoden/aichat)                            | 终端使用ChatGPT/GPT-3.5/GPT-4                                        | 1.支持角色预设<br/>2.语法突出显示markdown和其他200种语言                                                                                                                                                                  |


### GTP编程语言客户端

| 名称                      | github地址                                                                      | 简介                                                                    | 功能                                            |
|-------------------------|-------------------------------------------------------------------------|-----------------------------------------------------------------------|-----------------------------------------------|
| Python-ChatGPT客户端       | [PyChatGPT](https://github.com/rawandahmad698/PyChatGPT)                | 非官方ChatGPT API的Python客户端。                                             | 1.具有自动令牌再生，会话跟踪，代理支持等                         |
| Python-Shell-ChatGPT客户端 | [chatgpt-wrapper](https://github.com/mmabrouk/chatgpt-wrapper) | 在python或者命令行中使用ChatGPT                                                | 1.支持ChatGPT4                                  |
| Java-ChatGPT客户端-01      | [chatgpt-java](https://github.com/PlexPt/chatgpt-java)                  | ChatGPT Java SDK。支持 GPT3.5、 GPT4 API。开箱即用。                            | 1.支持上下文、阻塞式对话、代理等                             |
| Java-ChatGPT客户端-02      | [chatgpt-java](https://github.com/Grt1228/chatgpt-java)                 | ChatGPT的Java客户端，ChatGPT Java SDK，流式输出。                            | 1.支持OpenAI官方所有接口<br/>2.支持流式输出                 |
| Java-OpenAi客户端          | [openai-java](https://github.com/TheoKanning/openai-java)      | OpenAI的java客户端。                                                       | 1.支持GPT-4                                     |
| Node-ChatGPT客户端         | [chatgpt-node](https://github.com/transitive-bullshit/chatgpt-api)      | 官方ChatGPT API的Node.js客户端。                                             |                                               |
| Node-ChatGPT-Bing客户端    | [node-chatgpt-api](https://github.com/waylaidwanderer/node-chatgpt-api) | ChatGPT和Bing AI的node客户端                                               | 1.支持BingAIClient<br/>2.支持ChatGPTBrowserClient |
| Go-OpenAi客户端            | [go-openai](https://github.com/sashabaranov/go-openai)         | OpenAI的go客户端。                                                         | 1.支持GPT-4                                     |
| PHP-OpenAi客户端              | [openai-php](https://github.com/orhanerday/open-ai)            | OpenAI的PHP SDK                                                        |                                               |
| Android-ChatGPT客户端         | [chatgpt-android](https://github.com/skydoves/chatgpt-android) | 安卓的ChatGPT-SDK                                                        |                                               |
| .Net-ChatGPT客户端            | [openai-dotnet](https://github.com/betalgo/openai) | OpenAI ChatGPT, Whisper, GPT-3, GPT-4, Azure OpenAI和DALL-E的dotnet SDK |                                               |


### 第三方机器人接入

| 名称                  | github地址                                                                  | 简介                                                                         | 功能                                                                                                                                                                                                                                                      |
|---------------------|---------------------------------------------------------------------------|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 微信ChatGPT机器人-01     | [wechat-chatgpt](https://github.com/fuergaosi233/wechat-chatgpt)          | 在微信上迅速接入 ChatGPT                                                           | 1.基于 wechaty 和 Official API 在微信中使用 ChatGPT<br/>2.支持多轮对话<br/>3.支持命令设置<br/>4.支持 Dall·E<br/>5.支持 whisper<br/>6.支持设置 prompt                                                                                                                                 |
| 微信ChatGPT机器人-02     | [ChatGPT-wechat-bot](https://github.com/AutumnWhj/ChatGPT-wechat-bot)         | 微信ChatGPT机器人                                                               | 1.支持上下文语境的对话。<br/>2.支持重置上下文语境，通过关键词(reset)重置对话上下文语境。<br/>3.支持在群聊@你的机器人 🤖，@机器人即可收到回复。<br/>4.支持通过关键词唤醒你的机器人，如当在群组中发送“@机器人 hello xxxx”时才会收到回复。                                                                                                            |
| 微信ChatGPT机器人-03     | [chatgpt-on-wechat](https://github.com/zhayujie/chatgpt-on-wechat)            | 使用ChatGPT搭建微信聊天机器人，基于GPT3.5 API和itchat实现                                   | 1.支持规则定制化<br/>2.多账号<br/>3.图片生成<br/>4.上下文记忆<br/>5.语音识别<br/>6.插件化                                                                                                                                                                                         |
| QQ和电报ChatGPT机器人     | [OpenaiBot](https://github.com/LlmKira/Openaibot)                             | OpenaiBot是一款优秀的基于 GPT 系列模型(主要为 Openai ) 接口的ChatGPT聊天机器人。                   | 1.支持跨多平台使用、有通用接口，目前能对接到QQ和Telegram聊天平台使用、进行私聊和群聊、主动搜索回复、图像Blip理解支持、语音识别、贴纸支持、聊天黑白名单限制等多种功能                                                                                                                                                              |
| Discord-ChatGPT机器人  | [chatGPT-discord-bot](https://github.com/Zero6992/chatGPT-discord-bot)        | 将ChatGPT集成到您自己的discord机器人中                                                 | 1.切换GPT接口模式，支持4.0<br/> 2.支持Dalle2生图                                                                                                                                                                                                                     |
| 电报ChatGPT机器人-01     | [ChatGPT-Telegram-Workers](https://github.com/TBXark/ChatGPT-Telegram-Workers) | 将ChatGPT集成到您自己的Telegram机器人中                                                | 1.使用Cloudflare Workers，单文件，直接复制粘贴一把梭，无需任何依赖，无需配置本地开发环境，不用域名，免服务器                                                                                                                                                                                        |
| 电报ChatGPT机器人-02     | [chatgpt-telegram-bot](https://github.com/n3d1117/chatgpt-telegram-bot) | Telegram机器人与OpenAI的官方ChatGPT api集成                                         | 1.支持markdown输出<br/>2.Docker和Proxy支持<br/>3.支持DALL·E<br/>3.支持使用Whisper转录音频和视频消息                                                                                                                                                                           |
| QQ-ChatGPT机器人-01    | [chatgpt-mirai-qq-bot](https://github.com/lss233/chatgpt-mirai-qq-bot) | 一款使用 OpenAI 的 ChatGPT 进行聊天的 QQ 机器人！                                        | 1.文字转图片发送<br/>2.群聊回复引用<br/>3.关键词触发回复<br/>4.正向代理<br/>5.多账号支持<br/>6.支持 Mirai、 go-cqhttp、 Telegram Bot<br/>7.支持 ChatGPT Plus<br/>8.支持 ChatGPT API<br/>9.支持 Bing 聊天<br/>10.支持 Google bard<br/>11.支持 poe.com 网页版<br/>12.支持 文心一言 网页版<br/>13.支持 ChatGLM-6B 本地版 |
| QQ-ChatGPT机器人-02    | [QChatGPT](https://github.com/RockChinQ/QChatGPT)                     | 高稳定性、低耦合、支持插件、适配多种模型的 ChatGPT NewBing QQ 机器人！                              | 1.已支持 GPT-4、New Bing<br/>2.支持对话、绘图等模型，可玩性更高<br/>3.私聊、群聊黑名单机制                                                                                                                                                                                            |
| WhatsApp-ChatGPT机器人 | [whatsapp-gpt](https://github.com/danielgross/whatsapp-gpt)           | 在whatsapp上迅速接入 ChatGPT                                                     | 1.聊天机器人                                                                                                                                                                                                                                                 |
| 飞书ChatGPT机器人-01     | [feishu-chatgpt](https://github.com/Leizhenpeng/feishu-chatgpt)       | 飞书 ×（GPT-3.5 + DALL·E + Whisper）= 飞一般的工作体验                                 | 1.🚀 语音对话、角色扮演、多话题讨论、图片创作、表格分析、文档导出 🚀                                                                                                                                                                                                                  |
| 飞书ChatGPT机器人-02     | [ChatGPT-Feishu](https://github.com/bestony/ChatGPT-Feishu)       | 给飞书准备的 ChatGPT 机器人                                                         | 1.简单版本                                                                                                                                                                                                                                                  |
| 钉钉ChatGPT机器人        | [chatgpt-dingtalk](https://github.com/eryajf/chatgpt-dingtalk)        | 🔔 钉钉 & 🤖 GPT-3.5 让你的工作效率直接起飞 🚀 私聊群聊方式、单聊串聊模式、角色扮演、图片创作 🚀               | 1.与机器人私聊<br/>2.帮助列表<br/>3.切换模式<br/>4.查询余额<br/>5.日常问题<br/>6.通过内置prompt聊天支<br/>7.生成图片<br/>8.gpt-4                                                                                                                                                         |
| LINE-ChatGPT机器人-01  | [gpt-ai-assistant](https://github.com/memochou1993/gpt-ai-assistant)  | 在LINE上接入ChatGPT聊天机器人                                                       | 1.支持角色塑造<br/>2.支持定制Prompt模版<br/>3.支持文生图                                                                                                                                                                                                                 |
| LINE-ChatGPT机器人-02  | [ChatGPT-Line-Bot](https://github.com/TheExplainthis/ChatGPT-Line-Bot)  | 这是一个允许您将ChatGPT集成到Line的开源库                                                 | 1.支持文生图<br/>2.总结 Youtube 影片內容、新文文章                                                                                                                                                                                                                      |
| Slack-ChatGPT机器人    | [myGPTReader](https://github.com/madawei2699/myGPTReader)             | myGPTReader 是一个 Slack 机器人。                                                 | 1.可以阅读任何网页、电子书、视频（YouTube）或文件，并通过 chatGPT 进行总结。它还可以通过语音与你交谈                                                                                                                                                                                             |
| Teams-ChatGPT机器人    | [openai-teams-bot](https://github.com/formulahendry/openai-teams-bot) | 一个OpenAI Teams Bot应用程序，让你在微软Teams中使用OpenAI API聊天，类似于ChatGPT Teams Bot应用程序。 |                                                                                                                                                                                                                                                         |

### GPT工具

#### GPT工具-文档

| 名称         | github地址      | 简介                         | 功能                                                                                                           |
|------------| ----------- |----------------------------|--------------------------------------------------------------------------------------------------------------|
| 论文总结       | [ChatPaper](https://github.com/kaixindelele/ChatPaper)                               | 利用chatgpt进行论文总结+润色+审稿+审稿回复 | 1.论文总结+润色+审稿+审稿回复                                                                                            |
| 论文交谈       | [researchgpt](https://github.com/mukulpatnaik/researchgpt)                           | 一个开源的LLM研究助手，允许您与研究论文进行对话  | 上传论文，和论文对话。                                                                                                  |
| PPT生成      | [chat-gpt-ppt](https://github.com/williamfzc/chat-gpt-ppt)                           | 使用ChatGPT自动生成PPT           | 1.根据标题一键生成ppt<br/>2.支持多种语言                                                                                   |
| PDF交谈      | [gpt4-pdf-chatbot-langchain](https://github.com/mayooear/gpt4-pdf-chatbot-langchain) | PDF聊天机器人                   | 1.使用新的GPT-4 api为多个大型PDF文件构建chatGPT聊天机器人。                                                                     |
| PDF总结      | [DocsGPT](https://github.com/arc53/DocsGPT)                                | ChatGPT文档阅读器               | 1.支持总结PDF<br/>2.支持分享到discord                                                                                 |
| PDF阅读      | [ebook-GPT-translator](https://github.com/jesselau76/ebook-GPT-translator) | 以各种风格的语言阅读PDF、DOCX文件       |   该工具旨在帮助用户将文本从一种格式转换为另一种格式，以及使用 OpenAI API (model=gpt-3.5-turbo) 将其翻译成另一种语言。 目前支持PDF、DOCX、MOBI和EPUB文件格式转换翻译成EPUB文件及文本文件，可以将文字翻译成多种语言。                                                                                 |
| markdown文档 | [markprompt](https://github.com/motifland/markprompt)                      | 使用GPT4来阅读markdown文档        | 1.它扫描GitHub库里的 Markdown、 Markdoc 和 MDX 文件，并创建可用于创建提示的嵌入                                                                                 |

#### GPT工具-编程

| 名称       | github地址      | 简介                                                                    | 功能                                                                                                             |
|----------| ----------- |-----------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| git工具-01 | [gptcommit](https://github.com/zurawiki/gptcommit)                       | 用ChatGPT提交commit                                                  | git prepare-commit-msg钩子，用于用GPT-3编写提交消息。有了这个工具，你可以很容易地生成清晰、全面和描述性的提交消息                                         |
| git工具-02 | [opencommit](https://github.com/di-sukharev/opencommit)                  | 用ChatGPT提交commit                                                      | 自动生成清晰、全面和描述性的提交消息                                                                                                     |
| 错误检测     | [stackexplain](https://github.com/shobrook/stackexplain)                 | 使用ChatGPT用简单的英语解释你的错误信息                                               | 用stackexplain命令运行pythohn脚本，并且自动检测错误给出正确的修复方法                                                                   |
| SQL客户端   | [sqlchat](https://github.com/sqlchat/sqlchat)                            | SQL Chat是一个基于聊天的SQL客户端，使用自然语言询问数据库问题和查询数据库。                           | 1.支持MySQL和PostgreSQL                                                                                           |
| 代码搜索引擎   | [bloop](https://github.com/BloopAI/bloop)                                | bloop 是一个代码搜索引擎，它使用 GPT-4 来回答有关您的代码的问题。使用自然语言、正则表达式和过滤查询搜索本地和远程存储库    | 1.正则表达式搜索<br/>2.同步本地和Github仓库|                                                        
| 代码生成     | [aiac](https://github.com/gofireflyio/aiac)                              | 命令行的代码生成器                                                             | 1.生成IaC<br/>2.生成docker、k8s配置<br/>3.生成CI/CD<br/>4.生成SQL                                                         |
| 语言转换     | [ai-code-translator](https://github.com/mckaywrigley/ai-code-translator) | 使用 AI 将代码从一种语言翻译成另一种语言。                                          |                                                                                                                |


#### GPT工具-通用

| 名称                                                  | github地址      | 简介                                                                       | 功能                                                                                                             |
|-----------------------------------------------------| ----------- |--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
|实验工具| [Auto-GPT](https://github.com/Torantulino/Auto-GPT) | 自主 GPT-4 实验工具                                                            | 1.用于搜索和信息收集的 Internet 访问<br/>2.长期和短期内存管理<br/>3.访问热门网站和平台<br/>4.使用 GPT-3.5 进行文件存储和汇总<br/>5.支持语音模式 |
| 调教场景机器人-01                                          | [ai-anything](https://github.com/KeJunMao/ai-anything) | 创建各种场景的对话机器人                                                             | 1.写作助理<br/>2.代码解释器<br/>3.日报生成器等                                                                                |
| 调教场景机器人-02                                          | [OpenGpt](https://github.com/futantan/OpenGpt)      | 在几秒钟内创建自己的ChatGPT应用程序                                                    | 1.创建各种场景的对话机器人，比如小红书、日报等                                                                                       |
| 调教场景机器人-03                                          | [Portal](https://github.com/lxfater/Portal)         | Portal是一款传输工具，旨在将ChatGPT的能力整合到用户的工作流程中。它把整个操作系统当成自己的舞台，可以在任意软件上操作ChatGPT | 1.任意软件划词翻译<br/>2.自定义提示语模板<br/>3.对话管理 && 对话图生成                                                                  |

#### GPT工具-音视频

| 名称   | github地址      | 简介                                                                    | 功能                                                                                     |
|------| ----------- |-----------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| 语音   | [speechgpt](https://github.com/hahahumble/speechgpt)             | SpeechGPT是一个允许您与ChatGPT语音谈话的web应用程序，口语练习                              | 1.适配移动端<br/>2.支持超过100种语言<br/>3.语音陪练<br/>4.集成Azure的语音服务                                 |
| 语言   | [chat-with-gpt](https://github.com/cogentapps/chat-with-gpt) | 一个开源的ChatGPT语音应用程序                              | 1.集成ElevenLabs的语音服务<br/>2.支持docker部署                                                   |
| 视频总结 | [BibiGPT](https://github.com/JimmyLv/BibiGPT) | 音视频内容一键总结：哔哩哔哩丨YouTube丨网页丨播客丨会议丨本地文件等                                 | 开发中：支持网页丨播客丨会议丨本地音视频文件等输入，Prompt 和输出端均在持续迭代中                                           |

#### GPT工具-其他

| 名称                                                                             | github地址      | 简介                                                                    | 功能                                                                 |
|--------------------------------------------------------------------------------| ----------- |-----------------------------------------------------------------------|--------------------------------------------------------------------|
| 房间设计                                                                           | [roomGPT](https://github.com/Nutlope/roomGPT)                                    | 上传一张你房间的照片，用人工智能生成你的梦想房间。                                             | 你只需要给你的房间拍一张照，或是房间的 3D 效果图，并将其上传，即可用 AI 生成对应的梦幻房间效果图。（严格来说属于绘画领域的） |
| 结构知识                                                                           | [GraphGPT](https://github.com/varunshenoy/GraphGPT)                              | 自然语言 → 结构知识                                                           | 1.GraphGPT将非结构化的自然语言转换为知识图。传入您最喜欢的电影概要、维基百科页面上令人困惑的段落或视频文本，以生成实体及其关系的可视化图表。                                    |
|AR体验| [ChatARKit](https://github.com/trzy/ChatARKit)                                 | 使用ChatGPT以自然语言创建AR体验                                                  | 1.基于Sketchfab-3D模型网站                                                                                           |
|讲故事| [ChineseAiDungeonChatGPT](https://github.com/bupticybee/ChineseAiDungeonChatGPT) | 中文版的ai地牢，直接使用的openai的ChatGPT api作为讲故事的模型                                                  |                                                                                         |


### GPT插件

#### GPT插件-官方

| 名称                                                                             | github地址      | 简介                                                                    | 功能                                                                                                             |
|--------------------------------------------------------------------------------| --------- |-----------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
|ChatGPT检索插件| [chatgpt-retrieval-plugin](https://github.com/openai/chatgpt-retrieval-plugin) | ChatGPT 检索插件让您可以通过使用日常语言提问来轻松搜索和查找个人或工作文档。                                             |可以对个人或组织文档进行语义搜索和检索。它允许用户通过用自然语言提问或表达需求，从他们的数据源（如文件、笔记或电子邮件）中获取最相关的文档片段。企业可以使用此插件通过 ChatGPT 向员工提供内部文档。|

#### GPT插件-浏览器

| 名称              | github地址      | 简介                                        | 功能                                                                                                                                                                                         |
|-----------------| ----------- |-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 通用插件-01         | [chatGPTBox](https://github.com/josStorer/chatGPTBox)                                                | 将ChatGPT深度集成到您的浏览器中                       | 1.在任何页面随时呼出聊天对话框<br/>2.支持手机等移动设备<br/>3.通过右键菜单总结任意页面<br/>4.框选工具与右键菜单,执行各种你的需求,如翻译,总结,润色,情感分析,段落划分,代码解释,问询<br/>5.支持reddit, quora, youtube, github, gitlab, stackoverflow, zhihu, bilibili等网站 |
| 通用插件-02         | [browser-extension](https://github.com/TaxyAI/browser-extension)                                     | 使用GPT-4自动化你的浏览器                           | 1. 支持github、Netflix、OpenAI、calendar 等网站自动化操作                                                                                                                                               |
| 搜索插件            | [chatgpt-google-extension](https://github.com/wong2/chatgpt-google-extension)                        | 在Google搜索结果旁边显示ChatGPT响应                    | 1. 右侧显示ChatGPT搜索内容<br/>2.自定义触发模式<br/>3.支持切换语言                                                                                                                                              |
| 文本框插件           | [chatgpt-chrome-extension](https://github.com/gragland/chatgpt-chrome-extension)                     | 将ChatGPT集成到互联网上的每个文本框中!                   | 1.在文本框中右键Ask ChatGPT使用<br/>2.用它来写推特，修改电子邮件，修复代码错误，或其他任何你需要的东西                                                                                                                              |
| 文本框插件-推特版       | [tweetGPT](https://github.com/yaroslav-n/tweetGPT)                                                   | ChatGPT浏览器插件-推特网页                         | 1.在推特网页版中生成推文和回复                                                                                                                                                                           |
| 翻译插件-01         | [openai-translator](https://github.com/yetone/openai-translator)                                     | 基于 ChatGPT API 的划词翻译浏览器插件和跨平台桌面端应用。       | 1.划词翻译                                                                                                                                                                                     |
| 翻译插件-02         | [immersive-translate](https://github.com/immersive-translate/immersive-translate)                    | 沉浸式双语网页翻译扩展。       | 1.双语显示，中英文对照。<br/>2.针对常见主流网站进行定制优化，如 Twitter，Reddit，Discord, Gmail, Telegram, Youtube, Hacker News 等。<br/>3.支持 PDF 文件，EPUB 电子书双语翻译，制作与导出。<br/>4.支持移动端                                      |
| 下载插件            | [ChatGPT-pdf](https://github.com/liady/ChatGPT-pdf)                                                  | 一个Chrome扩展下载你的聊天gpt历史PNG, PDF或可分享的链接。     | 1.下载chatgpt官网聊天历史PNG                                                                                                                                                                       |
| ChatGPT增强插件     | [chatgpt-advanced](https://github.com/qunash/chatgpt-advanced)                                       | 一个浏览器扩展，增强您的ChatGPT提示与网络结果。               | 1.这个浏览器扩展为ChatGPT添加了web访问功能。从聊天机器人获得更多相关和最新的答案!                                                                                                                                            |
| 语音插件-01         | [talk-to-chatgpt](https://github.com/C-Nedelcu/talk-to-chatgpt)                                      | 用你的声音与ChatGPT AI交谈，并通过声音听它的答案。            | 1.和ChatGPT语音交流!<br/>2.支持多种语言                                                                                                                                                               |
| 语音插件-02         | [assistant-chat-gpt](https://github.com/idosal/assistant-chat-gpt)                                   | 嵌入ChatGPT作为免提语音助手。                        | 1.ChassistantGPT支持60多种语言和方言。选择您的母语和自定义触发短语(可在选项卡中配置)                                                                                                                                       |
| 分享插件            | [sharegpt](https://github.com/domeccleston/sharegpt)                                                 | 轻松地共享ChatGPT对话的永久链接到https://sharegpt.com/ | 1.一键分享自己ChatGPT对话到https://sharegpt.com                                                                                                                                                     |
| 阅读插件            | [chatgpt-arxiv-extension](https://github.com/hunkimForks/chatgpt-arxiv-extension)                    | arxiv论文使用ChatGPT                          | 1.能帮你读arxiv论文，在一些地方给出注解                                                                                                                                                                    |
| 总结插件-YouTube视频版 | [YouTube_Summary_with_ChatGPT](https://github.com/kazuki-sf/YouTube_Summary_with_ChatGPT)            | 通过OpenAI的ChatGPT人工智能技术，你可以获得YouTube视频文本和视频摘要。                     | 1.一键总结YouTube视频内容                                                                                                                                                                          |
| 总结插件            | [chatgpt-google-summary-extension](https://github.com/sparticleinc/chatgpt-google-summary-extension) | 它可以在Google搜索和Yuoutbe旁边显示来自ChatGPT的摘要，还支持 Yahoo、Github、Bing等。                     |                                                                                                                                                                           |

#### GPT插件-第三方应用

| 名称              | github地址                                                                              | 简介                                           | 功能                                                                                          |
|-----------------|---------------------------------------------------------------------------------|----------------------------------------------|---------------------------------------------------------------------------------------------|
| 编辑器-vscode插件    | [chatgpt-vscode](https://github.com/mpociot/chatgpt-vscode)                     | 一个允许你使用ChatGPT的VSCode扩展                      | 1.使用编辑器中的代码片段通过侧栏中的输入框查询ChatGPT<br/>2.右键单击代码选择并运行其中一个上下文菜单快捷方式<br/>3.在编辑器旁边的面板中查看ChatGPT的响应 |
| 编辑器-JetBrains插件 | [JetBrains-插件](https://github.com/dromara/ChatGPT)                              | 支持ChatGPT在JetBrains系列IDE上运行的一款插件             | 1.使用编辑器中的代码片段通过侧栏中的输入框查询ChatGPT<br/>2.右键单击代码选择并运行其中一个上下文菜单快捷方式<br/>3.在编辑器旁边的面板中查看ChatGPT的响应 |
| 编辑器-intellij插件  | [intellij-chatgpt](https://github.com/LiLittleCat/intellij-chatgpt)             | 一个将ChatGPT和其他第三方镜像网站整合到JetBrains IDEs 的插件。             | 1.集成免费的第三方镜像网站，并且更新方便。                                                                                          |
| 编辑器-IDA Pro插件   | [Gepetto](https://github.com/JusticeRage/Gepetto)                               | 一个接入了ChatGPT接口的IDA Pro插件                     | 1.支持解释函数<br/>2.支持重命名变量                                                                      |
| 编辑器-Neovim插件    | [ChatGPT.nvim](https://github.com/jackMort/ChatGPT.nvim)                        | 用于与OpenAI GPT-3聊天机器人交互的Neovim插件              | 1.命令打开交互窗口<br/>2.支持Awesome ChatGPT Prompts指令                                                |
| 效率工具-raycast插件  | [chatgpt-raycast](https://github.com/abielzulio/chatgpt-raycast)                | 一个raycast的ChatGPT插件                          | 1.使用Mac快捷键直接唤起ChatGPT进行对话<br/>2.自定义对话指令                                                     |
| 谷歌文档插件          | [docGPT](https://github.com/cesarhuret/docGPT)                                  | ChatGPT直接在谷歌文档作为编辑器插件                        | 1.ChatGPT直接集成到谷歌Docs中<br/>2.选中doc一键发送给chatgpt                                               |
| Kubernetes插件-01 | [kubernetes-chatgpt-bot](https://github.com/robusta-dev/kubernetes-chatgpt-bot) | 使用ChatGPT解决Kubernetes问题                      | 1.向ChatGPT直接发生Prometheus警报询问如何修复告警<br/>2.依赖可观测性神器robusta                                    |
| Kubernetes插件-02 | [kubectl-ai](https://github.com/sozercan/kubectl-ai)              | 这个项目是一个kubectl插件，使用OpenAI GPT生成和应用Kubernetes清单                                     | 1.用自然语言生成Kubernetes配置                                                                       |
| github插件-01     | [chatgpt-action](https://github.com/kxxt/chatgpt-action)          | github的codeReview插件                          | 1.让ChatGPT自动reviewCode<br/>2.让chatgpt检查你的PR                                                 |
| github插件-02     | [ChatGPT-CodeReview](https://github.com/anc95/ChatGPT-CodeReview) | github的代码审查机器人                               | 1.让ChatGPT自动reviewCode<br/>2.让chatgpt检查你的PR                                                 |
| 小爱插件            | [xiaogpt](https://github.com/yihong0618/xiaogpt)         | 在小爱音响上接入ChatGPT                              | 1.使用小米AI扬声器播放ChatGPT                                                                        |
| 3D软件Blender插件   | [BlenderGPT](https://github.com/gd3kr/BlenderGPT)        | 在Blender上接入ChatGPT                           | 1.在只需要输入文本，即可快速构建3D模型                                                                       |
| Siri插件          | [ChatGPT-Siri](https://github.com/Yue-Yang/ChatGPT-Siri) | 通过 Siri 启动「快捷指令」连接 ChatGPT API，让 Siri 变身 AI 聊天助手 | 1.支持连续对话<br/>2.配置系统prompt<br/>3.保存聊天记录                                                      |

### GPT开源平替机器人

| github地址      | 简介                                                                | 功能                                                                                                  |
| ----------- |-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [Open-Assistant](https://github.com/LAION-AI/Open-Assistant)                       | OpenAssistant是一个基于聊天的助手，可以理解任务，可以与第三方系统交互，并动态检索信息。                | Open Assistant 是一个旨在让每个人都能访问基于聊天的大型语言模型的项目。                                                         |
| [gpt4all](https://github.com/nomic-ai/gpt4all)     | 一个聊天机器人接受了大量干净的助手数据的训练，包括代码、故事和对话                                 | 1. 本地训练，调教                                                                                          |
| [PaLM-rlhf-pytorch](https://github.com/lucidrains/PaLM-rlhf-pytorch)                       | 在PaLM架构之上实现RLHF(带人类反馈的强化学习)。基本上是ChatGPT，但有PaLM。                   |                                                                                                     |
| [OpenChatKit](https://github.com/togethercomputer/OpenChatKit)                       | 前OpenAI团队打造，OpenChatKit提供了一个强大的开源基础，可以为各种应用程序创建专门的和通用的聊天机器人。      | 1.200亿参数的语言模型<br/>2.用户只需准备自己的数据集，并使用OpenChatKit的配方来微调模型即可获得高精度的结果。                                  |
| [text-generation-webui](https://github.com/oobabooga/text-generation-webui)                       | 一个用于运行大型语言模型(如GPT-J 6B, OPT, GALACTICA, LLaMA和Pygmalion)的梯度web UI |                                                                                                     |
| [stanford_alpaca](https://github.com/tatsu-lab/stanford_alpaca)                       | 斯坦福的羊驼模型（小羊驼）                                                     |                                                                                                     |
| [alpaca-lora](https://github.com/tloen/alpaca-lora)   | 轻量级 ChatGPT 的开源实现，小羊驼-lora                                        | 1. 使用了LoRA轻量级模型<br/>2.只需要训练很小一部分参数就可以获得媲美 Standford Alpaca 模型的效果<br/>3.要RTX 4090才能玩                 |
| [ChatRWKV](https://github.com/BlinkDL/ChatRWKV)                       | ChatRWKV是对标ChatGPT的开源项目，希望做"大规模语言模型的Stable Diffusion"             |                                                                                                     |
| [ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B)                       | 清华大学研发的产品，ChatGLM-6B 是一个开源的、支持中英双语的对话语言模型                         | 1.62 亿参数<br/>2.用户可以在消费级的显卡上进行本地部署（INT4 量化级别下最低只需 6GB 显存）                                            |
| [dolly](https://github.com/databrickslabs/dolly)                       | Databricks的Dolly是一个在Databricks机器学习平台上训练的大型语言模型                    | 1.Dolly 使用 Alpaca 数据，对两年前的开源EleutherAI 60亿参数模型进行微调                                                  |
| [BELLE](https://github.com/LianjiaTech/BELLE)                       | 开源中文对话大模型                                                         | 1.现阶段本项目基于一些开源预训练大语言模型（如BLOOM、LAMMA等），针对中文做了优化，模型调优仅使用由ChatGPT生产的数据（不包含任何其他数据）。                     |
| [KoboldAI-Client](https://github.com/KoboldAI/KoboldAI-Client)                       | KoboldAI-你通往GPT写作的大门                                              | 这是一个基于浏览器的前端I -辅助写作与多个本地和远程I模型                                                                      |
| [Chinese-LLaMA-Alpaca](https://github.com/ymcui/Chinese-LLaMA-Alpaca)     | 中文LLaMA&Alpaca大语言模型+本地部署                         | 1.🚀 开源了经过中文文本数据预训练的中文LLaMA大模型<br/>🚀 开源了进一步经过指令精调的中文Alpaca大模型<br/>🚀 快速地使用笔记本电脑（个人PC）本地部署和体验量化版大模型 |
| [ChatYuan](https://github.com/clue-ai/ChatYuan)     |国产的支持中英双语的功能型对话语言大模型：ChatYuan                      | 1.ChatYuan-large-v2是ChatYuan系列中以轻量化实现高质量效果的模型之一，用户可以在消费级显卡、 PC甚至手机上进行推理（INT4 最低只需 400M ）。           |
| [FastChat](https://github.com/lm-sys/FastChat)     | 一个用于训练、服务和评估基于大型语言模型的聊天机器人的开放平台。 | 1.斯坦福联手CMU、UC伯克利等机构的学者再次发布了130亿参数模型骆马（Vicuna），仅需300美元就能实现ChatGPT 90%的性能。                                                                                                                       |
| [minGPT](https://github.com/karpathy/minGPT)     | karpathy大神发布的一个 OpenAI GPT(生成预训练转换器)训练的最小 PyTorch 实现，代码十分简洁明了，适合用于动手学习 GPT 模型。                         |                                                                                                     |
| [LLaMA-Adapter](https://github.com/ZrrSkywalker/LLaMA-Adapter)     | 高效微调一个聊天机器人：LLaMA-Adapter🚀                        | 1.LLaMA在1小时内按照指示和1.2M参数进行微调                                                                         |
| [lit-llama](https://github.com/Lightning-AI/lit-llama)     | Lightning-AI 基于nanoGPT的LLaMA语言模型的实现。支持量化，LoRA微调，预训练。                        |                                                                                                     |
| [trlx](https://github.com/carperai/trlx)                       | 一个通过人类反馈强化学习(RLHF)对语言模型进行分布式训练的repo                               | 1.支持高达20b参数的在线RL和更大模型的离线RL。基本上就是你用来微调GPT到ChatGPT的项目                                                 |
| [minChatGPT](https://github.com/ethanyanjiali/minChatGPT)                       | 微型版ChatGPT，一个将语言模型与类似ChatGPT的RLHF对齐的最小示例                          |                                                                                                     |

### 专业领域机器人

| 名称      | github地址      | 简介                                                                | 功能                                                                                                  |
|---------| ----------- |-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| 医生机器人   | [ChatDoctor](https://github.com/Kent0n-Li/ChatDoctor) | 利用医学领域知识在LLaMA模型基础上改进的医学聊天模型                                             | 1.数据训练来自HealthCareMagic.com的20万次病人和医生之间的真实对话、来自icliniq.com的26k个病人和医生之间的真实对话                                    |
| 生物医学机器人 | [BioGPT](https://github.com/microsoft/BioGPT) | 微软团队推出的基于生物医学研究文献的大型语言模型                                                 | 1.提取诸如基因或疾病的生物医学实体<br/>2.可以回答生物医学问题的聊天机器人<br/>3.生物医学领域的总结和自动完成                                                 |


### Prompt对话指令
| github地址                                              | 简介                             | 功能                                |
|-------------------------------------------------|--------------------------------|-----------------------------------|
| [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) | ChatGPT指令合集，以更好地使用ChatGPT      | 各种场景对话调教                          |
| [awesome-chatgpt-prompts-zh](https://github.com/PlexPt/awesome-chatgpt-prompts-zh) | ChatGPT指令合集（中文版），以更好地使用ChatGPT | 各种场景对话调教（中文版）                     |
| [Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) | 指令工程师                          | 教你如何调教、训练AI                       |
| [ChatGPT-Shortcut](https://github.com/rockbenben/ChatGPT-Shortcut) | 让生产力加倍的 ChatGPT 快捷指令           | 按照领域和功能分区，可对提示词进行标签筛选、关键词搜索和一键复制。 |
| [Awesome-ChatGPT-prompts-ZH_CN](https://github.com/L1Xu4n/Awesome-ChatGPT-prompts-ZH_CN) | 如何将ChatGPT调教成一只猫娘              |                                   |
| [ChatGPT_DAN](https://github.com/0xk1h0/ChatGPT_DAN) | ChatGPT"越狱"指令                  |                                   |
| [ChatGPT-Data-Science-Prompts](https://github.com/travistangvh/ChatGPT-Data-Science-Prompts) | ChatGPT"数据科学"指令                |                                   |

### 其他（平台、逆向工程）

| github地址                                                | 简介                         | 功能                                                                                           |
|---------------------------------------------------------|----------------------------|----------------------------------------------------------------------------------------------|
| [Reverse ChatGPT](https://github.com/acheong08/ChatGPT) | ChatGPT逆向工程                | 提取ChatGPT的API                                                                                |
| [Reverse EdgeGPT](https://github.com/acheong08/EdgeGPT) | NewBing逆向工程                | 提取NewBing的API                                                                                |
| [langchain](https://github.com/hwchase17/langchain)     | 开发自己的 ChatGPT 应用：langchain | 它可以帮助开发者将LLM与其他计算或知识源结合起来，创建更强大的应用程序。                                                        |
| [国内镜像站收集](https://github.com/GentleLemon/ChatGPT-Anything)       |收集国内免费ChatGPT镜像，替代品收录  | |


---

## 相关资料
- [ChatGPT 中文指南](https://github.com/yzfly/awesome-chatgpt-zh)
- [开源-chatgpt-替代品列表](https://github.com/nichtdax/awesome-totally-open-chatgpt)
- [ChatGPT工具，演示，文档列表](https://github.com/humanloop/awesome-chatgpt)

---

## 贡献

这个awesome-open-gpt是我个人收集的关于GPT的有趣的开源项目，热烈欢迎你的贡献和建议，提交PR。
