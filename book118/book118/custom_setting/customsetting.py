# -*- coding: utf-8 -*-


START_URL = 'https://openapi.book118.com/getPreview.html?' \
            '&project_id=1' \
            '&aid=294721773&t=d50bd8d0481629a9af934d1077041212' \
            '&view_token=xuRQtPJrD34tJ3lrAQLiuJlfKkbH2z98' \
            '&page=1' \
            '&filetype=pdf' \
            '&callback=jQuery'

DEFAULT_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,'
              'image/avif,'
              'image/webp,image/apng,*/*;q=0.8,application/signed-exchange;'
              'v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'openapi.book118.com',
    'sec-ch-ua': '\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"90\", '
                 '\"Google Chrome\";v=\"90\"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1'
    # 'Referer': 'https://max.book118.com/'
}

# https://openapi.book118.com/getPreview.html?&project_id=1&aid=294721773&t=d50bd8d0481629a9af934d1077041212&view_token=xuRQtPJrD34tJ3lrAQLiuJlfKkbH2z98&page=1&filetype=pdf&callback=jQuery
# https://openapi.book118.com/getPreview.html?&project_id=1&aid=294721773&t=d50bd8d0481629a9af934d1077041212&view_token=xuRQtPJrD34tJ3lrAQLiuJlfKkbH2z98&page=7&filetype=pdf&callback=jQuery

# pages_url = \
#     "https://openapi.book118.com/getPreview.html?" \
#     "&project_id=1&aid=294721773&t=d50bd8d0481629a9af934d1077041212" \
#     "&view_token=xuRQtPJrD34tJ3lrAQLiuJlfKkbH2z98" \
#     "&page=13" \
#     "&filetype=pdf&callback=jQuery"
