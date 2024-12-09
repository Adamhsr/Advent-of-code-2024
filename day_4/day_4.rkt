#lang lazy

(define True
    (lambda (x y) x))

(define False
    (lambda (x y) y))

(define If
    (lambda (b t f) (b t f)))

(define logic
    (lambda (v) (If v 1 0)))

(define Cons
    (lambda (a b) (lambda (c) (c a b))))

(define First
    (lambda (c) (c (lambda (x y) x))))

(define Rest
    (lambda (c) (c (lambda (x y) y))))

(define Empty
    (lambda (a) (lambda (x y) x)))

(define Empty?
    (lambda (c) (c (lambda (a b) (lambda (x y) y)))))

(define (lambda->bool l)
    (If l true false))

(define (bool->lambda b)
    (if b True False))


(define Y
  (lambda (f)
    ((lambda (self) (f (self self)))
     (lambda (self) (f (self self))))))

(define fact
    (Y (lambda (self)
        (lambda (n) 
        (if (zero? n) 1
            (* n (self (sub1 n))))))))

λc.(c(λa.(λb.((c d) (a b))))) (λd.(d e))