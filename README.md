## backend

### to create a virtual environment on mac

```
python3 -m venv venv
// step to enable vitual environmant in vs code
view -> command palette -> python:select interpreter -> ./venv/bin/python

we also need to enable virtual environment in terminal
source venv/bin/activate

deactivate # to deactivate the virtial enevironment
```

### to install dependences

```
pip install -r requirements.txt
```

```
cd backend
uvicorn main:app --reload
```

```
aws ec2
nohup uvicorn main:app --reload --host 0.0.0.0 &
```

mysql docker

```
docker run --name mysqldb --platform linux/x86_64 -e MYSQL_DATABASE=admin -e MYSQL_ROOT_PASSWORD=admin -p 3306:3306 mysql:latest
```

API Server

```
http://localhost:8000/docs

```

## database - mysql

```
/usr/local/mysql/bin/mysql -u root -p
show databases;
use admin;
show tables;
```

## Installing MySQL on AWS EC2 instance - ubuntu

- mysql installation

```
sudo apt update
sudo apt install mysql-server
```

- status check on mysql server installation

```
sudo systemctl status mysql
```

- mysql command prompt

```
sudo mysql
```

- set a root password
  replace your password `your_password_here`

```
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'your_password_here'
```

- mysql command prompt

```
sudo mysql -u root -p
```

## Running FastAPI Server AWS EC2

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

## setup nginx on ec2

- nginx installation

```
sudo-apt install nginx -y
```

- start the nginx

```
systemctl start nginx
```

- check nginx status
  go to the url `http://<ip-address>`
  you can also check the status `systemctl status nginx`

- nginx configuration
  `cd /etc/nginx/sites-available`
  edit ngix file `default`
  `systemctl restart nginx`

- make sure that fastapi server is running.

## setup a firewall

```
sudo ufw status
sudo ufw allow http  # add rules
sudo ufw allow ssh   # add rules
sudo ufw enable # to make the firewall active
```

## frontend

```
cd frontend

```

- Install dependencies: `npm install` or `yarn`

- Start the server: `npm run dev` or `yarn dev`

- Views are on: `localhost:3000`

### frontend deployment to EC2

[Guide](https://medium.com/today-i-solved/how-to-deploy-next-js-on-aws-ec2-with-ssl-https-7980ec6fe8d3)

### API guide

- health score query sample:
- http://localhost:8000/healthscore/114/7417886-07?healthdate=04/20/22&plant=MC10

### Database guide

- MD04 data must be sorted according to the demand_date (oldest first)
- demand_date field format must be in mm/dd/yy (e.g., 04/20/22).
- the .csv file is in UTF-CSV format, Save the UTF-CSV file to .csv file
