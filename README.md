# Covid-19 Somaliland API
[![GitHub stars](https://img.shields.io/github/stars/Abdirahiim/covid-19-somaliland-api)](https://github.com/Abdirahiim/covid-19-somaliland-api/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Abdirahiim/covid-19-somaliland-api)](https://github.com/Abdirahiim/covid-19-somaliland-api/network/members)
[![HitCount](http://hits.dwyl.com/Abdirahiim/covid-19-somaliland-api.svg)](http://hits.dwyl.com/Abdirahiim/covid-19-somaliland-api)

Covid-19 Somaliland API is an API made for tracking Coronavirus cases in Somaliland, the data is based on the [official Somaliland Coronavirus website](https://somalilandcoronavirus.com)  and it's updated daily.

## API Reference

All endpoints are located at ``covid-19-somaliland-api.herokuapp.com/`` and are accessible via https. For instance: you can get data per location by using this URL:
[https://covid-19-somaliland-api.herokuapp.com/locations](https://covid-19-somaliland-api.herokuapp.com/locations)

You can open the URL in your browser to further inspect the response. Or you can make this curl call in your terminal to see the prettified response:

```
curl https://covid-19-somaliland-api.herokuapp.com/locations | json_pp
```

### Swagger

You can use the API through [the SwaggerUI](https://covid-19-somaliland-api.herokuapp.com).

## API Endpoints

### Latest Endpoint

Gets the latest national confirmed, recovered and deaths cases.

```http
GET /latest
```

__Sample response__
```json
{
  "latest": [
    "confirmed": 6,
    "deaths": 1,
    "recovered": 2
  ]
}
```

### Locations Endpoint

#### List of all locations

Gets the latest national confirmed, recovered and deaths cases of each location

```http
GET /locations
```

__Sample response__
```json
{
    "locations": [
    {
    "city": "Hargeysa",
    "confirmed": 3,
    "deaths": 0,
    "id": 1,
    "province": "Maroodijeex",
    "recovered": 0
    },
    {
    "city": "Burco",
    "confirmed": 1,
    "deaths": 0,
    "id": 2,
    "province": "Togdheer",
    "recovered": 1
     }
   ]
 }
```

#### Gets location by Id

```http
GET /locations/id/:id
```
__Path Parameters__
| __Path parameter__ | __Required/Optional__ | __Description__                                                                                                                                                          | __Type__ |
| ------------------ | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| id                 | OPTIONAL              | The unique location id for each location. The list of valid location IDs can be found in the locations response: ``/locations`` | Integer  |

#### Example Request
```http
GET /locations/id/2
```

__Sample response__
```json
{
    "locations": [
    {
    "city": "Burco",
    "confirmed": 1,
    "deaths": 0,
    "id": 2,
    "province": "Togdheer",
    "recovered": 1
    }
  ]
 }
```

#### Gets location by province

```http
GET /locations/province/:province
```
__Path Parameters__
| __Path parameter__ | __Required/Optional__ | __Description__                                                                                                                                                          | __Type__ |
| ------------------ | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| province                 | OPTIONAL              | The name of the province in which the location belongs to. The list of the provinces can be found in the locations response: ``/locations`` | String  |

#### Example Request
```http
GET /locations/province/togdheer
```

__Sample response__
```json
{
    "locations": [
    {
    "city": "Burco",
    "confirmed": 1,
    "deaths": 0,
    "id": 2,
    "province": "Togdheer",
    "recovered": 1
    }
  ]
 }
```

#### Gets location by city

```http
GET /locations/city/:city
```
__Path Parameters__
| __Path parameter__ | __Required/Optional__ | __Description__                                                                                                                                                          | __Type__ |
| ------------------ | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| province                 | OPTIONAL              | The name of the city in which the location belongs to. The list of the cities can be found in the locations response: ``/locations`` | String  |

#### Example Request
```http
GET /locations/city/burao
```

__Sample response__
```json
{
    "locations": [
    {
    "city": "Burco",
    "confirmed": 1,
    "deaths": 0,
    "id": 2,
    "province": "Togdheer",
    "recovered": 1
    }
  ]
 }
```