@rem bot made by dwight dolatre
@rem gh - https://github.com/hashcat26
@rem web - https://hashcat.rf.gd

@echo off && color 07
cd "%~DP0" && prompt $P$_$G$S
title DISCORD BOT ENVIRONMENT GENERATOR

if not exist .venv (
    mkdir .venv && goto venv
) else goto eof

:venv
pipenv install -r requirements.txt
del .venv\.gitignore

:eof
echo Project .venv folder initialized.
ping localhost -n 2 > nul && exit
