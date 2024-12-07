[Setup]
AppName=Unreal Module Creator
AppVersion=1.0
DefaultDirName={pf}\Unreal Module Creator
DefaultGroupName=Unreal Module Creator
OutputDir=..\Output
OutputBaseFilename=UnrealModuleCreatorInstaller
Compression=lzma
SolidCompression=yes

[Files]
Source: "..\Output\create_module.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\Template\*"; DestDir: "{app}\Template"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\MyTool"; Filename: "{app}\dist\create_module.exe"; WorkingDir: "{app}"; IconFilename: "{app}\icon.ico"
Name: "{group}\Uninstall MyTool"; Filename: "{uninstallexe}"

[Run]
Filename: "{cmd}"; Parameters: "/C setx PATH ""{app};%PATH%"""; Flags: runhidden
