import pandas as pd

file_path = 'icc_t20_worldcup_2022_23_matches plus links.csv'

# خواندن ستون 'link' از فایل CSV
webpages = pd.read_csv(file_path, usecols=['link'])

# نمایش داده‌های خوانده‌شده
print(webpages)

