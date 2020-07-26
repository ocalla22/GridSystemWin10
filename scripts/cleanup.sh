#Assumes we are somewhere and sets project dir as the root of the repo
project_dir=`git rev-parse --show-toplevel`

#Removes dist and build folders.
rm -r $project_dir/dist/ \
      $project_dir/build/ 

#Removes .spec file
rm $project_dir/hello.spec