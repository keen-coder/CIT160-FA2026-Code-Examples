# This program displays a stair-step pattern.


def main():
   NUM_STEPS = 6

   for r in range(NUM_STEPS):
      for c in range(r):
         print(' ', end='')
      print('#')

if __name__ == '__main__':
   main()
