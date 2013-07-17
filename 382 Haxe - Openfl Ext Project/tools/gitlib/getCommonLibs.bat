@ECHO OFF

git clone http://192.168.102.200/gitlab/darcyg/systemcommonlib.git
cd systemcommonlib
git archive -o ..\systemcommonlib.tar master
cd ..
tar -Pxf systemcommonlib.tar -C ../../
rm -Rf systemcommonlib*