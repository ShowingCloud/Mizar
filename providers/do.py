from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

from credentials import providers as credentials_providers

cls = get_driver(Provider.DIGITAL_OCEAN)
driver = cls(credentials_providers.DO_ACCESSKEY, api_version = "v2")

def list_nodes():
    nodes = driver.list_nodes()
    print(nodes)

