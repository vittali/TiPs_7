#!/bin/zsh
alias inkscape=$NUAGE/software/Inkscape-0e150ed-x86_64.AppImage

 inkscape --export-dpi=768 --export-type="png" --export-area-drawing --export-filename=../latex/hardware/EP.png ../latex/hardware/EP.svg
 
