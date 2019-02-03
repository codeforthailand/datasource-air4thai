from datetime import datetime
import json
import pandas as pd
import urllib.request
import numpy as np

_API_TEMPLATE = 'http://air4thai.pcd.go.th/webV2/history/api/data.php?stationID={station_ids}' + \
                '&param={measurements}&type=hr&sdate={sdate}&edate={edate}'+ \
                '&stime=00&etime=24'

_STATIC_COLS = ['stationID', 'DATETIMEDATA']


class Air4Thai(object):
    @staticmethod
    def fetch(stations, measurements, sdate='2019-01-01', edate=datetime.now().strftime('%Y-%m-%d'), verbose=False):
        url = _API_TEMPLATE.format(
            station_ids=','.join(stations),
            measurements=','.join(measurements),
            sdate=sdate,
            edate=edate
        )

        if verbose:
            print('Fetching data from %s' % url)

        with urllib.request.urlopen(url) as data:
            data = json.loads(data.read().decode())

            records = []
            for s in data['stations']:
                for r in s['data']:
                    records.append(dict(stationID=s['stationID'], **r))

            cols = _STATIC_COLS + measurements
            df = pd.DataFrame(records)[cols].sort_values(_STATIC_COLS)
            df['DATETIMEDATA'] = pd.to_datetime(df['DATETIMEDATA'], format='%Y-%m-%d %H:%M:%S')

        df.replace('-', np.NaN, inplace=True)

        return df