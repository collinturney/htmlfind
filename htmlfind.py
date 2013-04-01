#!/usr/bin/env python

import sys
import argparse
import requests
import HTMLParser
from urlparse import urljoin
from lxml import etree


def configure():
    parser = argparse.ArgumentParser()

    parser.add_argument('-u', '--url', required=True)
    parser.add_argument('-x', '--xpath', required=True)
    parser.add_argument('-a', '--absolute-urls', action='store_true')

    args = parser.parse_args()

    return args

if __name__ == "__main__":
    args = configure()

    response = requests.get(args.url)

    html_parser = etree.HTMLParser(encoding=response.encoding)
    dom = etree.fromstring(response.content, parser=html_parser)

    results = dom.xpath(args.xpath)

    if args.absolute_urls:
        results = [urljoin(args.url, x) for x in results]

    if results:
        print("\n".join(results))
