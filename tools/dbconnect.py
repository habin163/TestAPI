import pymysql

class DBCONNECT:
    """

    """
    def __init__(self):
        pass

    def __connect(self,db):
        """

        :param db:
        :return:
        """
        host = "127.0.0.1"
        conn = pymysql.connect(host=host,port=4306,user="root",passwd="mysql",db=db)

        return conn

    def select(self,db,query):
        """

        :param db:
        :param query:
        :return:
        """
        conn = self.__connect(db=db)
        corr = conn.cursor()
        corr.execute(query=query)

        result = corr.fetchall()

        all_rows = []
        for line in result:
            row = []
            for col in line:
                row.append(str(col))
            all_rows.append(row)


        conn.close()
        corr.close()
        return all_rows

    def update(self,db,query):
        """

        :param db:
        :param query:
        :return:
        """
        conn = self.__connect(db)

        corr = conn.cursor()

        result = corr.execute(query=query)
        conn.commit()
        conn.close()
        corr.close()

        return result