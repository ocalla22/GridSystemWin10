#Assumes we are somewhere and sets project dir as the root of the repo
project_dir=`git rev-parse --show-toplevel`

#defines path to requirements file
requirements=$project_dir/requirements.txt

#defines path to main script to be packaged.
main_script=`find $project_dir -iname hello.py`

#defines path to dist folder
dist_path=$project_dir/dist

#defines virtual environment name
venv_path=$project_dir/myvenv

#Creates Virtual environment if it does not already exist
if [ ! -d "$venv_path" ]; then
    python -m venv $project_dir/myvenv  
fi

#Activates virtual environment and installs requirements
. $project_dir/myvenv/Scripts/activate
pip install -r $requirements

#packages the main file and builds dist folder in project directory.
pyinstaller --distpath $dist_path $main_script