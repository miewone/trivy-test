from oauthtest import app
import redis
import json
from google.cloud import bigquery
from google.oauth2 import service_account, credentials as cred
import google.auth



rd = redis.Redis(host="superset-redis-master", port=6379, db=0)


if __name__ == "__main__":
    test = rd.get('wongyun')
    sessions = json.loads(test)
    sessions["client_secret"] = "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"
    sessions["client_id"] = "319633121491-5jgh73okm4qvag6ne99md6crd36qaj24.apps.googleusercontent.com"
    
    credentials = cred.Credentials(
            sessions['token'],
            refresh_token=sessions['refresh_token'],
            token_uri=sessions['token_uri'],
            client_id=sessions['client_id'],
            client_secret=sessions['client_secret']
            # access_token= sessions['access_token']
        )  
    default_project = "beha-data"
    
    client = bigquery.Client(
        project=default_project,
        credentials=credentials,
        location="asia-northeast3",
        default_query_job_config=None,
    )
    
    QUERY = "select * from `beha-data`.`dq_poc`.NOT_NULL limit 5;"
    query_job = client.query(QUERY) 
    rows = query_job.result()  # Waits for query to finish
    return_qeury = ""
    for row in rows:
        print(row)
    
    print(sessions)
    app.run(host="0.0.0.0")