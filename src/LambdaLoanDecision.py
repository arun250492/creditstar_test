import psycopg2
from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        loan_op=cur.execute('SELECT * from <loan_history_table>')
        For i in loan_op:
          paid_loans=i[client][paid_loans][count]
          days_since_last_late_payment=i[client][days_since_last_late_payment][count]
          If paid_loans==1 and days_since_last_late_payment<=30:
            Print("Loan will be given")
          else:
            Print("Loan will not be given")
            
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()
