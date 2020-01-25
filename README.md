# ynab

Provide integration with YNAB's API. See https://api.youneedabudget.com

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project.

Forked from [deanmcgregor/ynab-python](https://github.com/deanmcgregor/ynab-python) due to lack of maintenance.

Status: Github Actions takes care of opening PRs for new OpenAPI versions/YNAB API updates. I try to check weekly on new PRs/issues, but no guarantees. If you would like to more strongly maintain the project, please feel free to reach out.

## Requirements

Python 3.5+ (We try to respect the [Python EOL schedule](https://devguide.python.org/#status-of-python-branches))

## Installation & Usage
### pip install

```sh
pip install git+https://github.com/davidhao3300/ynab-python.git
```

Then import the package:
```python
import ynab 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import ynab
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import ynab
from ynab.rest import ApiException
from pprint import pprint

configuration = ynab.Configuration()
# Configure API key authorization: bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.youneedabudget.com/v1
configuration.host = "https://api.youneedabudget.com/v1"
# Create an instance of the API class
api_instance = ynab.AccountsApi(ynab.ApiClient(configuration))
budget_id = 'budget_id_example' # str | The id of the budget (\"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget)
account_id = 'account_id_example' # str | The id of the account

try:
    # Single account
    api_response = api_instance.get_account_by_id(budget_id, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_account_by_id: %s\n" % e)

```

## Documentation for API Endpoints and Models

All URIs are relative to *https://api.youneedabudget.com/v1*

See [docs folder](docs/) for auto-generated documentation.

## Author

David Hao
