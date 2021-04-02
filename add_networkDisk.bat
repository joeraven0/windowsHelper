@echo off
title "Add/remove network location"
set /P action=(A)dd disk -(D)elete disk link:
set /P disk=Disk letter:

IF /i "%action%"=="A" goto actionAdd
IF /i "%action%"=="D" goto actionDelete
:actionAdd
set /P netlocation=Disk location ie NAS Disk1:
net use "%disk%" "%netlocation%" /PERSISTENT:YES
goto commonexit

:actionDelete
net use %disk% /Delete
goto commonexit

:commonexit
set /P er=Enter to exit: