
import allure
import pytest

from pages.app import BaseTest
#
# @pytest.fixture(scope="session")
# def start():
#     app = BaseTest()
#     main = app.start()
#     # return main
#     yield main
#     app.quit()

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        # 添加allure报告截图
        with allure.step('添加失败截图...'):
            allure.attach(BaseTest().start().driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)



