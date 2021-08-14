### Empty Trash

Python script to empty local trash.

### to run

Full Disk Access is needed for this program to run.

### env

- `conda create -n empty`
- `conda activate empty`
- `conda install python`
- `conda install -c conda-forge schedule`
- `brew install redis`
- `conda install -c conda-forge rq`

### RUN

3 tabs are needed: 

1. `redis-server`
2. `rq worker --with-scheduler`
3. `python app.py`