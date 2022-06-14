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
