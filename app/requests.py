import requests

base_url=None

def configure_request(app):
    global base_url

   
def get_quote():
    get_response = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    return get_response