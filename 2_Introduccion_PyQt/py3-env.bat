@ECHO OFF 

set OSGEO4W_ROOT=D:\OSGeo4W64

@echo off
call "%OSGEO4W_ROOT%\bin\o4w_env.bat"
call "%OSGEO4W_ROOT%\bin\qt5_env.bat"
call "%OSGEO4W_ROOT%\bin\py3_env.bat"

@echo off
path %OSGEO4W_ROOT%\apps\qgis\bin;%PATH%
set QGIS_PREFIX_PATH=%OSGEO4W_ROOT:\=/%/apps/qgis
set GDAL_FILENAME_IS_UTF8=YES

set VSI_CACHE=TRUE
set VSI_CACHE_SIZE=1000000
set QT_PLUGIN_PATH=%OSGEO4W_ROOT%\apps\qgis\qtplugins;%OSGEO4W_ROOT%\apps\qt5\plugins
set PYTHONPATH=%OSGEO4W_ROOT%\apps\qgis\python;%PYTHONPATH%

cd /d %~dp0
::python3 CreateCanvas.py
::python3 CreateCanvas_FakeIface.py
::python3 comrobacion_processing.py
::python3 comrobacion_qgis.py
::python3 extractvertices_standalone.py
::python3 processing_standalone_QGIS3_2.py
::pause

REM Abrimos la consola
start cmd
REM Abrimos Python directamente
::"%PYTHONHOME%\python" %*

