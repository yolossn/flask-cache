from locust import HttpUser, task, constant
import names
import json
import random

class cacheService(HttpUser):

    wait_time = constant(1)
    ids = []

    @task
    def create(self):
        payload = {"username":names.get_full_name()}
        headers = {'content-type': 'application/json'}
        resp = self.client.post("/cache/new", data=json.dumps(payload),headers=headers)
        if resp.status_code == 200:
            out = resp.json()
            cache_id = out["_id"]
            self.ids.append(cache_id)
        
    @task
    def get(self):
        if len(self.ids) == 0:
            self.create()
        else:
            rid = random.choice(self.ids)
            self.client.get(f"/cache/{rid}")

        