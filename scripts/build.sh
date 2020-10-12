#Signals to activate venv. Pycharm can't activate venvs in scripts.
#https://youtrack.jetbrains.com/issue/PY-21974
activate_venv=true

print_expected_usage() {
  printf "Usage: ..."
}

while getopts 'a' flag; do
  case "${flag}" in
    a) activate_venv='' ;;
    *) print_expected_usage
       exit 1 ;;
  esac
done

#Assumes we are somewhere in the project and sets project dir as the root of the repo
project_dir=`git rev-parse --show-toplevel`

#Creates Virtual environment if it does not already exist
if [ ! -d "$project_dir/myvenv" ]; then
    python -m venv $project_dir/myvenv
fi

#Activate venv if flag is set.
if [ $activate_venv ]; then
    . $project_dir/myvenv/Scripts/activate
fi

#Installs requirements but hide 'already satisfied' to keep logs clean.
pip install -r $project_dir/requirements.txt | grep -v 'Requirement already satisfied'

#defines path to main script to be packaged.
main_script=`find $project_dir -iname app.py`

#packages the main file and builds dist folder in project directory.
pyinstaller \
    --distpath $project_dir/dist \
    --workpath $project_dir/build\
    --specpath $project_dir \
    --clean \
    $main_script