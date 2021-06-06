
import json
import requests

username = ""  # T-Mobile telefoonnummer
password = ""  # T-Mobile wachtwoord

print('Start T-Mobile Unlimited 2GB aanvuller')

# Get AuthorizationCode
url = "https://capi.t-mobile.nl/login?response_type=code"

payload = "{\r\n    \"Username\": \"" + username + "\",\r\n    \"Password\": \"" + password + "\", \r\n    \"ClientId\": \"9havvat6hm0b962i\",\r\n    \"Scope\": \"usage+readfinancial+readsubscription+readpersonal+readloyalty+changesubscription+weblogin\"\r\n}"
headers = {
    'Authorization': 'Basic OWhhdnZhdDZobTBiOTYyaTo=',
    'Content-Type': 'application/vnd.capi.tmobile.nl.login.v1+json; charset=utf-8',
    'User-Agent': 'T-Mobile 5.3.28 (Android 10; 10)',
    'Cookie': 'afck-httpsetting-backendpool-tmobile-capi-t-mobile-nl-main-https=8e74d86ac726a62c145252273e1bcb1b; afck-httpsetting-backendpool-tmobile-capi-t-mobile-nl-main-httpsCORS=8e74d86ac726a62c145252273e1bcb1b'
}

response = requests.request("POST", url, headers=headers, data=payload)
AuthorizationCode = response.headers['AuthorizationCode']
print('Authorization code is ' + AuthorizationCode)

# Get AccesToken
url = "https://capi.t-mobile.nl/createtoken"

payload = json.dumps({
    "AuthorizationCode": AuthorizationCode
})
headers = {
    'Authorization': 'Basic OWhhdnZhdDZobTBiOTYyaTo=',
    'User-Agent': 'T-Mobile 5.3.28 (Android 10; 10)',
    'Content-Type': 'application/json',
    'Cookie': 'afck-httpsetting-backendpool-tmobile-capi-t-mobile-nl-main-https=8e74d86ac726a62c145252273e1bcb1b; afck-httpsetting-backendpool-tmobile-capi-t-mobile-nl-main-httpsCORS=8e74d86ac726a62c145252273e1bcb1b'
}

response = requests.request("POST", url, headers=headers, data=payload)
AccessToken = response.headers['AccessToken']
print('Access token is ' + AccessToken)

# Get subscription API url
url = "https://capi.t-mobile.nl/account/current?resourcelabel=Customer&resourcelabel=Connection&resourcelabel=Subscription&resourcelabel=PushNotificationRegistrationStatus&resourcelabel=PushNotificationRegistration"

payload = ""
headers = {
    'Authorization': 'Bearer ' + AccessToken,
    'Accept': 'application/json',
    'User-Agent': 'T-Mobile 5.3.28 (Android 10; 10)',
    'Cookie': 'afck-httpsetting-backendpool-tmobile-capi-t-mobile-nl-main-https=8e74d86ac726a62c145252273e1bcb1b; afck-httpsetting-backendpool-tmobile-capi-t-mobile-nl-main-httpsCORS=8e74d86ac726a62c145252273e1bcb1b'
}

response = requests.request("GET", url, headers=headers, data=payload)
JSONresponse = json.loads(response.text)
SubscriptionAPIUrl = JSONresponse['Resources'][2]['Url']
print('Subscription API URL is ' + SubscriptionAPIUrl)

# Add roaming bundle
url = SubscriptionAPIUrl + "/RoamingBundles"

payload = json.dumps({
    "Bundles": [
        {
            "BuyingCode": "A0DAY01"
        }
    ]
})
headers = {
    'Authorization': 'Bearer ' + AccessToken,
    'Accept': 'application/vnd.capi.tmobile.nl.roamingbundles.V3+json',
    'User-Agent': 'T-Mobile 5.3.28 (Android 10; 10)',
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

if(response.status_code == 500):
    print('Aanvuller nog niet beschikbaar!')
else:
    print('Aanvuller geactiveerd!')
