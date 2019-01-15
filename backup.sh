#!/usr/bin/env bash
function paint_stripper(){
	read a
	echo "$a" | sed s/'"'/''/g
}
function datecode(){
       	date +"%H%M%S_%m%d%Y"
}

CONFIG='./backup.json'
ARCHIVE="`jq '.destination' $CONFIG | paint_stripper`"
SOURCE="`jq '.source' $CONFIG | paint_stripper`"
FNAME="`jq '.fname' $CONFIG | paint_stripper`"
EXT="`jq '.ext' $CONFIG | paint_stripper`"
FNAME_FULL="$ARCHIVE/$FNAME-`datecode`.$EXT"
LOG="`jq '.log' $CONFIG | paint_stripper`"

function backup(){
	tar -Jcvf "$FNAME_FULL" "$SOURCE"
	printf "\033[1;31;40m$FNAME_FULL\033[1;40;m\n" | tee "$ARCHIVE/$LOG"
}
backup
