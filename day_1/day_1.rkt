#lang racket
(define in (open-input-file "./day_1/input.txt"))

(define char->string
    (lambda (c) (list->string (list c))))

(define string-rest
    (lambda (s) (substring s 1 (string-length s))))

(define string-first
    (lambda (s) (char->string (string-ref s 0))))

(define (get-nums str)
    (map string->number (regexp-match* #rx"[1.2.3.4.5.6.7.8.9.0]+" str)))

(define (read-day1 f a b)
    (let* [(l (read-line in))]
    (if (eof-object? l) (list a b)
        (read-day1 f (cons (first (get-nums l)) a) (cons (second (get-nums l)) b)))))

(define (parse-pt1 a b)
    (define (help a b sum)
        (if (empty? a) sum
            (help (rest a) (rest b) (+ sum (abs (- (first a) (first b)))))))
    (help a b 0))

(define (parse-pt2 a b)
    (define (help a b sum)
        (if (empty? a) sum
            (help (rest a) b (+ sum 
                (* (first a) 
                    (count (lambda (x) (= x (first a))) b))))))
    (help a b 0))

(define inp (read-day1 in empty empty))
(define a (first inp))
(define b (second inp))
(define a-sorted (sort a <))
(define b-sorted (sort b <))

(printf "pt1: ~a\n" (parse-pt1 a-sorted b-sorted))
(printf "pt2: ~a\n" (parse-pt2 a b))


(close-input-port in)