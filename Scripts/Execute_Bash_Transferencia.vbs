' Funcion: Ejecuta un comando Python (argumento[0]) dada una ruta especificada y 2 variables entregadas desde AA.
' Necesidad: Filtrar un .csv (argumento[1]) con una serie de condiciones especificadas en archivo python y dejar
'            los resultados en un nuevo archivo .csv (argumento[2]).


' Se asigna el SHELL a ocupar
Set WshShell = WScript.CreateObject("WScript.Shell") 

Set ObjShell = CreateObject("Shell.Application") 
ObjShell.ShellExecute WScript.Arguments(0) , """" & WScript.ScriptFullName & """ RunAsAdministrator", , "runas", 1 
WScript.Quit 
 



' Syntaxis: oShell.Run(strCommand, [intWindowStyle], [bWaitOnReturn]) 
' Componentes:
'    - strCommand
'           Valor de cadena que indica la l?nea de comando que desea ejecutar. Debe incluir cualquier par?metro 
'           que desee pasar al archivo ejecutable.

'    - [intWindowStyle] (Opcional)
'           Valor entero que indica la apariencia de la ventana del programa. Tenga en cuenta que no todos los 
'           programas hacen uso de esta informaci?n.
'             0 - Oculta la ventana y activa otra ventana.
'            (1) - Activa y muestra una ventana. Si la ventana se minimiza o maximiza, el sistema la restaura a su 
'                 tama?o y posici?n originales. Una aplicaci?n debe especificar este indicador cuando muestra la 
'                 ventana por primera vez.
'             2 - Activa la ventana y la muestra como una ventana minimizada.
'             3 - Activa la ventana y la muestra como una ventana maximizada.
'             4 - Muestra una ventana en su tama?o y posici?n m?s recientes. La ventana activa permanece activa.
'             5 - Activa la ventana y la muestra en su tama?o y posici?n actuales.
'             6 - Minimiza la ventana especificada y activa la siguiente ventana de nivel superior en el orden Z.
'             7 - Muestra la ventana como una ventana minimizada. La ventana activa permanece activa.
'             8 - Muestra la ventana en su estado actual. La ventana activa permanece activa.
'             9 - Activa y muestra la ventana. Si la ventana se minimiza o maximiza, el sistema la restaura a su 
'                 tama?o y posici?n originales. Una aplicaci?n debe especificar este indicador al restaurar una 
'                 ventana minimizada.
'             10 - Establece el estado del show en funci?n del estado del programa que inici? la aplicaci?n.

'    - [bWaitOnReturn] (Opcional)
'           Valor booleano que indica si el script debe esperar a que el programa termine de ejecutarse antes de 
'           continuar con la siguiente instrucci?n en su script. Si se establece en verdadero, la ejecuci?n del 
'           script se detiene hasta que el programa finaliza y Run devuelve cualquier c?digo de error devuelto por 
'           el programa. Si se establece en falso (el valor predeterminado), el m?todo Run regresa inmediatamente 
'           despu?s de iniciar el programa, devolviendo autom?ticamente 0 (no debe interpretarse como un c?digo de 
'           error).
