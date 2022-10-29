import requests
import json 

BASE_URL = "https://api.github.com/search/repositories"

class GithubCrawler:
    def __init__(self):
        self.base_url = BASE_URL

    def crawl(self, query):
        data = []
        try:
            rq = self.base_url+ "?" + "q=" + query 
            response = requests.get(rq).json()
            print(rq)
            if len(response) == 0:
                print("No data match with this query")
            else:
                items = response["items"]
                for i in range(len(items)):
                    tmp = {}
                    tmp["repo_full_name"] = items[i]["full_name"]
                    tmp["url"] = items[i]["html_url"]
                    tmp["owner"] = items[i]["owner"]["login"]
                    tmp["description"] = items[i]["description"]
                    tmp["language"] = items[i]["language"]
                    data.append(tmp)
            return data
        except:
            print("Error when make request to Github API")



        
