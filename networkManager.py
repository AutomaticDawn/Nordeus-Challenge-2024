import requests

class NetworkManager:
    def __init__(self):
        pass

    def get_new_map_str(self):
        x = requests.get("https://jobfair.nordeus.com/jf24-fullstack-challenge/test")
        s = str(x.content).replace('b', '').replace('\'', '')
        #print(s)
        return s