import pytest
import random


@pytest.fixture(params=[1,2,3])
def before(request):
    return request.param


class Test1:
    # @pytest.mark.run(order=2)
    # def test_1(self):
    #     print("通过")
    #     assert True

    # @pytest.mark.run(order=1)
    # def test_2(self):
    #     num = random.randint(1, 2)
    #     if num % 2:
    #         print("成功")
    #         assert True
    #     else:
    #         print("失败")
    #         assert False

    # @pytest.mark.skipif(True, reason="跳过该函数")
    # def test_3(self):
    #     print("skip")

    # @pytest.mark.xfail(False, reason="标注为预期失败")
    # def test_4(self):
    #     assert False
    # @pytest.mark.parametrize("keys,key", ([0, 1],[2, 3]))
    # def test_5(self,keys,key):
    #     print(keys,key)
    # @pytest.fixture()
    # def before(self):
    #     print("b----")

    def test_a(self,before):  # ⚠️ test_a方法传入了被fixture标识的函数，已变量的形式
        print(before)
        assert 1

    # def test_b(self):  # ⚠️ test_a方法传入了被fixture标识的函数，已变量的形式
    #     print("------->test_b")
    #     assert 1
#     pytest.main(["-s","test_1.py"])
     def test_c(self,before):  # ⚠️ test_c方法传入了被fixture标识的函数，已变量的形式
        print(before)
        assert 1


    def test_hh(self, before):  # ⚠️ test_c方法传入了被fixture标识的函数，已变量的形式

        print(before)
        assert 1
