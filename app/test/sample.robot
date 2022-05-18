*** Settings ***
Library   Browser
Library   config.py
Library    REST     https://api.lambdatest.com

*** Test Cases ***
Example Test
    ${value}    Capability
    Log         ${value}
    Connect To Browser    wss://cdp.lambdatest.com/playwright?capabilities=${value}    chromium
    New Page    https://playwright.dev
    Get Text    h1    ==    Playwright enables reliable end-to-end testing for modern web apps.

    ${user}=    Set Variable    deekshasalugu
    ${pass}=    Set Variable    tFU6g0crbGJ85WKCGu4WVS6rrPlX9wQtc5SoJxmk40oiSVcAcU

    # this kyword is in the Strings library
    ${userpass}=    Convert To Bytes    ${user}:${pass}   # this is the combined string will be base64 encode
    ${userpass}=    Evaluate    base64.b64encode($userpass)    base64

    # add the new Authorization header
    &{headers}=     Create Dictionary  Authorization    Basic ${userpass}

    ${response}=    GET       /automation/api/v1/sessions/OW75K-L69JR-SKPFO-NIUUT    headers=${headers}
    Output    response  body
