import redis
import json

r = redis.Redis(host='localhost', port=6379, db=0)

async def publish(ws_id, data):
    r.publish(ws_id, json.dumps(data))