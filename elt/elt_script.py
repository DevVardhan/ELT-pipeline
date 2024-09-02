import subprocess
import time 

# rechecking docker connection with postgres
def wait_for_postgress(host , maxretries = 5 , delayed_seconds = 5):
    retries = 0 
    while(retries < maxretries):
        try:
            result = subprocess.run(["pg_isready", "h" , host] , check=True , capture_output=True , text=True)
            if "accepting connections" in result.stdout:
                print("Successfully connected to postgres")
                return True 
        except subprocess.CalledProcessError as e:
            print(f"Error connecting to postgres: {e}")
            retries+=1 
            print(f"Retrying in {delayed_seconds} seconds .. Attemt {retries} of {maxretries}")
            time.sleep(delayed_seconds) 
    print("Max retries reached")
    return False

if not wait_for_postgress(host="source_postgres"):
    exit(1)

print("***Starting Elt script*** ")

# dump files(backup file) for extraction database
source_config = {
    'dbname': 'source_db',
    'user': 'postgres',
    'password':'password',
    'host': 'source_postgres'
}

# dump files(backup file) for loading database
destination_config = {
    'dbname': 'destination_db',
    'user': 'postgres',
    'password':'password',
    'host': 'destination_postgres'
}

#mapping dump commands
dump_command =[
    'pg_dump',
    '-h' ,source_config['host'] , 
    '-u' , source_config['user'],
    '-d' , source_config['dbname'] ,
    '-f','data_dump.sql' ,
    #auto mapped to password 
    '-w'
]

#created an env for subprocess so auto use the password for source database
subprocess_env = dict(PASSWORD= source_config['password'])

# dumpped everything to source database
subprocess.run(dump_command , env=subprocess_env , check=True)

#mapping load commands
load_command =[
    'psql',
    '-h' ,destination_config['host'] , 
    '-u' , destination_config['user'],
    '-d' , destination_config['dbname'] ,
    '-a','-f','data_dump.sql' ,
    #auto mapped to password 
]


#created an env for subprocess so auto use the password for destination database
subprocess_env = dict(PASSWORD= destination_config['password'])

# dumpped everything to destination database
subprocess.run(load_command , env=subprocess_env , check=True)