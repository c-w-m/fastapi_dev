"""
This is private information used for development and testing
DO NOT CHECK-IN THIS FILE!!!!

rename file to: proxy_private.py
which is listed as a file to ignore by git in '.gitignore'.
"""
COMPANY_NAME='xxxxxxx'

HTTP_PROXY=f"http://proxy-web.{COMPANY_NAME}.com:80"
HTTPS_PROXY=f"http://proxy-web.{COMPANY_NAME}.com:80"
NO_PROXY=f"*.{COMPANY_NAME}.com,localhost,127.0.0.1,.{COMPANY_NAME}.com,addmmsi"
