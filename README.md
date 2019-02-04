# Package for Air4Thai's API

```
DISCLAIMER: This is an unofficial package. It's just a wrapper for the actual API.
```
This Python package provides a convenient way to retrieve data Air4Thai's [history data API][api].

## Installation
```
pip install code4th-datasource-air4thai
```

## Usage
```
from code4th.datasources import Air4Thai

df = Air4Thai.fetch(
    stations=['03t', '05t'],
    measurements=['O3', 'CO', 'NO2', 'PM25'],
    sdate='2019-01-01',
    edate='2019-02-03',
    verbose=True
)
```

Please visit `DATA-DICTIONARY.md` for available values of stations and measurements

## Tutorial
Currently, there is a tutorial on how to use the package to retrieve Air4Thai's historical data. The tutorial also includes simple time series analysis that one can do with the data, such as seasonal decomposing or forecasting models.
Feel free to check it out at `./examples/tutorial.ipynb`.

<div align="center">
<img src="https://i.imgur.com/4unRLva.png"/>
</div>

## Relevant Projects
- https://github.com/gain9999/PM2.5

## Contributions
Any feedback, suggestions, or pull-requests are more than welcome.

[api]: http://air4thai.pcd.go.th/webV2/history/
