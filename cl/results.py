import datetime
import mlbgame


base = datetime.datetime.today()

### Setup Questions ###
numdays = int(raw_input("How many days back to you want to see?  "))

inclusion = str(raw_input("Include today? y/n  "))
if inclusion == 'n':
    date_list = [base - datetime.timedelta(days=x) for x in range(1, numdays)]
else:
    date_list = [base - datetime.timedelta(days=x) for x in range(0, numdays)]

num_runs = str(raw_input("How many runs?  "))

### Application ###
for d in date_list:
    yearr = d.year
    monthh = d.month
    datee = d.day

    print(str(d))
    game_day = mlbgame.games(yearr, monthh, datee)
    games = mlbgame.combine_games(game_day)
    for game in games:
        g = str(game)
        if "(%s)" % num_runs in g:
            print(g)
