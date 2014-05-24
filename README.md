# poya

Tells you when the next poya day is.
A live version is available at http://www.nextpoyawhen.com

## Poya?

Poya occurs every full moon day. It's a public holiday in Sri Lanka, so everyone here loves when it's Poya.

## API

**IMPORTANT:** The base URL for all API requests should be `http://nextpoyawhen.appspot.com/` (and NOT `http://www.nextpoyawhen.com/`)

### Next poya

Returns the next poya

Endpoint: `/api/next`

Return format example: 

    {"date": "2014-06-12", "weekday": "Thursday", "days": 19, "month": "June"}


### All poya days of the year

Returns all the poya days of the current year

Endpoint: `/api/all`

Return format example: 

    [{"date": "2014-01-15", "weekday": "Wednesday", "days": -129, "month": "January"}, {"date": "2014-02-14", "weekday": "Friday", "days": -99, "month": "February"}, {"date": "2014-03-16", "weekday": "Sunday", "days": -69, "month": "March"}, {"date": "2014-04-14", "weekday": "Monday", "days": -40, "month": "April"}, {"date": "2014-05-14", "weekday": "Wednesday", "days": -10, "month": "May"}, {"date": "2014-06-12", "weekday": "Thursday", "days": 19, "month": "June"}, {"date": "2014-07-12", "weekday": "Saturday", "days": 49, "month": "July"}, {"date": "2014-08-10", "weekday": "Sunday", "days": 78, "month": "August"}, {"date": "2014-09-08", "weekday": "Monday", "days": 107, "month": "September"}, {"date": "2014-10-08", "weekday": "Wednesday", "days": 137, "month": "October"}, {"date": "2014-11-06", "weekday": "Thursday", "days": 166, "month": "November"}, {"date": "2014-12-06", "weekday": "Saturday", "days": 196, "month": "December"}]

