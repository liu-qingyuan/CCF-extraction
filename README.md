# CCF推荐列表爬虫 / CCF Recommended List Crawler

## 项目说明 / Project Description

这个项目包含用于爬取中国计算机学会(CCF)推荐的国际学术会议和期刊列表的工具。

This project contains tools for crawling the list of international academic conferences and journals recommended by China Computer Federation (CCF).

### 文件结构 / File Structure

- `ccf_venues.py`: 爬虫脚本 / Crawler script
- `ccf_venues.csv`: 输出的数据文件 / Output data file

## 数据格式 / Data Format

### ccf_venues.csv 列说明 / Column Description

- `name`: 会议/期刊简称 / Venue abbreviation
- `full_name`: 会议/期刊全称 / Full name of the venue
- `publisher`: 出版商 / Publisher
- `url`: DBLP链接 / DBLP link
- `level`: CCF等级(A/B/C) / CCF level (A/B/C)
- `field`: 研究领域 / Research field
- `type`: 类型(conference/journal) / Type (conference/journal)

### 涵盖领域 / Covered Fields

1. 计算机体系结构/并行与分布计算/存储系统  
   Computer Architecture/Parallel and Distributed Computing/Storage System
2. 计算机网络  
   Computer Networks
3. 网络与信息安全  
   Network and Information Security
4. 软件工程/系统软件/程序设计语言  
   Software Engineering/System Software/Programming Language
5. 数据库/数据挖掘/内容检索  
   Database/Data Mining/Content Retrieval
6. 计算机科学理论  
   Theoretical Computer Science
7. 计算机图形学与多媒体  
   Computer Graphics and Multimedia
8. 人工智能  
   Artificial Intelligence
9. 人机交互与普适计算  
   Human-Computer Interaction and Ubiquitous Computing
10. 交叉/综合/新兴  
    Cross/Comprehensive/Emerging Fields

## 使用方法 / Usage

```bash
# 安装依赖 / Install dependencies
pip install requests beautifulsoup4 pandas

# 运行爬虫 / Run crawler
python ccf_venues.py
```

## 输出示例 / Output Example

```csv
name,full_name,publisher,url,level,field,type
TOCS,ACM Transactions on Computer Systems,ACM,http://dblp.uni-trier.de/db/journals/tocs/,A,计算机体系结构/并行与分布计算/存储系统,journal
TOS,ACM Transactions on Storage,ACM,http://dblp.uni-trier.de/db/journals/tos/,A,计算机体系结构/并行与分布计算/存储系统,journal
TCAD,IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems,IEEE,http://dblp.uni-trier.de/db/journals/tcad/,A,计算机体系结构/并行与分布计算/存储系统,journal
TC,IEEE Transactions on Computers,IEEE,http://dblp.uni-trier.de/db/journals/tc/index.html,A,计算机体系结构/并行与分布计算/存储系统,journal
TPDS,IEEE Transactions on Parallel and Distributed Systems,IEEE,http://dblp.uni-trier.de/db/journals/tpds/,A,计算机体系结构/并行与分布计算/存储系统,journal
```

## 注意事项 / Notes

1. 请遵守网站的爬虫规则 / Please follow the website's crawler rules
2. 建议添加适当的请求延迟 / Recommend adding appropriate request delays
3. 数据仅供参考，以CCF官网为准 / Data is for reference only, please refer to the official CCF website 
