import sys

input = sys.stdin.readline
# int fibonacci(int n) {
#     if (n == 0) {
#         printf("0");
#         return 0;
#     } else if (n == 1) {
#         printf("1");
#         return 1;
#     } else {
#         return fibonacci(n‐1) + fibonacci(n‐2);
#     }
# }
test_case = int(input())
n_list = [int(input()) for i in range(test_case)]
n_max = max(n_list)
fibonacci_list = [[]*40]

def fibonacci(n):
    if fibonacci_list[n].empty():
        return 
