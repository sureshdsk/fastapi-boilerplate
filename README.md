# fastapi-starter-kit

## run using docker
```
docker build -t dsk-fast-api-1 .

docker run -d --name mycontainer -p 8000:8000 dsk-fast-api-1
```

```
git clone https://github.com/sureshdsk/fastapi-starter-kit.git

cd /path/to/project-root

# create virtualenv
virtualenv -p python3 venv

# activate virtualenv
. venv/bin/activate

# install dependancies
pip install -r requirements.txt

# run app
./run.sh 
./run_async.sh # runs async version
```
