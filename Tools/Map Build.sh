if not exist "../Bin/" mkdir "../Bin/"

del /f "..\Bin\Assets 1.SC2Mod"
del /f "..\Bin\Assets 2.SC2Mod"
del /f "..\Bin\Assets 3.SC2Mod"
del /f "..\Bin\Assets 4.SC2Mod"
del /f "..\Bin\UA Data.SC2Mod"
del /f "..\Bin\UA UI.SC2Mod"
del /f "..\Bin\Utility.SC2Mod"
del /f "..\Bin\Undead Assault 3 Dasdan.SC2Map"

new "../Bin/Assets 1.SC2Mod"
new "../Bin/Assets 2.SC2Mod"
new "../Bin/Assets 3.SC2Mod"
new "../Bin/Assets 4.SC2Mod"
new "../Bin/UA Data.SC2Mod"
new "../Bin/UA UI.SC2Mod"
new "../Bin/Utility.SC2Mod"
new "../Bin/Undead Assault 3 Dasdan.SC2Map"

add "../Bin/Assets 1.SC2Mod" "../Development/Assets 1.SC2Mod/*" /r /c /auto
add "../Bin/Assets 2.SC2Mod" "../Development/Assets 2.SC2Mod/*" /r /c /auto
add "../Bin/Assets 3.SC2Mod" "../Development/Assets 3.SC2Mod/*" /r /c /auto
add "../Bin/Assets 4.SC2Mod" "../Development/Assets 4.SC2Mod/*" /r /c /auto
add "../Bin/UA Data.SC2Mod" "../Development/UA Data.SC2Mod/*" /r /c /auto
add "../Bin/UA UI.SC2Mod" "../Development/UA UI.SC2Mod/*" /r /c /auto
add "../Bin/Utility.SC2Mod" "../Development/Utility.SC2Mod/*" /r /c /auto
add "../Bin/Undead Assault 3 Dasdan.SC2Map" "../Development/Undead Assault 3 Dasdan.SC2Map/*" /r /c /auto

f "../Bin/Assets 1.SC2Mod"
f "../Bin/Assets 2.SC2Mod"
f "../Bin/Assets 3.SC2Mod"
f "../Bin/Assets 4.SC2Mod"
f "../Bin/UA Data.SC2Mod"
f "../Bin/UA UI.SC2Mod"
f "../Bin/Utility.SC2Mod"
f "../Bin/Undead Assault 3 Dasdan.SC2Map"