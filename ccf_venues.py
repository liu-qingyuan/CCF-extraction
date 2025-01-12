import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def clean_text(text):
    """清理文本数据"""
    if not text:
        return ''
    return ' '.join(text.strip().split())

def parse_venue_row(row, current_field, current_level, current_type):
    """解析每一行的会议/期刊信息"""
    cells = row.find_all(['td', 'div'])
    if len(cells) < 4:
        return None
        
    # 跳过表头行
    if '序号' in cells[0].text:
        return None
        
    # 提取信息
    name_cell = clean_text(cells[1].text)
    full_name = clean_text(cells[2].text)
    publisher = clean_text(cells[3].text)
    url = cells[4].find('a')['href'] if cells[4].find('a') else ""
    
    # 提取缩写（如果存在）
    name = name_cell.strip()
    
    return {
        'name': name,
        'full_name': full_name,
        'publisher': publisher,
        'url': url,
        'level': current_level,
        'field': current_field,
        'type': current_type
    }

def scrape_ccf_venues(url, field_name):
    """爬取指定URL的CCF推荐列表
    
    Args:
        url: CCF推荐列表的URL
        field_name: 领域名称
    
    Returns:
        list: 包含所有venue信息的列表
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        
        venues = []
        current_type = None
        current_level = ''
        
        for element in soup.find_all(['h4', 'h3', 'ul']):
            if element.name == 'h4':
                text = element.text.strip()
                if '刊物' in text:
                    current_type = 'journal'
                elif '会议' in text:
                    current_type = 'conference'
                
            elif element.name == 'h3':
                level_text = element.text.strip()
                if 'A类' in level_text:
                    current_level = 'A'
                elif 'B类' in level_text:
                    current_level = 'B'
                elif 'C类' in level_text:
                    current_level = 'C'
                    
            elif element.name == 'ul' and element.get('class') and 'x-list3' in element.get('class'):
                if current_type:
                    rows = element.find_all('li')
                    for row in rows:
                        venue = parse_venue_row(row, field_name, current_level, current_type)
                        if venue:
                            venues.append(venue)
        
        return venues
        
    except Exception as e:
        print(f"Error scraping {url}: {str(e)}")
        return []

def scrape_all_fields():
    """爬取所有领域的CCF推荐列表"""
    # 定义要爬取的URL和对应的领域名称
    fields = [
        {
            'url': 'https://www.ccf.org.cn/Academic_Evaluation/ARCH_DCP_SS/',
            'name': '计算机体系结构/并行与分布计算/存储系统'
        },
        {
            'url': 'https://www.ccf.org.cn/Academic_Evaluation/CN/',
            'name': '计算机网络'
        },
        {
            'url': 'https://www.ccf.org.cn/Academic_Evaluation/NIS/',
            'name': '网络与信息安全'
        },
        {
            'url': 'https://www.ccf.org.cn/Academic_Evaluation/TCSE_SS_PDL/',
            'name': '软件工程/系统软件/程序设计语言'
        },
        {
            'url': 'https://www.ccf.org.cn/Academic_Evaluation/DM_CS/',
            'name': '数据库/数据挖掘/内容检索'
        },
        {
            'url': 'https://www.ccf.org.cn/Academic_Evaluation/TCS/',
            'name': '计算机科学理论'
        },
        {
            'url': 'https://www.ccf.org.cn/Academic_Evaluation/CGAndMT/',
            'name': '计算机图形学与多媒体'
        },
        {
            'url': 'https://www.ccf.org.cn/Academic_Evaluation/AI/',
            'name': '人工智能'
        },
        {
            'url': 'https://www.ccf.org.cn/Academic_Evaluation/HCIAndPC/',
            'name': '人机交互与普适计算'
        },
        {
            'url': 'https://www.ccf.org.cn/Academic_Evaluation/Cross_Compre_Emerging/',
            'name': '交叉/综合/新兴'
        }
    ]
    
    all_venues = []
    for field in fields:
        print(f"\nScraping {field['name']}...")
        try:
            venues = scrape_ccf_venues(field['url'], field['name'])
            all_venues.extend(venues)
            print(f"Found {len(venues)} venues")
        except Exception as e:
            print(f"Error scraping {field['name']}: {str(e)}")
            continue
    
    # 转换为DataFrame并保存
    if all_venues:
        df = pd.DataFrame(all_venues)
        required_columns = ['name', 'full_name', 'publisher', 'url', 'level', 'field', 'type']
        for col in required_columns:
            if col not in df.columns:
                df[col] = ''
        
        print("\nType distribution:")
        print(df['type'].value_counts())
        print("\nField distribution:")
        print(df['field'].value_counts())
        
        df.to_csv('ccf_venues.csv', index=False, encoding='utf-8-sig')
        print(f"\nTotal venues scraped: {len(all_venues)}")
    
    return all_venues

if __name__ == "__main__":
    scrape_all_fields()