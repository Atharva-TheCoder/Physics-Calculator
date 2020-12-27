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
echo '    Updating Termux...   '
echo " "
echo " "
sleep 2.0
apt-get update -y
echo " "
echo " "
apt-get upgrade -y
echo " "
echo " "
echo '   Installing necessary packages...   '
echo " "
echo " "
sleep 1.0
pkg install python -y
echo " "
echo " "
pkg install python2 -y
echo " "
echo " "
pip install lolcat
echo " "
echo '   Package installed successfully...   '
sleep 2.0
clear
echo '   Please wait for few seconds...   '
echo '       Making some changes...       '
cd 
cd Physics-Calculator
chmod +x runcalc.sh
sleep 2.0
clear
echo '   Installation completed...   '
sleep 2.0
echo " "
echo "  Type 'runcalc.sh' in any directory to "
echo "             start calculator       "  
sleep 5.0 
clear
./runcalc.sh
