# TestRail API binding for Python 3.x (API v2, available since TestRail 3.0)
# Copyright Gurock Software GmbH. See license.md for details.
import urllib2, json, base64

def createClient(user, key):
    client = APIClient()
    client.user = user
    client.key = key
    return client

class APIClient():
    def __init__(self):
        baseUrl = 'https://mutualmobile.testrail.com'
        self.user = ''
        self.key = ''
        if not baseUrl.endswith('/'):
            baseUrl += '/'
        self.url = baseUrl + 'index.php?/api/v2/'

    def updateTestrail(self, user, key, caseId, runId, resultFlag, msg=""):
        client = createClient(user, key)

        """
        :param user: email address
        :param key: API key
        :param case_id: test case id number
        :param run_id: test run id number
        :result flag: test result
        """
        # status_id is 1 for Passed, 2 For Blocked, 4 for Retest and 5 for Failed
        statusId = 1 if resultFlag is True else 5

        if runId is not None:
                client.sendPost(
                    'add_result_for_case/%s/%s' % (runId, caseId),
                    {'status_id': statusId, 'comment': msg})
        else:
            print("No run id - cannot update test result")

    def sendPost(self, uri, data):
        return self.sendRequest('POST', uri, data)

    def sendRequest(self, method, uri, data):
        url = self.url + uri
        request = urllib2.Request(url)
        if method == 'POST':
            request.add_data(json.dumps(data))
        auth = base64.b64encode('%s:%s' % (self.user, self.key))
        request.add_header('Authorization', 'Basic %s' % auth)
        request.add_header('Content-Type', 'application/json')

        e = None
        try:
            response = urllib2.urlopen(request).read()
        except urllib2.HTTPError as e:
            response = e.read()

        if response:
            result = json.loads(response)
        else:
            result = {}

        if e != None:
            if result and 'error' in result:
                error = '"' + result['error'] + '"'
            else:
                error = 'No additional error message received'
            raise APIError('TestRail API returned HTTP %s (%s)' %
                           (e.code, error))
        return result

class APIError(Exception):
    pass
