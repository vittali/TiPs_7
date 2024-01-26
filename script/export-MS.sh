#!/bin/zsh
alias inkscape=$NUAGE/software/Inkscape-0e150ed-x86_64.AppImage

 inkscape --export-dpi=384 --export-type="png" --export-area-drawing --export-filename=../latex/hardware/modules/PO/MS/MS.png ../latex/hardware/modules/PO/MS/MS.svg
 
