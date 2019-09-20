curl https://api.youneedabudget.com/papi/spec-v1-swagger.json > spec-v1-swagger.json
openapi-generator generate -g python -i spec-v1-swagger.json --package-name ynab
