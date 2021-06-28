import webbrowser
# from selenium import webdriver

# browser = webdriver.Firefox()
def authenticate():
    webbrowser.open("http://localhost:5000/login")#,new=1)
    # browser.get('http://localhost:5000/login')
    while True:
        with open("authenticate.txt") as file:
            if file.read()=="1":
                break
            else:
                return False
    return True

# x=authenticate()
#
# while True:
#     with open("authenticate.txt") as file:
#         if file.read() == "1":
#             print("logged in successfully")
#             # window_name = browser.window_handles[0]
#             # print(browser.window_handles,'*******', window_name)
#             # browser.switch_to.window(window_name)
#             # browser.close()
#             break
#         else:
#             pass
# print(dir(webbrowser._browsers['firefox'][1]))