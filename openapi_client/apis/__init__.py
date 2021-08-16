
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.analytics_api import AnalyticsApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from openapi_client.api.analytics_api import AnalyticsApi
from openapi_client.api.applications_api import ApplicationsApi
from openapi_client.api.auth_api import AuthApi
from openapi_client.api.boxes_api import BoxesApi
from openapi_client.api.buildings_api import BuildingsApi
from openapi_client.api.configurations_api import ConfigurationsApi
from openapi_client.api.contacts_api import ContactsApi
from openapi_client.api.devices_api import DevicesApi
from openapi_client.api.fieldtest_api import FieldtestApi
from openapi_client.api.fieldtests_api import FieldtestsApi
from openapi_client.api.meters_api import MetersApi
from openapi_client.api.users_api import UsersApi
