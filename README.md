# LT-robot-framework

## Setup
* Clone the repo
* Install dependencies  `pip install robotframework`  &&  `pip install --upgrade robotframework-seleniumlibrary`
* `pip install robotframework-pabot` -> This is for parallelization 
* For Appium, `pip install robotframework-appiumlibrary` .For more information refer https://github.com/serhatbolsu/robotframework-appiumlibrary
* **Note: This is w.r.t Python3**

## Set lambdatest Credentials 
* You can export the environment variables for the Username and Access Key of your lambdatest account. 

  ```
  export LT_USERNAME=<lambdatest-username> &&
  export LT_ACCESS_KEY=<lambdatest-access-key>
  ```

## Running tests

### App Automate

* Navigate to `cd app/test`
* Upload app refer https://www.lambdatest.com/support/docs/running-appium-tests-with-python/
* Sample app: https://github.com/mayank2193/robot_LT/blob/main/app/test/WikipediaSample.apk
* Replace "app_url" from script with the response recieved while uploading your test app to Lambdatest . Eg: lt://APP10020521642428466273345
- Android
```
Open Application    ${REMOTE_URL}    app=app_url  name=parallel_test    build=RobotFramework    platformName=Android    platformVersion=10   deviceName=Google Pixel 3 XL  isRealMobile=true
```

* To run single test, run `robot Appium_android.robot` OR  run `robot Appium_ios.robot` 
* Parallel Execution: 
* To run parallel tests, navigate to 'parallel' folder, run `cd parallel`
  1. Test Suite level
    - Run `pabot --processes <count_of_parallels> *.robot`
    - Alternate method: `pabot --processes <count_of_parallels> <name_of_suites_to_run>` Eg: `pabot --processes 2 Suite1_App.robot       Suite2_App.robot`
  2. Test case level
    - Run `pabot --testlevelsplit <file_name>` Eg:  `pabot --testlevelsplit Suite1.robot`
  3. Run Test cases and Test suites together in parallel
    - Run `pabot --testlevelsplit --processes <count_of_parallels> *.robot`
    - **Note: If the process count exceeds the parallel thread limit, it will automatically get queued. No changes required in the scripts.**
    

  

