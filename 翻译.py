import hashlib
import json
import random
import time

import requests


def fanyi(n):
    lts = str(int(time.time() * 1000))
    salt = lts + str(random.randint(1, 10))
    sign = hashlib.md5(("fanyideskweb" + n + salt +
                        "Ygy_4c=r#e#4EX^NUGUc5").encode()).hexdigest()

    url = "https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/94.0.4606.71 Safari/537.36 Core/1.94.184.400 QQBrowser/11.3.5190.400",
        "Cookie": "OUTFOX_SEARCH_USER_ID=-209804399@10.105.137.202; OUTFOX_SEARCH_USER_ID_NCOO=2012611780.3580341; "
                  "___rl__test__cookies=1669987334140",
        "Referer": "https://fanyi.youdao.com/"
    }
    data = {
        "i": n,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": salt,
        "sign": sign,
        "lts": lts,
        "bv": "abc3d146c18668aa006a31382c136667",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME"
    }
    res_data = requests.post(url, headers=header, data=data)
    res_dic = json.loads(res_data.text)
    return res_dic["translateResult"][0][0]["tgt"]


if __name__ == "__main__":
    while True:
        e = input("请输入你要翻译的内容:")
        if e == "q":
            break
        lts = str(int(time.time() * 1000))
        salt = lts + str(random.randint(1, 10))
        sign = hashlib.md5(("fanyideskweb" + e + salt +
                            "Ygy_4c=r#e#4EX^NUGUc5").encode()).hexdigest()

        url = "https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.184.400 QQBrowser/11.3.5190.400",
            "Cookie": "OUTFOX_SEARCH_USER_ID=-209804399@10.105.137.202; OUTFOX_SEARCH_USER_ID_NCOO=2012611780.3580341; ___rl__test__cookies=1669987334140",
            "Referer": "https://fanyi.youdao.com/"
        }
        data = {
            "i": e,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign,
            "lts": lts,
            "bv": "abc3d146c18668aa006a31382c136667",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME"
        }
        res_data = requests.post(url, headers=header, data=data)
        res_dic = json.loads(res_data.text)
        print(res_dic["translateResult"][0][0]["tgt"])
