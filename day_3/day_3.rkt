#lang racket
(define in (open-input-file "./day_3/input.txt"))
(define inp (port->string in))
(close-input-port in)


(define char->string
    (lambda (c) (list->string (list c))))

(define string-rest
    (lambda (s) (substring s 1 (string-length s))))

(define string-first
    (lambda (s) (char->string (string-ref s 0))))

(define (get-prod str)
    (foldr * 1 (map string->number (regexp-match* #rx"[1.2.3.4.5.6.7.8.9.0]+" str))))

(define pt1 
    (foldr + 0 (map get-prod 
        (regexp-match* #rx"mul\\([1.2.3.4.5.6.7.8.9.0]+,[1.2.3.4.5.6.7.8.9.0]+\\)" inp))))

(define 2rx (regexp-match* #rx"mul\\([1.2.3.4.5.6.7.8.9.0]+,[1.2.3.4.5.6.7.8.9.0]+\\)|do\\(\\)|don't\\(\\)" inp))

(define (parse-second lst)
    (define (help lst off? sum)
        (cond
            [(empty? lst) sum]
            [(string=? (first lst) "do()")
             (help (rest lst) false sum)]
            [(string=? (first lst) "don't()")
             (help (rest lst) true sum)]
            [off?
             (help (rest lst) off? sum)]
            [else
             (help (rest lst) off? (+ sum (get-prod (first lst))))]))
    (help lst false 0))

(define pt2 (parse-second 2rx))

(printf "pt1: ~a\npt2: ~a\n" pt1 pt2)