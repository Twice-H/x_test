import pymysql
from utils.logutil import my_log

class Mysql:
    # 初始化数据链接数据库
    def __init__(self, host, user, passwrod, database, charset="utf-8", port="3306"):
        self.log = my_log()
        self.conn = pymysql.connect(
            host=host,
            user=user,
            passwrod=passwrod,
            database=database,
            charset=charset,
            port=port
        )
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    #3、创建查询、执行方法
    def fetchone(self, sql):
        """
        单个查询
        :param sql:
        :return:
        """
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def fetchall(self, sql):
        """
        多个查询
        :param sql:
        :return:
        """
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def exec(self, sql):
        """
        执行
        :param sql:
        :return:
        """
        try:
            if self.conn and self.cursor:
                self.cursor.execute(sql)
                self.conn.commit()
        except Exception as ex:
            self.conn.rollback()
            self.log.error("Mysql执行失败")
            self.log.error(ex)
            return False
        return True

    # 4. 关闭对象
    def __del__(self):
        # 关闭光标对象
        if self.cursor is not None:
            self.cursor.close()

        # 关闭链接对象
        if self.cursor is not None:
            self.conn.close()

if __name__ == "__main__":
    mysql = Mysql("211.103.136.242",
                  "test",
                  "test123456",
                  "meiduo",
                  charset="utf8",
                  port=7090)
    res = mysql.exec("update tb_users set first_name='python' where username = 'python'")
    print(res)