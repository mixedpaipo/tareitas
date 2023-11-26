#lang scheme
(define (cantidad lista)
  (if (null? lista)
      0
      (+ 1 (cantidad (cdr lista))))
  )

;; cantidad evalua la cantidad de indices en la lista
;; usando la lista y sumando uno para cada resto

(define (checkear num lista)
  (if (= num (cantidad lista))
      (display "true")
      (display "false"))
  )
