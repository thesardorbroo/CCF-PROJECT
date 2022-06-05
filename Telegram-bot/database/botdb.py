from psycopg2 import connect

from user.User import *


class BotDB:
    def __init__(self):
        self.connection = connect(
            host="ec2-44-194-117-205.compute-1.amazonaws.com",
            database="d8e1dqtfv4b376",
            user="xryuottcvtzvrl",
            password="9641a16e6819f4faaaedd432abe7c2e267a08f76e2c0b0dccb5379dcf6416d85"
        )

    async def get_user(self, user_id):
        query = f"""
        SELECT * FROM eocus WHERE user_id = {user_id}
        """
        try:
            user = await self.__read_from_base(query)
            user = user[0]
            print(user)
            return UserOS(user[0], user[1], user[2], user[3], user[4], user[5], user[6])

        except IndexError:
            return None

    async def get_barber(self, id: int):
        query = f"""
        SELECT * FROM barber WHERE id = {id}
        """
        barber = await self.__read_from_base(query)
        barber = barber[0]
        master = Barber(barber[0], barber[1], barber[2], barber[3], barber[4], barber[5], barber[6])
        return None if master is None else master

    async def get_barber_key(self, key: str):
        query = f"""
        SELECT * FROM barber WHERE key = '{key}'
        """

        barber = await self.__read_from_base(query)
        try:
            barber = barber[0]
            master = Barber(barber[0], barber[1], barber[2], barber[3], barber[4], barber[5], barber[6])
            return None if master is None else master
        except IndexError:
            return None

    async def __write_to_base(self, query):
        c = self.connection.cursor()
        c.execute(query)
        self.connection.commit()

    async def __read_from_base(self, query):
        c = self.connection.cursor()
        c.execute(query)
        return c.fetchall()

    async def add_new_user(self, user_id):
        query = f"""
        INSERT INTO eocus (user_id,step) VALUES ({user_id},1)
        """
        await self.__write_to_base(query)

    async def reserve_base(self):
        query = f"""
        ALTER TABLE barbershop ADD COLUMN region VARCHAR(64)
        """
        await self.__write_to_base(query)

    async def update_column(self, user_id: int, column: str, value: any):
        query = ""
        if type(value) == int:
            query = f"""
            UPDATE eocus SET {column} = {value} WHERE user_id = {user_id}
            """
        else:
            query = f"""
            UPDATE eocus SET {column} = '{value}' WHERE user_id = {user_id}
            """

        await self.__write_to_base(query)

    async def update_all_column(self, user_id):
        query = f"""
        UPDATE eocus SET step = {1} WHERE user_id = {user_id}
        """
        await self.__write_to_base(query)

    async def delete_from_base(self, user_id):
        query = f"""
        DELETE FROM eocus WHERE user_id = {user_id}
        """

        await self.__write_to_base(query)

    async def show_all_data(self):
        query = f"""
        SELECT * FROM eocus
        """
        data = await self.__read_from_base(query)
        for i in data:
            print(i, "+++++")

    async def get_barber_orders(self, barber_id: int, day: str):
        query = f"""
        SELECT * FROM orders WHERE barber_id = {barber_id} and order_day = '{day}'
        """
        orders = await self.__read_from_base(query)
        if orders is None:
            return None

        else:
            return orders

    async def update_table_orders_p1(self, user: UserOS, day: str):
        query = f"""
        INSERT INTO orders (barber_id, customer_id, order_day) 
        VALUES ({user.barber_id}, {user.id}, '{day}')
        """
        await self.__write_to_base(query)

    async def update_table_orders_p2(self,user: UserOS, order_time, id: int):
        print("UPDAATE ",id, '\t\t', user.id)
        query = f"""
        UPDATE orders SET order_time = '{order_time}' WHERE id = {id}
        """
        await self.__write_to_base(query)

    async def get_one(self, customer_id: int, barber_id: int):
        query = f"""
        SELECT * FROM orders WHERE customer_id = {customer_id} and barber_id = {barber_id}
        """
        return await self.__read_from_base(query)














