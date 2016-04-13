# Convert Timestamps

Convert a table of timestamps into a different timezone.  A timezone unifies time across a region.

Thanks to [Gustavo Niemeyer](https://github.com/niemeyer), [Tomi Pieviläinen](https://code.launchpad.net/~tpievila), [Yaron de Leeuw](https://github.com/jarondl), [Paul Ganssle](https://github.com/pganssle) for [dateutil](https://pypi.python.org/pypi/python-dateutil).

Thanks to [Stuart Bishop](https://launchpad.net/~stub) for [pytz](https://pypi.python.org/pypi/pytz).

First, provide the table and column of timestamps.

{timestamp_table_path}
{timestamp_column}

Then, indicate the source and target timezones by location.

{source_address}
{target_address}

Finally, specify the timestamp format in [strftime syntax](https://docs.python.org/2/library/time.html#time.strftime).

{target_strftime}