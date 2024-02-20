import csv
import calendar
import pdb

from database import insert_varibles_into_summary
from mail import send_email

def extrac_data_csv():
  debit = []
  credit = []
  month_txn = {}

  with open('txns.csv',mode ='r') as file:
    next(file)
    txns = csv.reader(file)
    for txn in txns:
      credit.append(float(txn[2])) if txn[2].startswith('+') else debit.append(float(txn[2]))
      month = get_txn_month(txn[1])
      
      if month in month_txn:
        month_txn[month] += 1
      else:
        month_txn[month] = 1

  return credit, debit, month_txn

def get_avergage_amount(trxs):
  sum_trxs = sum(trxs)
  
  return sum_trxs / len(trxs)

def get_total_balance(credit, debit):
  return round(sum(credit) + sum(debit),2)

def get_txn_month(txn):
  month = txn.split('/')[0]
  return calendar.month_name[int(month)]

def format_month_tx(month):
  lines = []

  for key,value in month.items():
    lines.append(f'Number of transactions in {key} : {value}')

  return '\n'.join(lines)

def create_summary():
  credit, debit, month = extrac_data_csv()

  credit_avg = get_avergage_amount(credit)
  debit_avg = get_avergage_amount(debit)
  balance =  get_total_balance(credit, debit)

  months_resume = format_month_tx(month)

  insert_varibles_into_summary(credit_avg,debit_avg,balance,str(month))
  send_email(credit_avg,debit_avg,balance,months_resume)

if  __name__ == "__main__":
  create_summary()