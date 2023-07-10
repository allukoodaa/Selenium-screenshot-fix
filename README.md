# Custom implementation for capturing full page screenshots with SeleniumLibrary and Robot framework

Embeds screenshot to log.html by default, can be overridden 


Under settings in robot file:

    ***Settings***
    Library    ${your path}/FullPageScreenshot.py
    Library    SeleniumLibrary    run_on_failure=Capture Full Page Screenshot

Or:

    ***Settings***
    Library    ${your path}/FullPageScreenshot.py
    Library    SeleniumLibrary    run_on_failure=Failure Screenshot

    ***Keywords***
    Failure Screenshot
        [Documentation]    Take full page screenshot in case of suite failure
        Capture Full Page Screenshot    failure.png

In tests/keywords:

    Test 1
        Open Browser    ${url}    headlesschrome
        Capture Full Page Screenshot    filename.png
