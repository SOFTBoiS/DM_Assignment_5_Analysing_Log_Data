import csv
from log_entry import LogEntry
from automaton import Automaton


def analyze_log(file):
    with open(file) as csv_file:
        aut = Automaton()
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_reader.__next__()
        for row in csv_reader:
            le = LogEntry(*row)
            try:
                aut.make_action(le.instance, le.action)
            except Exception as e:
                print(str(e), le.instance, le.action)
            print('number of instances running ', aut.number_of_instances())
