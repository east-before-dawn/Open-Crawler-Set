import time
import os
from pprint import pprint


class UintTest(object):

    def crawler_test(self):
        pprint("--------")


if __name__ == '__main__':
    page_cnt = 17
    pprint(page_cnt)
    pages_url = \
        "https://openapi.book118.com/getPreview.html?" \
        "&project_id=1&aid=294721773&t=d50bd8d0481629a9af934d1077041212" \
        "&view_token=xuRQtPJrD34tJ3lrAQLiuJlfKkbH2z98" \
        "&page="
    pages_url_tail = "&filetype=pdf&callback=jQuery"

    pages_url = pages_url + str(page_cnt) + pages_url_tail
    pprint(pages_url)

