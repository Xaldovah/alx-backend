#!/usr/bin/env python3

import requests
import csv


url = "https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240126%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240126T225026Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=01d23278c605b31849a0039a90f4ab109268bacdb7104ee554e0a55d8d785543"
response = requests.get(url)

if response.status_code == 200:
    with open("Popular_Baby_Names.csv", "w", newline="") as csvfile:
        reader = csv.reader(response.text.splitlines())
        writer = csv.writer(csvfile)

        for row in reader:
            writer.writerow(row)

else:
    print("Error:", response.status_code)
