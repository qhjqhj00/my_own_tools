try:
    from duckduckgo_search import DDGS
except ImportError:
    print("duckduckgo_search is not installed, please install it using 'pip install duckduckgo-search'")
from my_own_tools import load_pickle, save_pickle
import requests
import re
from typing import Optional

class DuckDuckGoSearchEngine:
    def __init__(self, cache_file: str=""):
        self._cache_file = cache_file
        self._cache = None
        if self._cache_file:
            if os.path.exists(self._cache_file):
                self._cache = load_pickle(self._cache_file)
            else:
                self._cache = {}
        self._ddgs = DDGS()

    def search(self, query):
        require_search = True
        result_list = []
        if self._cache:
            if query in self._cache:
                # print("This query has been cached, so we can load results directly...")
                result_list = self._cache[query]
                require_search = False
        if require_search:
            response = self._ddgs.text(query, max_results=10)
            for item in response:
                title = item.get("title")
                link = item.get("href")
                snippet = item.get("body")
                
                result_list.append({
                    "title": title,
                    "snippet": snippet,
                    "url": link
                })
            
            if self._cache_file:
                self._cache[query] = result_list
                save_pickle(self._cache, self._cache_file)

        #json list
        return result_list

def extract_text_from_url(url, use_jina=True, jina_api_key=None, snippet: Optional[str] = None):
    if use_jina:
        jina_headers = {
            'Authorization': f'Bearer {jina_api_key}',
            'X-Return-Format': 'markdown',
            # 'X-With-Links-Summary': 'true'
        }
        response = requests.get(f'https://r.jina.ai/{url}', headers=jina_headers).text
        pattern = r"\(https?:.*?\)|\[https?:.*?\]"
        text = re.sub(pattern, "", response).replace('---','-').replace('===','=').replace('   ',' ').replace('   ',' ')
        return text
    else:
        raise NotImplementedError("Not implemented yet")

