#lang scheme

(define cantidades_cola
  (lambda (base lista)
    (define (iter lista suma)
      (if (null? lista)
          (reverse suma)
          (iter (cdr lista)
                (cons (apply (car lista) (list base)) suma))))
    (iter lista '())))
                      
          
    
(define cantidades_simple
  (lambda (base lista)
    (if (null? lista)
        '()
        (cons (apply (car lista) (list base))
              (cantidades_simple base (cdr lista)))))
)

;; cantidades_cola hace una recursión de cola
;; usando base y lista, al checkear que la lista es nula, le da la vuelta a suma que es el resultado final de las funciones evaluadas
;; cantidades_simple solo evalua usando base y lista con una recursión simple
;; recalcar que cantidades_simple evalua a una lista vacía en el caso de ser nula