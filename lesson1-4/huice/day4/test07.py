import requests

# response = requests.get("http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getRegionProvince")
# print response.status_code
# print type(response.text), response.text
#
# params = {"theRegionCode":"3113"}
# response = requests.get("http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString", params)
# print response.status_code
# print response.text

# headers = {'Content-Type': 'application/x-www-form-urlencoded'}
# params = {"theRegionCode":"3113"}
# response = requests.post('http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString', params, headers=headers)
# print response.status_code
# print response.text

# headers = {'Content-Type': 'text/xml', 'SOAPAction': 'http://WebXml.com.cn/getSupportCityString'}
# context_text = '''
# <?xml version="1.0" encoding="utf-8"?>
# <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
#   <soap12:Body>
#     <getSupportCityString xmlns="http://WebXml.com.cn/">
#       <theRegionCode>3113</theRegionCode>
#     </getSupportCityString>
#   </soap12:Body>
# </soap12:Envelope>
# '''
#
# response = requests.post('http://ws.webxml.com.cn/WebServices/WeatherWS.asmx', data=context_text, headers=headers)
# response.encoding = 'utf-8'
# print response.status_code
# print response.text
