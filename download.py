from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from util.download_wait import wait_download
from util.robust import robust


@robust
def click_po(po):
    po.click()


def download_page(driver):

    download_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#site > div:nth-child(4) > div > div > div.product-preview-holder.col-sm-6 > div > div.editor.row.row-no-gutter > div.editor-sidebar.col-xs-4 > div.sidebar-header > button.btn-block.btn.btn-primary"))
    ) # 페이지 전환 후 다운로드 버튼이 활성화 될 때까지 기다립니다.

    product_overlays = driver.find_elements(By.CSS_SELECTOR, 'div.product-overlay')

    for i, po in enumerate(product_overlays):
        click_po(po)
        driver.execute_script('arguments[0].click();', download_button)

        # 60 프레임, without skin 을 선택합니다.
        select_elements = driver.find_elements(By.CSS_SELECTOR, 'select#formControlsSelect')
        Select(select_elements[1]).select_by_value('false')
        Select(select_elements[2]).select_by_value('60')

        # 팝업에 뜬 Download 버튼을 선택합니다.
        inner_download_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
            "body > div:nth-child(7) > div > div.asset-download-modal.fade.in.modal > div > div > div.modal-footer > div > button.btn.btn-primary"))
        )
        driver.execute_script('arguments[0].click();', inner_download_button)

        # 다운로드가 시작될 때 까지 기다립니다.
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "li.message-display-item.alert.alert-dismissible.alert-info"))
        )

        # if i != 0 and i % 5 == 0: # 매 5번째 다운로드 마다 다운로드 완료를 기다립니다... 가 원래 계획이었으나 다운로드 페이지를 못 불러오네요
        #     pass
            # driver.implicitly_wait(120) # 그래서 그냥 2 분 기다립니다.




def download(driver):

    # download_page(driver)

    for i in range(2, 53):
        driver.get('https://www.mixamo.com/#/?page={}'.format(i))
        driver.implicitly_wait(3)
        download_page(driver)



