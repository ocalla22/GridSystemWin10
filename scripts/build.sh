#Assumes we are somewhere in the project and sets project dir as the root of the repo
project_dir=`git rev-parse --show-toplevel`

#Creates Virtual environment if it does not already exist
if [ ! -d "$project_dir/myvenv" ]; then
    python -m venv $project_dir/myvenv 
fi

#Activates virtual environment and installs requirements. Hide 'already satisfied' to keep logs clean.
source $project_dir/myvenv/Scripts/activate
pip install -r $project_dir/requirements.txt \
| grep -v 'already satisfied'

#defines path to main script to be packaged.
main_script=`find $project_dir -iname main.py`

#packages the main file and builds dist folder in project directory.
pyinstaller \
    --distpath $project_dir/dist \
    --workpath $project_dir/build\
    --specpath $project_dir \
    --clean \
    $main_script