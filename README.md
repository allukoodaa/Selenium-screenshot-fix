# Selenium-screenshot-fix

Under settings in robot file:
Library    ${your path}/FullPageScreenshot.py
Library    SeleniumLibrary    run_on_failure=Capture Full Page Screenshot

In tests/keywords:
Test 1
    Open Browser    ${url}    headlesschrome
    Capture Full Page Screenshot    filename.png
