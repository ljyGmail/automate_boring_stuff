import threading
import time

print('Start of program.')


def takeANap():
    time.sleep(1)
    print('Wake up!')


threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('End of program.')

# Passing Arguments to the Thread's Target Function
# print('Cats', 'Dogs', 'Frogs', sep=' & ')
threading.Thread(target=print, args=[
                 'Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})


#  Concurrency Issues
