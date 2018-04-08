from results import results
from snail import send_email
import setup





results(setup.number_of_days, setup.include_today, setup.number_of_runs)
send_email()