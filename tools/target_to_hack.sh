#!/bin/sh

target=$(cat ~/.config/bin/target)

if [ -n "$target" ]; then
    echo "%{F#ffff00}ﲅ%{F#ffffff} $target%{u-}"
else
    echo "%{F#e51d0b}ﲅ%{u-}%{F#ffffff} No target"
fi
