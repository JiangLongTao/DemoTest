import pytest


# @pytest.mark.parametrize(key, values)
# @pytest.mark.parametrize("key", ["value"])
# def test_parametrize_01(key):
#     print("我是" + key)

# 单次循环
# @pytest.mark.parametrize("name", ["value"])
# def test_parametrize_01(key):
#     assert name == "value"

# 一个参数多个值，测试用例会把每个值赋给参数，进行测试用例执行
# 几个值，测试用例执行几次
@pytest.mark.parametrize("hero_name", ["安其拉", "黄忠", "小乔"])
def test_parametrize_01(hero_name):
    assert hero_name == "安其拉"
