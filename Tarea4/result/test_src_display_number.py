# Test cases automatically generated by Pynguin (https://github.com/se2p/pynguin).
# Please check them before you use them.
import pytest
import src.display_number as module_0


def test_case_0():
    bool_0 = True
    number_display_0 = module_0.NumberDisplay(bool_0, bool_0)
    var_0 = number_display_0.str()
    assert var_0 == "0True"


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    number_display_0 = module_0.NumberDisplay(bool_0, bool_0)
    dict_0 = {
        number_display_0: number_display_0,
        number_display_0: number_display_0,
        number_display_0: number_display_0,
    }
    number_display_1 = module_0.NumberDisplay(dict_0, number_display_0)
    var_0 = number_display_1.reset()
    assert number_display_1.value == 0
    number_display_1.increase()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    number_display_0 = module_0.NumberDisplay(bool_0, bool_0)
    var_0 = number_display_0.invariant()
    assert var_0 is False
    var_0.increase()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b""
    number_display_0 = module_0.NumberDisplay(bytes_0, bytes_0)
    var_0 = number_display_0.clone()
    var_0.str()


@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = 381.28695
    number_display_0 = module_0.NumberDisplay(float_0, float_0)
    var_0 = number_display_0.str()
    assert var_0 == "381.28695"
    var_0.reset()
