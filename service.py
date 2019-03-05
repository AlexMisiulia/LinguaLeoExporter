import json
from http.cookiejar import CookieJar

import requests
import logging
import http.client


class Lingualeo:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.cj = CookieJar()

        http.client.HTTPConnection.debuglevel = 1

        logging.basicConfig()
        logging.getLogger().setLevel(logging.DEBUG)
        requests_log = logging.getLogger("requests.packages.urllib3")
        requests_log.setLevel(logging.DEBUG)
        requests_log.propagate = True

    def auth(self):
        url = "http://api.lingualeo.com/api/login"
        values = {
            "email": self.email,
            "password": self.password
        }

        return self.get_content(url, values)

    def add_word(self, word, tword, context):
        url = "http://api.lingualeo.com/addword"
        values = {
            "word": word,
            "tword": tword,
            "context": context,
        }
        self.get_content(url, values)

    def get_translates(self, word):
        url = "http://api.lingualeo.com/gettranslates?word=" + word

        try:
            result = self.get_content(url, {})
            translate = result["translate"][0]
            return {
                "is_exist": translate["is_user"],
                "word": word,
                "tword": translate["value"].encode("utf-8")
            }
        except Exception as e:
            return e.message

    def get_content(self, url, values):
        print(f'Request: {url}, {values}')
        response = requests.post(url, values, cookies=self.cj)

        print(f'Response: {response.raw}')
        self.cj = response.cookies
        return json.loads(response.text)
