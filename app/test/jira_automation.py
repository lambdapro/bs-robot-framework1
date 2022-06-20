import urllib.request as urllib2
import urllib.parse
import sys
import json
import base64
import os
import datetime
import config

JIRA_URL = ""  # enter url name here

JIRA_USERNAME = ""  # enter user name here
JIRA_PASSWORD = ""  # For Jira Cloud use a token generated here: https://id.atlassian.com/manage/api-tokens

JIRA_PROJECT_KEY = "DEMO"  # Your project key
JIRA_ISSUE_TYPE = "Bug"

ROBOT_LISTENER_API_VERSION = 2


def end_test(name, attrs):
    if attrs['status'] == 'FAIL':
        print('Test "%s" failed: %s' % (name, attrs['message']))
        capability = json.loads(urllib.parse.unquote(config.caps()))
        print(capability['LT:Options']['name'])
        input('Press enter to continue.')

        def jira_rest_call(data):
            # Set the root JIRA URL, and encode the username and password
            url = JIRA_URL + '/rest/api/2/issue/'
            combined = JIRA_USERNAME + ':' + JIRA_PASSWORD
            base64string = base64.b64encode(bytes(combined, 'utf-8'))
            print(base64string)
            print(data)
            # Build the request
            restreq = urllib2.Request(url)
            restreq.add_header('Content-Type', 'application/json')
            restreq.add_header("Authorization", "Basic " + base64string.decode());

            # Send the request and grab JSON response
            response = urllib2.urlopen(restreq, data)

            # Load into a JSON object and return that to the calling function
            return json.loads(response.read())

        def generate_summary():
            #return "Summary - " + '{date:%Y-%m-%d %H:%M}'.format(date=datetime.datetime.now())
            return capability['LT:Options']['name'];

        def generate_description(data):
            data = data.replace("\n", "").replace("\'", "")
            return data

        def generate_issue_data(summary, description):
            # Build the JSON to post to JIRA
            json_data = '''  { "fields":{ "project":{ "key":"%s" }, "summary": "%s", "issuetype":{ "name":"%s" }, "description": "%s" } } ''' % (JIRA_PROJECT_KEY, summary, JIRA_ISSUE_TYPE, description)
            return json_data.encode()

        json_response = jira_rest_call(
            generate_issue_data(generate_summary(), generate_description(attrs['message'])))
        issue_key = json_response['key']
        print("Created issue ", issue_key)
