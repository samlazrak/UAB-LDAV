import csv

def tab_to_csv(_axgt, _csv):
  _axgt = csv.reader(open('./data/axon_data/axontextfile_tab_delimited.axgt', "r"), delimiter='\t')
  _csv = csv.writer(open('./data/exported/axondata.csv', 'w'))
  
  _csv.writerows(_axgt)
