
BOT_NAME = 'cen'

SPIDER_MODULES = ['cen.spiders']
NEWSPIDER_MODULE = 'cen.spiders'

ROBOTSTXT_OBEY = True
LOG_LEVEL = 'WARNING'

ITEM_PIPELINES = {
    'cen.pipelines.MySQLPipeline': 2
}

DB_HOST = 'localhost'
DB_PORT = 3306
DB_USER = 'root'
DB_PASSWD = 'helloworld'
DB_DB = 'khmergoo_sequelize'
