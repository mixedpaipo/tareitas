#lang scheme

(define (cantidad lista)
      (if (null? lista)
          0
          (+ 1 (cantidad (cdr lista)))
      ))

;;cantidad es la misma función para la primera pregunta
;;ocupa la lista y suma 1 para cada resto de la lista

(define armar_lista
  (lambda (stock)
    (if (null? stock)
        '()
        (let* ((elemento (car stock))
               (cantidad_necesaria (car elemento))
               (compra (car(cdr elemento)))
               (cantidad_existente (cantidad compra)))
          (if (= cantidad_necesaria cantidad_existente)
              (armar_lista (cdr stock))
              (cons (list (- cantidad_necesaria cantidad_existente) (car compra)) (armar_lista (cdr stock)))
          )))))


;; armar-lista usa la funcion cantidad para checkear si la cantidad elemntos a comprar es la que tenemos
;; usamos la variable stock la cual redefinimos en otras variables para su uso más fácil
;; checkeamos con cantidad la cantidad de elemntos en la lista y vemos si es necesario añadirla a la lista final evaluada