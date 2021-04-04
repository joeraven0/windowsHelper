set /P filetype=Remove all filetype extensions: 

del /F /A *."%filetype%"

set /P All removed=True