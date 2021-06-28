# from flask import Flask, render_template
#
# app=Flask(__name__)
#
# @app.route("/")
# def home():
#     return render_template('home.html')
#
# # @app.route("/<id>",methods=['GET'])
# # def home(id):
# #     return id
#
# @app.route("/<int:a>/<int:b>",methods=['GET'])
# def get(a,b):
#     x,out=max(a,b),[]
#     for i in range(1,x+1):
#         if a%i==0 and b%i==0:
#             out.append(i)
#
#     return "<h1>"+str(max(out))+"</h1>"
#
# if __name__=="__main__":
#     app.run(debug=True)
#
#
# '''
# 367 people in a room
# probability of a pair with same birth date
# 1/367
#
# lady with 2 kids
# 1 girl
# g g
# g b
# b b
# b g
#
#
#
# '''

# __author__ = 'bdm4'
# import requests, json
# import subprocess
# import sys
# authorize_url = "https://login.microsoftonline.com/db76fb59-a377-4120-bc54-59dead7d39c9/oauth2/authorize?resource=https://k2-dev.merckgroup.com/"
# token_url = "https://login.microsoftonline.com/db76fb59-a377-4120-bc54-59dead7d39c9/oauth2/token"
# #callback url specified when the application was defined
# callback_uri = "https://k2-dev.merckgroup.com/"
# test_api_url = "https://k2-dev.merckgroup.com/Api/Workflow/Preview/workflows?type=Startable"
# #client (application) credentials - located at apim.byu.edu
# client_id = 'bfdeb815-6507-4a4e-b7ce-2c550f70553d'
# client_secret = 'Krc_~Ol1yoL20MgPN9M1u9A9Gie-~~u9n0'
# #step A - simulate a request from a browser on the authorize_url - will return an authorization code after the user is
# authorization_redirect_url = authorize_url + '?response_type=code&client_id=' + client_id + '&redirect_uri=' + callback_uri + '&scope=openid'
# print ("go to the following url on the browser and enter the code from the returned url: ")
# print ("---  " + authorization_redirect_url + "  ---")
# output = requests.get(authorization_redirect_url)
# print(output.cookies)
# authorization_code = input('code: ')
# # step I, J - turn the authorization code into a access token, etc
# data = {'grant_type': 'authorization_code', 'code': authorization_code, 'redirect_uri': callback_uri}
# print ("requesting access token")
# access_token_response = requests.post(token_url, data=data, verify=False, allow_redirects=False, auth=(client_id, client_secret))
# print ("response")
# print (access_token_response.headers)
# print ('body: ' + access_token_response.text)
# # we can now use the access_token as much as we want to access protected resources.
# tokens = json.loads(access_token_response.text)
# access_token = tokens['access_token']
# print ("access token: " + access_token)
# api_call_headers = {'Authorization': 'Bearer ' + access_token}
# api_call_response = requests.get(test_api_url, headers=api_call_headers, verify=False)
# print (api_call_response.text)


__author__ = 'bdm4'

import requests, json

def token_create():
    token_url = "https://login.microsoftonline.com/dbd7ee05-27ee-436c-a97c-9ef70e6794a2/oauth2/token"

    test_api_url = "http://localhost:5000/getAToken"

    #client (application) credentials on apim.byu.edu
    client_id = '1a89daa9-8c59-48e5-bca3-9d3c4f5e5f61'
    client_secret = '9~y3l4x_f0uj6C_G7ZE_8ymsL1X~UT2Xj2'

    #step A, B - single call with client credentials as the basic auth header - will return access_token
    data = {'grant_type': 'client_credentials'}


    access_token_response = requests.post(token_url, data=data, verify=True, allow_redirects=False, auth=(client_id, client_secret))

    # print (access_token_response.headers)
    # print (access_token_response.text)

    tokens = json.loads(access_token_response.text)

    print ("access token: " + tokens['access_token'])

    #step B - with the returned access_token we can make as many calls as we want


    api_call_headers = {'Authorization': 'Bearer ' + tokens['access_token']}
    # api_call_response = requests.get(test_api_url, headers=api_call_headers, verify=False)
    x=requests.post(test_api_url,headers=api_call_headers,verify=False)
    # print (api_call_response.headers)


