# Definición de las fuentes y el objetivo
SOURCES := Pikinim.java Cyan.java Magenta.java Amarillo.java Zona.java ILevantar.java Pieza.java Enemigo.java Pildora.java Muralla.java Juego.java
MAIN_CLASS := Juego

# Opciones del compilador Java
JC := javac
JVM := java
JFLAGS := -g

# Objetivos
CLASSES := $(SOURCES:.java=.class)

# Reglas de compilación
.SUFFIXES: .java .class
.java.class:
	$(JC) $(JFLAGS) $*.java

all: $(CLASSES)

run: $(MAIN_CLASS).class
	$(JVM) $(MAIN_CLASS)

clean:
	$(RM) *.class

.PHONY: all run clean
