#!/bin/sh

# simple script to build and push to gh-pages
# designed to be run from master

# To use this script you need another copy of the repo, right next this
# one, but named "IntroToPython.gh-pages"
# this script then builds the docs, then copies them to the other repo
# then pushed to the gh-pages branch.


# make the docs
make html

# copy to other repo (on the gh-pages branch)
cp -R build/html/ ../../IntroToPython.gh-pages

cd ../../IntroToPython.gh-pages
git checkout gh-pages
git add * # in case there are new files added
git commit -a -m "updating presentation materials"
git pull -s ours
git push
