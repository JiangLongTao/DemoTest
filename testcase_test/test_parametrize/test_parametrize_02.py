import pytest


# 数组的形式
# @pytest.mark.parametrize("name, word", [["安其拉", "火烧皮皮咯"], ["黄忠", "周日被我射熄火了"], ["鲁班", "上上下下左左右右"]])
# def test_parametrize_02(name, word):
#     print(f"{name}的台词是{word}")

# 元组的形式
# @pytest.mark.parametrize("name, word", [("安其拉", "火烧皮皮咯"), ("黄忠", "周日被我射熄火了"), ("鲁班", "上上下下左左右右")])
# def test_parametrize_02(name, word):
#     print(f"{name}的台词是{word}")

# 错误用法
# @pytest.mark.parametrize("name, word", ["安其拉", "火烧皮皮咯"])
# def test_parametrize_02(name, word):
#     print(f"{name}的台词是{word}")

# 错误用法修正
# @pytest.mark.parametrize("name, word", [["安其拉", "火烧皮皮咯"]])
# def test_parametrize_02(name, word):
#     print(f"{name}的台词是{word}")

# 参数值为字典
@pytest.mark.parametrize("hero", [{"name": "安琪拉", "word": "火焰是我最喜欢的玩具"}, {"name": "黄忠"}, {"name": "小乔"}])
def test_parametrize_01(hero):
    print(hero["name"])
    print(hero["word"])
