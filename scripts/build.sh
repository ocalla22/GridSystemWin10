#Assumes we are somewhere and sets project dir as the root of the repo
project_dir=`git rev-parse --show-toplevel`

#defines path to requirements file
requirements=$project_dir/requirements.txt

#defines path to main script to be packaged.
main_script=`find $project_dir -iname hello.py`

#defines path to dist folder
dist_path = $project_dir/dist

#Creates and activates virtual environemt and installs requirements
python -m venv $project_dir/myvenv
. $project_dir/myvenv/Scripts/activate
pip install -r $requirements

#packages the main file and builds dist folder in project directory.
pyinstaller --distpath $dist_path $main_script