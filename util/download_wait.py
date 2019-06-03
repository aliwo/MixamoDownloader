from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


def every_downloads_chrome(driver):
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') # MAC 에서는 Keys.COMMAND

    if not driver.current_url.startswith("chrome://downloads"):
        driver.get("chrome://downloads/")
    return driver.execute_script("""
        var items = downloads.Manager.get().items_;
        if (items.every(e => e.state === "COMPLETE"))
            return items.map(e => e.file_url);
        """)


def wait_download(driver):
    try:
        paths = WebDriverWait(driver, 240, 1).until(every_downloads_chrome)
    except:
        paths = []
    finally:
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
        return paths

#
# # waits for all the files to be completed and returns the paths
# print(paths)
