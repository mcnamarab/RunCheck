import datetime
import mlbgame


def results(numdays, inclusion, numruns):
    base = datetime.datetime.today()

    if inclusion == False:
        date_list = [base - datetime.timedelta(days=x) for x in range(1, numdays)]
    else:
        date_list = [base - datetime.timedelta(days=x) for x in range(0, numdays)]
    

 ### Application ###
    
    f = open('results.txt', 'a')  # opens results file
    # deletes current contents of results file
    f.seek(0)
    f.truncate()
    f.close()
    
    for d in date_list:
        yearr = d.year
        monthh = d.month
        datee = d.day
        date_format = "%d" % monthh + "/%d" % datee +"/%d" % yearr
        
        f = open('results.txt', 'a')
        f.write(str('\n' + date_format) + '\n')
        f.close()
    
        results =[]
        
        game_day = mlbgame.games(yearr, monthh, datee)
        games = mlbgame.combine_games(game_day)
        
        for game in games:
            g = str(game)
            if "(%s)" % numruns in g:
                results.append(str(g))
        
        if len(results) > 0:
            for x in results:        
                f = open('results.txt', 'a')
                f.write(x + '\n')
                f.close()
    
        else:  # if no game have score number, prints message to thirteen_results.txt
            f = open('results.txt', 'a')
            f.write("There were no games with %d runs" % numruns + '\n')
            
 