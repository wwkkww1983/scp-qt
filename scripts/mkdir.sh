SCP_QT='scp-qt'
main(){
	if test ! -e "$HOME/$SCP_QT" ; then
		mkdir "$HOME/$SCP_QT"
		if test "$?" == "0" ; then
			return 0
		else
			return 1
		fi
	else
		if test -d "$HOME/$SCP_QT" ; then
			return 0
		else
			return 2
		fi
	fi
}
main
