from robot.api.deco import keyword, library
from robot.libraries.BuiltIn import BuiltIn


@library(scope='GLOBAL')
class FullPageScreenshot:
    """Custom implementation to capture full page screenshot with Selenium and Robot framework.

    Usage:
    |   Library     ${your path}/FullPageScreenshot.py
    |   Library     SeleniumLibrary    run_on_failure=Capture Full Page Screenshot

    Works in headless mode only.
    """
    @keyword
    def capture_full_page_screenshot(self, filename='EMBED'):
        # Get library instance from test suite.
        self.selenium_lib = BuiltIn().get_library_instance('SeleniumLibrary')
        driver = self.selenium_lib.driver
        # Save original size.
        original_size = driver.get_window_size()
        # Get total width and height.
        total_width = driver.execute_script('return document.documentElement.scrollWidth')
        total_height = driver.execute_script('return document.documentElement.scrollHeight')
        driver.set_window_size(total_width, total_height)
        # Take screenshot of the whole page.
        self.selenium_lib.capture_page_screenshot(filename)
        # Reset size to original.
        driver.set_window_size(original_size['width'], original_size['height'])
