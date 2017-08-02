from urllib.parse import urlparse


#Get domain name (example.com)

def get_domain_name(url):
    try:
        return get_sub_domain_name(url)

       # results=get_sub_domain_name(url).splite('.')
        #return results[-2] + '.' + results[-1]
    except:
        return ''



# Get sub domain name (name.example.com)

def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''