## backend

### to create a virtual environment on mac

```
python3 -m venv venv
// step to enable vitual environmant in vs code
view -> command palette -> python:select interpreter -> ./venv/bin/python

we also need to enable virtual environment in terminal
source venv/bin/activate

deactivate # to deactivate the virtial enevironment

The virtual environment helps us to prepare `requirements.txt` file `pip freeze > requirements.txt`

```

### backend

```
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
http://localhost:8000/docs
```

## frontend

```
cd frontend
Install dependencies: `npm install` or `yarn`
Start the server: `npm run dev` or `yarn dev`
Views are on: `localhost:3000`

```

## data wrangling

- MD04 data must be sorted according to the demand_date (oldest first)
- demand_date field format must be in mm/dd/yy (e.g., 04/20/22).
- the .csv file is in UTF-CSV format, Save the UTF-CSV file to .csv file

### Deploying server on AWS EC2

### EC2 instance preparation

- Spin EC2 instance and ssh terminal
- upgrade repo: `sudo apt update && sudo apt upgrade -y`
- python version check: `python3 --version`
- pip version check: `pip --version` , `pip3 --version`
- pip installation: `sudo apt install python3-pip`
- install virtual environment using pip
  `sudo pip3 install virtualenv`

- to set the password on ubuntu, `sudo su`, `passwd ubuntu`

- working as a root user is bit risky, so we can create a user,
  which has similar privilleges

  `adduser pankesh`, `su - pankesh` , `usermod -aG sudo pankesh`

### setup fastapi server repository

- folder structure:

  ```
   app
    |- src
        |- frontend
        |- backend
        |- README.md
        |- Datasets
        |- ...
    |- venv

  ```

- `mkdir app`, `cd app`
- `virtualenv venv` # create a virtual environment:
- `source venv/bin/activate` # to activate virtual env
- `deactivate` # to deactivate

- `mkdir src` , `cd src`
- clone github repo to `src`
- `git clone https://github.com/pankeshpatel/postgre-planner-server.git .`

- `pip install -r requirements.txt` # to install requirements
-

### Postgres db

- install postgres database  
   `sudo apt install postgresql postgresql-contrib -y`

- to connect to postgresql database, one need `psql` cli
  to check the installation: `psql --version`

- to help on command line on `psql --help`

- the default user on EC2 machine is `ubuntu`
  postgres can not allow `ubuntu` user to access postgres
  to see created users: `sudo cat /etc/passwd`
  change the user `su - postgres`

- `psql -U postgres` # to connect to database using `psql` cli
  `\password postgres` # to set a new password for postgres
  `\q` # to exit out of postgres cli
  `exit` # to logout from postgres database

- to change postgres configuration
  navigate to `/etc/postgresql/14/main`
  you will see a list of files

- `pg_hba.conf` `postgresql.conf`

- to edit `sudo nano postgresql.conf`, you can
  `listen_addresses = '*'`

- to edit `sudo nano pg_hba.conf`
  change authentication from `peer` to `md5` (password based)
  `local all postgres md5`
  `local all all md5`
  `host all all 0.0.0.0/0 md5`
  `host all all ::/0 md5`

  to change into effect, restart the `postgresql` application
  `systemctl restart postgresql`

- how to connect pgadmin (running on Mac) to postgresql on sql
  add new server -> provide name and ip address of AWS

### redis installation

- refer redis documentation
- to check redis status: `redis-cli -h localhost -p 6379 ping`

## server setup on ec2 (optional)

```
uvicorn --host 0.0.0.0 main:app --reload
```

- If the application is crashed / reboot our machhine, `uvicorn` does not restart automatically.
  for these feature use we will use process manager -- `gunicorn`

```
pip install gunicorn
gunicorn -w 1 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:8000

# for background
nohup gunicorn -w 1 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:8000
```

### setup nginx on ec2

- nginx installation

```
sudo-apt install nginx -y # nginx installation
systemctl start nginx  # start the nginx
```

- check nginx status
  go to the url `http://<ip-address>`
  you can also check the status `systemctl status nginx`

- nginx configuration
  `cd /etc/nginx/sites-available`
  edit ngix file `default`
  `systemctl restart nginx`

- make sure that fastapi server is running.

### setup a firewall

```
sudo ufw status
sudo ufw allow http  # add rules
sudo ufw allow ssh   # add rules
sudo ufw enable # to make the firewall active
```
