import json
import urllib.parse

try:
    from robot.libraries.BuiltIn import BuiltIn
    from robot.libraries.BuiltIn import _Misc
    import robot.api.logger as logger
    from robot.api.deco import keyword
    ROBOT = False
except Exception:
    ROBOT = False

@keyword("Capability")
def caps():
    # create a sample json
  a = {
      'browserName': 'Chrome',
      'browserVersion': '91.0',
      'LT:Options': {
        'platform': 'Windows 10',
        'build': 'browser-library tests',
        'name': 'browser-library',
        'user': 'deekshasalugu',
        'accessKey': 'tFU6g0crbGJ85WKCGu4WVS6rrPlX9wQtc5SoJxmk40oiSVcAcU'
      }
    }

  # Convert JSON to String
  y = json.dumps(a)
  print("Encoded" + urllib.parse.quote(y))
  return urllib.parse.quote(y)