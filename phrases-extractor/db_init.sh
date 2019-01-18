#! /usr/bin/env bash
DB='statements.db'
SQL='create table if not exists statements(phrase text,tag text,rowid integer primary key autoincrement);'
sqlite3 "$DB" "$SQL"
