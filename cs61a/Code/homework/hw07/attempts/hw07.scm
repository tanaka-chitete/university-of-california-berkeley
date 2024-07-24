(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)


(define (sign num)
  (cond
    [(< num 0) -1]
    [(= num 0) 0]
    [else 1]
  )
)


(define (square x) (* x x))

(define (pow x y)
  (cond
    [(= y 0) 1]
    [(even? y) (square (pow x (/ y 2)))]
    [else (* x (square (pow x (/ (- y 1) 2))))]
  )
)


(define (unique s)
  (if (null? s) 
    '()
    (cons (car s) (unique (filter (lambda (x) (not (equal? x (car s)))) (cdr s))))
  )
)


(define (replicate x n)
  (define (replicate-sofar x n lst-sofar)
    (if (= n 0)
      lst-sofar
      (replicate-sofar x (- n 1) (cons x lst-sofar))
    )
  )
  (replicate-sofar x n nil)
)


(define (accumulate combiner start n term)
  (if (= n 0)
    start
    (combiner (accumulate combiner start (- n 1) term) (term n))
  )
)


(define (accumulate-tail combiner start n term)
  (define (accumulate-tail-sofar combiner start n term res-sofar)
    (if (= n 0)
      res-sofar
      (accumulate-tail-sofar combiner start (- n 1) term (combiner res-sofar (term n)))
    )
  )
  (accumulate-tail-sofar combiner start n term start)
)


(define-macro (list-of map-expr for var in lst if filter-expr)
  (list 'map (list 'lambda (list var) map-expr) (list 'filter (list 'lambda (list var) filter-expr) lst))
)

