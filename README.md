# Package for Air4Thai's API

```
DISCLAIMER: This is an unofficial package. It's just a wrapper for the actual API.
```

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

Please visit DATADICT.md for available values of stations and measurements

## Analysis Examples
Currently, there is a tutorial on how to use the package to retrive Air4Thai's historical data and build a forecasting model for PM2.5.
Please visit `./examples/tutorial.ipynb'


## Contributions
Any feedback, suggestions, or pull-requests are more than welcome.

