#lang racket
(define in (open-input-file "./day_2/input.txt"))

(define (read-lines file)
    (let [(l (read-line file))]
        (if (eof-object? l) empty
            (cons l (read-lines file)))))

(define char->string
    (lambda (c) (list->string (list c))))

(define string-rest
    (lambda (s) (substring s 1 (string-length s))))

(define string-first
    (lambda (s) (char->string (string-ref s 0))))

(define string-empty?
    (lambda (s) (zero? (string-length s))))

(define (parseline str)
    (define (help str curr_num lst)
        (cond 
            [(string-empty? str) (cons curr_num lst)]
            [(string=? (string-first str) " ")
                (help (string-rest str) "" (cons curr_num lst))]
            [else
                (help (string-rest str)
                      (string-append curr_num (string-first str))
                      lst)]))
    (foldl (lambda (x y) (cons (string->number x) y)) empty (help str "" empty)))

(define (valid_line? lst)
    (define (help lst prev_dist prev_val)
        (cond
            [(empty? lst) true]
            [else
            (let* [(val (first lst))
                   (dist (- val prev_val))]
             (cond
                [(or (and (< 0 prev_dist) (> 0 dist))
                     (and (> 0 prev_dist) (< 0 dist)))
                 false]
                [(zero? dist)
                 false]
                [(or (< dist -3) (> dist 3))
                 false]
                [else
                 (help (rest lst) dist val)]))]))
    (help (rest lst) 0 (first lst)))

(define (lose lst n)
    (if (zero? n) (rest lst)
        (cons (first lst) (lose (rest lst) (sub1 n)))))

(define perms (lambda (l) (build-list (length l) (lambda (x) (lose l x)))))

(define inp (map parseline (read-lines in)))
(close-input-port in)

(define pt1 (count valid_line? inp))
(define pt2 (count (lambda (x) (ormap valid_line? (perms x))) inp))
(printf "pt1: ~a\npt2: ~a\n" pt1 pt2)