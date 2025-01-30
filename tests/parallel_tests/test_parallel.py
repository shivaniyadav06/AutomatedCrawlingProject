import pytest
from selenium.webdriver import Remote
import config

@pytest.fixture(scope="class")
def grid_driver_init(request):
    grid_url = "http://localhost:4444/wd/hub"
    capabilities = {
        "browserName": "chrome"
    }
    driver = Remote(command_executor=grid_url, desired_capabilities=capabilities)
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.usefixtures("grid_driver_init")
class TestParallelGrid:
    def test_parallel_1(self):
        self.driver.get(config.BASE_URL)
        assert "Amazon" in self.driver.title

    def test_parallel_2(self):
        self.driver.get(config.BASE_URL)
        assert "Amazon" in self.driver.title
