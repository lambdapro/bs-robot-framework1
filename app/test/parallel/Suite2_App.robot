*** Settings ***
Library    AppiumLibrary
Library    Process

*** Variables ***
${USERNAME}    %{LT_USERNAME}   #Can specify lambdatest Username directly instead of Environment variable.
${ACCESS_KEY}    %{LT_ACCESS_KEY}    #Can specify lambdatest Accesskey directly instead of Environment variable.
${REMOTE_URL}    https://${USERNAME}:${ACCESS_KEY}@beta-hub.lambdatest.com/wd/hub

*** Test Cases ***
Appium Test on lambdatest
    # id=org.wikipedia.alpha:id/search_container
   Open Application    ${REMOTE_URL}    app=lt://APP10020521642426864932379   name=parallel_test    build=RobotFramework    platformName=Android    platformVersion=10   deviceName=Galaxy S9  isRealMobile=true
	# id=org.wikipedia.alpha:id/search_container
	Click Element    id=org.wikipedia.alpha:id/search_container
	# id=org.wikipedia.alpha:id/search_src_text
	Click Element    id=org.wikipedia.alpha:id/search_src_text
	Input Text    id=org.wikipedia.alpha:id/search_src_text    lambdatest
	# xpath=/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.view.ViewGroup/android.support.v4.view.ViewPager/android.view.ViewGroup/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.LinearLayout
	Click Element    xpath=/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.view.ViewGroup/android.support.v4.view.ViewPager/android.view.ViewGroup/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.LinearLayout
	Close Application

