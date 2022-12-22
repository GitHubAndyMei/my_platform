# MYSQL
IP = '127.0.0.1'
PORT = 13306
USERNAME = 'momenta'
PASSWORD = 'momenta'
DATABASE = 'ct_db'

ORM = 'sqlalchemy'

# 目标文件
MODEL_OUTDIR = '../../app/model'  # 模型文件输出目录
MODEL_INIT_OUTDIR = MODEL_OUTDIR + '/__init__.py'  # 模型文件输出目录

# 模板文件路径
MODEL_TEMP = f'./template/{ORM}/model.template'
MODEL_DTO_TEMP = f'./template/{ORM}/dto.template'
MODEL_INIT_TEMP = f'./template/__init__.template'
MODEL_README_TEMP = './template/README.md.template'

# 导包路径
IMPORT_INIT_PATH = f'from {".".join(MODEL_OUTDIR.split("/")[2:5])}.'  # app.model.dbs
