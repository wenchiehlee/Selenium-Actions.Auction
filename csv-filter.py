#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys
from csvfilter import Processor
import csv

def filter_rows(row):
    return "初上櫃" in row or "初上市" in row or "創新板初上市" in row or "第一上市初上市" in row or "創新板轉列上市" in row

# Set up processor with fields to match the expected number of columns in the CSV
processor = Processor(fields=list(range(26)))  # Fields 0 to 25
processor.add_validator(filter_rows)

# Modify the output stream to avoid additional newlines
sys.stdout.reconfigure(newline='')

# Set up CSV writer for standard output, with all items quoted
writer = csv.writer(sys.stdout, quotechar='"', quoting=csv.QUOTE_ALL)

# Write header row to standard output
writer.writerow([
    "序號", "開標日期", "證券名稱", "證券代號", "發行市場", "發行性質", "競拍方式", "投標開始日", "投標結束日", "競拍數量(張)",
    "最低投標價格(元)", "最低每標單投標數量(張)", "最高投(得)標數量(張)", "保證金成數(%)", "每一投標單投標處理費(元)",
    "撥券日期(上市、上櫃日期)", "主辦券商", "得標總金額(元)", "得標手續費率(%)", "總合格件", "合格投標數量(張)", "最低得標價格(元)",
    "最高得標價格(元)", "得標加權平均價格(元)", "承銷價格(元)", "取消競價拍賣(流標或取消)"
])

# Process rows and write each filtered row to standard output
for filtered_row in processor.process(sys.stdin):
    writer.writerow(filtered_row)
