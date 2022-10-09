import pytest
import requests

from utils.read_data import get_data

from utils.read_ini import read_ini

url = read_ini()['host']['api_sit_url']


# @pytest.mark.parametrize("param", get_data["mobile_belong"])
def test_mobile():
    param = get_data["mobile_belong"]
    print("测试手机号归属地get请求")
    r = requests.get('https://api.binstd.com/shouji/query',
                     params={"shouji": param["shouji"], "appkey": param["appkey"]})
    print(r.status_code)
    assert r.status_code == 200
    result = r.json()
    assert result['status'] == 0
    assert result['msg'] == "ok"
    assert result['result']['shouji'] == "13456755448"
    assert result['result']['province'] == "浙江"
    assert result['result']["company"] == "中国移动"
    assert result['result']["cardtype"] is None
    assert result['result']["areacode"] == "0571"


@pytest.mark.parametrize("mobile, appkey", get_data["mobile_belong_post"])
def test_mobile_post(mobile, appkey):
    params = {
        "shouji": mobile,
        "appkey": appkey
    }
    r = requests.post('https://api.binstd.com/shouji/query', params=params)
    assert r.status_code == 200
    result = r.json()
    assert result['status'] == 0
    assert result['msg'] == "ok"
    assert result['result']["shouji"] == "13456755448"
    assert result['result']["province"] == "浙江"
    assert result['result']["city"] == "杭州"
    assert result['result']["company"] == "中国移动"
    assert result['result']["cardtype"] is None
    assert result['result']["areacode"] == "0571"


@pytest.mark.parametrize("mobile, appkey", get_data["mobile_belong_get"])
def test_mobile_get(mobile, appkey):
    print("测试手机号归属地get请求")
    r = requests.get(url + '/shouji/query',
                     params={"shouji": mobile, "appkey": appkey})
    print(r.status_code)
    assert r.status_code == 200
    result = r.json()
    assert result['status'] == 0
    assert result['msg'] == "ok"
    assert result['result']['shouji'] == "13456755448"
    assert result['result']['province'] == "浙江"
    assert result['result']["company"] == "中国移动"
    assert result['result']["cardtype"] is None
    assert result['result']["areacode"] == "0571"


if __name__ == '__main__':
    pytest.main()
