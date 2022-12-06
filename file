#
SRCDOCS=/home/pbrian/src/rhaptos2.user/docs/_build/html

cd $SRCDOCS
MSG="Adding gh-pages docs for `git log -1 --pretty=short --abbrev-commit`"

TMPREPO=/tmp/docs/user
rm -rf $TMPREPO
mkdir -p -m 0755 $TMPREPO

git clone git@github.com:Connexions/rhaptos2.user.git $TMPREPO
cd $TMPREPO
git checkout gh-pages  ###gh-pages has previously one off been set to be nothing but html
cp -r $SRCDOCS/ $TMPREPO
git add -A
git commit -m "$MSG" && git push origin gh-pages
