clear

echo " "

echo " "

echo '    Installing... wait for a while...  '

sleep 2.0

echo " "

echo " "

clear

echo " "

cd $HOME

apt-get update -y

echo " "
echo " "
apt-get upgrade -y

echo " "
echo " "
pkg install python -y

echo " "
echo " "
pkg install python2 -y

echo " "
echo " "
pip install lolcat
clear

echo '   Installation completed...   '

sleep 2.0

echo " "

clear

cd Physics-Calculator

bash run.sh
