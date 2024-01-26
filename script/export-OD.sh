#!/bin/zsh
alias inkscape=$NUAGE/software/Inkscape-0e150ed-x86_64.AppImage

 inkscape --export-dpi=384 --export-type="png" --export-area-drawing --export-filename=../latex/hardware/modules/MA/OD/OD.png ../latex/hardware/modules/MA/OD/OD.svg
 
