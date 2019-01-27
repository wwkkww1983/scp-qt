od='./lib_widget'
uid='./ui'
pyuic5 "$uid"/scp-qt-config.ui -o "$od"/config.py
pyuic5 "$uid"/entryView.ui -o "$od"/entryView.py
pyuic5 "$uid"/historyView.ui -o "$od"/historyView.py
pyuic5 "$uid"/scp_qt.ui -o "$od"/scp_qt.py
pyuic5 "$uid"/scp_qt_tray.ui -o "$od"/scp_qt_tray.py

