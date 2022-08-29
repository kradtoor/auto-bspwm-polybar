Se ha testeado este script en Parrot-security-5.0.1.

# Instalación
```sh
  git clone https://github.com/kradtoor/auto-bspwm-polybar
  cd auto-bspwm-polybar/
  python3 main.py
```

## Preview
![BSPWM](https://i.ibb.co/B4YbKDy/2021-12-07-150410-1920x1080-scrot.png "auto-bspwm-polybar by KradToor")

## Target
```sh
  settarget  "HTB's IP"
  cleartarget
```

## Utilidades:
- **bspwm**: Tiling Window Manager.
- **zsh**: Shell.
- **oh-my-zsh**: Oh-My-Zsh.
- **sxhkd**: Escucha los eventos del teclado y ejecuta comandos.
- **polybar**: Herramienta  para crear barras de estado.
- **polybar-themes**: Temas para la polybar.
- **rofi**: Lanzador de aplicaciones.
- **feh**: Visor de imágenes.
- **fzf**: Buscador de línea de comandos.
- **scripts**: extractPorts, whichSystem.
- **kitty**:  Terminal.

## Shortcuts
<kbd>Windows</kbd> + <kbd>Enter</kbd> : Abre la consola (kitty).  
<kbd>Ctrl</kbd> + <kbd>1,2,3,4,5,6,7,8,9</kbd> : Cambia entre las tabs de la consola (kitty).  
<kbd>Windows</kbd> + <kbd>W</kbd> : Cierra la ventana actual.  
<kbd>Windows</kbd> + <kbd>Alt</kbd> + <kbd>R</kbd> : Reinicia la configuración del bspwm.  
<kbd>Windows</kbd> + <kbd>Alt</kbd> + <kbd>Q</kbd> : Cierrar la sesión.  
<kbd>Windows</kbd> + <kbd>(⬆⬅⬇➡)</kbd> : Moverse por las ventanas en la workspace actual.  
<kbd>Windows</kbd> + <kbdD</kbd> : Abre el Rofi. <kbd>Esc</kbd> para salir.  
<kbd>Windows</kbd> + <kbd>(1,2,3,4,5,6,7,8,9,0)</kbd> : Cambia entre los workspace.  
<kbd>Windows</kbd> + <kbd>T</kbd> : Cambia la ventana actual a modo "terminal" (normal). Nos sirve cuando la ventana está en modo pantalla completa o flotante.  
<kbd>Windows</kbd> + <kbd>M</kbd> : Cambia la ventana actual a modo "completo" (no ocupa la polybar). Presione la mismas teclas para volver a modo "terminal" (normal).  
<kbd>Windows</kbd> + <kbd>F</kbd> : Cambia la ventana actual a modo pantalla completa (ocupa todo incluyendo la polybar).  
<kbd>Windows</kbd> + <kbd>S</kbd> : Cambia la ventana actual a modo "flotante".  
<kbd>Windows</kbd> + <kbd>Alt</kbd> + <kbd>(1,2,3,4,5,6,7,8,9,0)</kbd> : Mueve la ventana actual a otro workspace.  
<kbd>Windows</kbd> + <kbd>Alt</kbd> + <kbd>(⬆⬅⬇➡)</kbd> : Cambia el tamaño de la ventana actual (solo funciona si está en modo terminal o flotante).  
<kbd>Windows</kbd> + <kbd>Ctrl</kbd> + <kbd>(⬆⬅⬇➡)</kbd> : Cambia la posición de la ventana actual (solo funciona en modo flotante).  
<kbd>Windows</kbd> + <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>(⬆⬅⬇➡)</kbd> : Muestra una preselección para luego abrir una aplicación.  
<kbd>Windows</kbd> + <kbd>Ctrl</kbd> + <kbd>Space</kbd> para deshacer la preselección.  

## Commands:
- **Abrir imagen en el terminal**:
```sh
  kitty +kitten icat /path/to/image/picture.png
```

## Créditos
- Tomado como referencia del repo de [yorkox](https://github.com/yorkox0/autoBspwm)
- Autor: KradToor
- Video de configuración de [S4vitar](https://www.youtube.com/watch?v=mHLwfI1nHHY)
