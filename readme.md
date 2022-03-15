# list env
conda env list

# create env
conda create --name fastapi

# activate env
conda activate fastapi

# install pip in environment
conda install -n fastapi pip

# install modules
pip install -r requirements.txt


# deactivate env
conda deactivate

# remove env
conda remove --name fastapi --all