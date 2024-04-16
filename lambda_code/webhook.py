import json
import urllib3

http = urllib3.PoolManager()

def lambda_handler(event, context):
    raw_event = json.loads(event['body'])

    # Let's do a POST to an external API endpoint with data
    # defining the api-endpoint:
    TICKET_ENDPOINT = "{TICKET_ENDPOINT}"
    BASE_64_FRESHSERVICE_API_TOKEN = '{BASE_64_FRESHSERVICE_API_TOKEN}'
      
    # define headers and data portions
    headers = {"content-type":"application/json",
               "Authorization":'Basic {}'.format(BASE_64_Freshservice_API_TOKEN)}
    data = {'description': raw_event['details'],
            'status': 2,
            'priority': 2,
            "subject": '{} - {} - {}'.format(raw_event["type_string"], raw_event["asset_name"], raw_event["asset_type_string"]),
            "email": "ticket-from-orca@orca.security"
           }
    
    response = http.request('POST',
                        url = TICKET_ENDPOINT,
                        body = json.dumps(data),
                        headers = headers,
                        retries = False)
    
    # extracting response text 
    api_response = response.data
    logger.info('Response from external API: %s', api_response)

    return {
        'statusCode' : str(response.status),
        #'body': json.dumps(event)
        'body': json.dumps(raw_event)
    }
