import pprint
import requests
import json
import sys

class Error(Exception):
    """An Error was encounter"""
    pass

class no_schema_found(Error):
    """Raised when trying to find schema that does not exist"""
    pass

def citeline_connection(citeuser: object, citepass: object, citeauth: object) -> object:

    url = "https://identity.pharmaintelligence.informa.com/connect/token"

    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" \
              "Content-Disposition: form-data; name=\"grant_type\"\r\n\r\npassword\r\n" \
              "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" \
              "Content-Disposition: form-data; name=\"username\"\r\n\r\n" + citeuser +"\r\n" \
              "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" \
              "Content-Disposition: form-data; name=\"password\"\r\n\r\n"+ citepass + "\r\n" \
              "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" \
              "Content-Disposition: form-data; name=\"scope\"\r\n\r\ncustomer-api\r\n" \
              "------WebKitFormBoundary7MA4YWxkTrZu0gW--"

    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'Authorization': "Basic " + citeauth,
        'Cache-Control': "no-cache",
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response)
    return json.loads(response.text)['access_token']

class query_api():

    avail_schema = ["drug", "trial", "investigator", "organization", "drugevent", "drugcatalyst"]
    def make_header(citeconn):
        headers = {
            'Accept': "application/json",
            'Authorization': "Bearer " + citeconn,
            'Cache-Control': "no-cache"
        }
        return headers

    def citeline_get_permissions(citeconn):
        result = []

        for item in query_api.avail_schema:
            url = "https://api.pharmaintelligence.informa.com/v1/feed/" + item + "/schema"

            headers = query_api.make_header(citeconn)

            localResponse = json.loads(requests.request("GET", url, headers=headers).text)
            try:
                result.append([item, "Permission Fail", localResponse['meta']['message']])
            except:
                result.append([item, "Permission OK"])

        return result

    def citeline_schema(s_type, citeconn, has_page=0):

        print(s_type)
        if(s_type not in query_api.avail_schema):
            raise no_schema_found("type not found in schema list")
        if(has_page==0):
            url="https://api.pharmaintelligence.informa.com/v1/feed/"+ s_type +"/schema"
        else:
            url=has_page
        headers = {
            'Accept': "application/json",
            'Authorization': "Bearer " + citeconn,
            'Cache-Control': "no-cache"
        }

        localResponse = json.loads(requests.request("GET",url,headers=headers).text)
        return localResponse


    #helpful tip: has_page is a URL that citeline passes back under ['pagination']['nextPage'], it contains
    #all original query parameters

    def citeline_feed(s_type, citeconn, has_page=0):

        print("Getting "+ s_type + ", this may take a while")
        if(s_type not in query_api.avail_schema):
            raise no_schema_found("type not found in schema list")
        if(has_page==0):
            url="https://api.pharmaintelligence.informa.com/v1/feed/"+ s_type
        else:
            url=has_page
        headers = {
            'Accept': "application/json",
            'Authorization': "Bearer " + citeconn,
            'Cache-Control': "no-cache"
        }
        localResponse = json.loads(requests.request("GET",url,headers=headers).text)
        print(str(sys.getsizeof(str(localResponse))/1000/1000) + " MB")
        return localResponse