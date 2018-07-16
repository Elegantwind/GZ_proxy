# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import json
import os
import sys


# from DataBaseFunction.Real_time_data_statistics_SQL import insert_realtime_data
# from ProxyFunction.url import WritUrl


class RealTimResponse:
    def __int__(self):
        self.url = ''
        self.request_method = ''
        # 协议
        self.request_scheme = ''
        self.request_host = ''
        self.request_port = ''
        self.request_path = ''
        self.request_http_version = ''
        self.request_headers = ''
        self.request_content = ''
        self.request_text = ''
        self.response_http_version = ''
        self.response_status_code = ''
        self.response_reason = ''
        self.response_headers = ''
        self.response_content = ''
        self.response_text = ''

    def request(self, flow):
        self.url = str(flow.request.url)
        self.request_method = flow.request.method
        # 协议
        self.request_scheme = flow.request.scheme
        self.request_host = flow.request.host
        self.request_port = flow.request.port
        self.request_path = flow.request.path
        self.request_http_version = flow.request.http_version
        temp_header = {}
        for key, value in flow.request.headers.items():
            temp_header.update({key: value})
        self.request_headers = json.dumps(temp_header)
        self.request_content = flow.request.content
        self.request_text = flow.request.text

    def response(self, flow):
        self.response_http_version = flow.response.http_version
        self.response_status_code = flow.response.status_code
        self.response_reason = flow.response.reason
        temp_header = {}
        for key, value in flow.request.headers.items():
            temp_header.update({key: value})
        self.response_headers = json.dumps(temp_header)
        self.response_content = flow.response.content
        self.response_text = flow.response.text
        print((self.url, self.request_method, self.request_scheme, self.request_host, self.request_port,
                             self.request_path, self.request_http_version, self.request_headers, self.request_content,
                             self.response_http_version, self.response_status_code, self.response_reason,
                             self.response_headers,
                             self.response_content, self.response_text))
        # 写入数据库
        # insert_realtime_data(self.url, self.request_method, self.request_scheme, self.request_host, self.request_port,
        #                      self.request_path, self.request_http_version, self.request_headers, self.request_content,
        #                      self.response_http_version, self.response_status_code, self.response_reason,
        #                      self.response_headers,
        #                      self.response_content, self.response_text)


class WritUrl:
    def request(self, flow):
        url = flow.request.url
        print(url)
        with open('./urllog.txt', 'a+') as f:
            f.write(url)


def start():
    return RealTimResponse()


addons = [
    WritUrl(), RealTimResponse()
]
