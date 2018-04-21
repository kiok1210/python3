from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

appid = 1400080597
appkey = "2ba0bba2b0b6f85c46ce33a968f6637b"
phone_numbers = ["18119606753"]

ssender = SmsSingleSender(appid, appkey)
result = ''
try:
    result = ssender.send(0, 86, phone_numbers[0],
        "测试短信，普通单发，深圳，小明，上学。")
except HTTPError as e:
    print(e)
except Exception as e:
    print(e)

print(result)