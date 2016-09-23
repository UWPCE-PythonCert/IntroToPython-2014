#!/bin/sh

# simple script to build and push to gh-pages
# designed to be run from master

# To use this script you need another copy of the repo, right next this
# one, but named "IntroToPython.gh-pages"
# this script builds the docs, then copies them to the other repo
# then pushes that to gitHub

GHPAGESDIR=../../IntroToPython.gh-pages/

# make sure the Gh pages repo is there and in the right branch
pushd $GHPAGESDIR
git checkout gh-pages
popd

# make the docs
make html
# copy to other repo (on the gh-pages branch)
cp -R build/html/ $GHPAGESDIR

pushd $GHPAGESDIR
git add * # in case there are new files added
git commit -a -m "updating presentation materials"
git pull -s ours --no-edit
# git push

