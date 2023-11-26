#lang scheme


(define contiene_ingrediente
   (lambda (ingrediente ingredientes)
    (cond
      ((null? ingredientes) #f)
      ((eqv? ingrediente (car ingredientes)) #t)
      (else (contiene_ingrediente ingrediente (cdr ingredientes))))))


;;contiene_ingrediente checkea si el ingrediente existe en una receta
;;esto haciendo eqv? y haciendo recursión con el resto de los ingredientes
;; es un trabajo en conjunto de  busqueda intensiva y contiene_ingredientes
                            
(define busquedaintensiva
  (lambda (ingrediente lista)
    (if (null? lista)
        '()
        (if (contiene_ingrediente ingrediente (cdr (car lista)))
            (cons (car (car lista)) (busquedaintensiva ingrediente (cdr lista)))
            (busquedaintensiva ingrediente (cdr lista))))))

;;busqueda intensiva hace eso, una busqueda intensiva
;;usando la función contiene ingrediente y checkeando con esta si el ingrediente se encuentra en una receta
;;para así hacer una recursión con la siguiente parte de la lista


(define buscar_recetas
  (lambda (ingredientes recetas)
    (if (null? ingredientes)
        '()
        (cons (busquedaintensiva (car ingredientes) recetas)
              (buscar_recetas (cdr ingredientes) recetas)))))

;; buscar_recetes tiene 2 funciones auxiliares, ya que usa las dos para hacer su funcionalidad
;; busqueda intensiva llama a contiene ingrediente y lo agrega a la lista evaluada para seguir haciendo una busqueda intesiva con los demás ingredientes
;; contiene ingrediente solo checkea si es true o false la existencia del ingrediente
;; para después al final de la recursión de busqueda intensiva se hace una recursión de nuevo con buscar_recetas para las recetas que faltan