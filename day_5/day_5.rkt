#lang racket

(provide array-length append emptyArray access list->array array->list)

(define-struct array (trie length))

(define emptyArray (make-array empty 0))

(define (append A v)
    (make-array (trie-set (array-length A) v (array-trie A)) (add1 (array-length A))))

(define (access A i)
    (if (>= i (array-length A))
        (error "Index Error: index out of range")
        (trie-get i (array-trie A))))

(define (list->array lst)
    (foldl (lambda (x y) (append y x)) emptyArray lst))

(define (array->list arr)
    (build-list (array-length arr) (lambda (x) (access arr x))))

(define-struct set (trie))

(define-struct node (set? value left right))
(define unset (make-node false 0 empty empty))
(define (set-node-value v T)
    (make-node true v (node-left T) (node-right T)))

(define next (lambda (x) (floor (/ x 2))))

(define (update-left update T)
    (make-node 
        (node-set? T)
        (node-value T)
        update
        (node-right T)))


(define (update-right update T)
    (make-node 
        (node-set? T)
        (node-value T)
        (node-left T)
        update))

(define (trie-set i v T)
    (define (help temp trie)
        (cond
            [(empty? trie) (help temp unset)]
            [(zero? temp) (set-node-value v trie)]
            [(even? temp) (update-left (help (next temp) (node-left trie)) trie)]
            [else (update-right (help (next temp) (node-right trie)) trie)]))
    (help i T))

(define (trie-has v T)
    (define (help temp trie)
        (cond  
            [(empty? trie) false]
            [(zero? temp) (node-set? trie)]
            [(even? temp) (help (next temp) (node-left trie))]
            [else (help (next temp) (node-right trie))]))
    (help v T))

(define (trie-get i T)
    (define (help temp trie)
        (cond
            [(zero? temp) (node-value trie)]
            [(even? temp) (help (next temp) (node-left trie))]
            [else (help (next temp) (node-right trie))]))
    (help i T))

(define (trie-get-or-false i T)
    (define (help temp trie)
        (cond
            [(empty? trie) false]
            [(zero? temp) (node-value trie)]
            [(even? temp) (help (next temp) (node-left trie))]
            [else (help (next temp) (node-right trie))]))
    (help i T))

(define (hash item)
    (define (hash-number x)
        (abs (floor x)))
    (define (hash-string s)
        (foldr (lambda (x y) (+ (char->integer x) y)) 0 (string->list s)))
    (cond
        [(number? item) (hash-number item)]
        [(string? item) (hash-string item)]))