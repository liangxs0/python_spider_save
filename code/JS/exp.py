import time
import base64
from typing import List,Any
import requests
import hashlib

index_url = "https://dynamic6.scrape.cuiqingcai.com/api/movie?limit={limit}&offset={offset}&token={token}"
limit = 10
offset = 0

def get_token(args:List[Any]):
    timestamp = str(int(time.time()))
    args.append(timestamp)
    sign = hashlib.sha1(",".join(args).encode("utf-8")).hexdigest()
    token_ = base64.b64encode(",".join([sign, timestamp]).encode("utf-8")).decode("utf-8")
    return token_

args = ["/api/movie"]
token = get_token(args=args)
print(token)
url = index_url.format(limit=limit,offset=offset,token=token)
response = requests.get(url)
print(response.json())