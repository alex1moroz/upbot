from base import Database
import requests
from big_base import Database

database = Database(host='ec2-34-192-173-173.compute-1.amazonaws.com',
                    database='df0b31na5sq5g1',
                    user='zdbkddrjcbayyh',
                    password='41423ae124efcd6d5ecfb904a1bbab37980bcb18781e83736c5fb93f73da7f61')


class Datachange:

    result = database.execute_query('select * from site')

    def check(self):
        count = len(Datachange.result)

        for num in count:
            pg = Datachange.result[num][0]
            print(pg)
            # rq = requests.get(pg)
            # status = rq.status_code
            # if status == 200:
            #     message = f'{pg} гуд'
            # else:
            #     message = f'Страница {pg} упала!!! Код ошибки {status}'
            # print(message)
Datachange.check(())
print(len(Datachange.result))
print(Datachange.result[0][0])




