library(readxl)
AccidentesBicicletas_2018 <- read_excel("AccidentesBicicletas_2018.xlsx")
View(AccidentesBicicletas_2018)

colnames(AccidentesBicicletas_2018)
str(AccidentesBicicletas_2018)


accidente <- AccidentesBicicletas_2018
accidente

accidente$"CPFA Lluvia" <- NULL
accidente$"CPFA Granizo" <- NULL
accidente$"CPFA Lluvia" <- NULL
accidente$"CPFA Hielo" <- NULL
accidente$"CPFA Niebla" <- NULL
accidente$"CPFA Nieve" <- NULL
accidente$"CPFA Mojada" <- NULL
accidente$"CPFA Aceite" <- NULL
accidente$"CPFA Barro" <- NULL
accidente$"CPSV Mojada" <- NULL
accidente$"CPSV Aceite" <- NULL
accidente$"CPSV Barro" <- NULL
accidente$"CPSV Grava Suelta" <- NULL
accidente$"CPSV Hielo" <- NULL
accidente$"Nº" <- NULL
accidente$"CPSV Seca Y Limpia" <- NULL
accidente$`CPFA Seco` <- NULL

colnames(accidente)

names(accidente) <- c("Fecha", "Rango Horario", "Dia Semana", "Distrito", "Lugar Accidente", "Numero Parte","Numero Victimas",
                      "Tipo Accidente","Tipo Vehiculo","Tipo Persona","Sexo","lesividad","Tramo Edad"  )
accidente$"lesividad" <- NULL
colnames(accidente)

fsexo = as.factor(accidente$Sexo)
fsexo
levels(fsexo)
summary(fsexo)
plot(fsexo)

fhoras = as.factor(accidente$`Rango Horario`)
fhoras
levels(fhoras)
summary(fhoras)

fecha <- accidente$Fecha
fecha
format(fecha, format = "%d/%m/%y")


# Realizamos la impresion de la grafica y nos damos cuenta de que estan desorganizados los dias de la semana

fdia = as.factor(accidente$`Dia Semana`)
fdia
levels(fdia)
summary(fdia)
plot(fdia)

# Para poder organizar los datos necesitamos cambiar a factor la variable: 

fechas2 <- as.factor(accidente$`Dia Semana`)

# ver como está ordenada
levels(fechas2)

# confirmar que tiene 7 niveles
nlevels(fechas2)
summary(fechas2)

# ordenar correctamente
fechas2 = factor(accidente$`Dia Semana`, levels = c("LUNES", "MARTES", "MIERCOLES", "JUEVES", "VIERNES", "SABADO", "DOMINGO"))

# confirmar que está ordenada
levels(fechas2)
summary(fechas2)
plot(fechas2)