from libcloud.dns.types import Provider
from libcloud.dns.providers import get_driver

from credentials import providers as credentials_providers

cls = get_driver(Provider.CLOUDFLARE)
driver = cls(credentials_providers.CF_USERNAME, credentials_providers.CF_APIKEY)

def list_records():
    print(driver.list_zones())
    for zone in driver.list_zones():
        print(driver.list_records(zone))

