import requests
import json

BOTACCOUNT_ID="zq96693yt7g5umy9d1sg3jfjxo"
BASEURL="http://192.168.2.110:8082/mattermost"
TAGET_CHANNEL="off-topic"
HEADERS = {
    'Authorization': 'Bearer ' + BOTACCOUNT_ID
}

ANNOUNCE_MESSEGE = {
    #"channel_id": item, 
    "message":"## :loudspeaker: This is the announcement from the MM Administrator", 
    "props":{
        "attachments": [{
            "text": "## broadcast message target channels"
        }]
    }
}

def search(arg, cond, res):
    temp = []
    if cond(arg):
        if arg.get('name') == TAGET_CHANNEL :
            res.append(arg.get('id'))
    if isinstance(arg, list):
        for item in arg:
            temp += search(item, cond, res)
    elif isinstance(arg, dict):
        for value in arg.values():
            temp += search(value, cond, res)
    return res

def has_star_key(arg):
    if isinstance(arg, dict):
        return 'name' in arg

def get_star(arg):
    res = []
    return search(arg, has_star_key, res)

def getchannels():
    r = requests.get(BASEURL+'/api/v4/channels', headers=HEADERS)
    
    return r.json()

def broadcast (arg):
    for item in arg:
        channel_id = {
            "channel_id": item             
        }
        ANNOUNCE_MESSEGE.update(channel_id)
        r = requests.post(BASEURL+'/api/v4/posts', headers=HEADERS, data=json.dumps(ANNOUNCE_MESSEGE))
    
    return r.json()
    
if __name__ == "__main__":
    broadcast(get_star(getchannels()))
