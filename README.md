## [HouseQR](http://houseqr.ryukyuupdate.com)
#### このリポジトリは主にフロントエンド、DBと連携しバックエンド処理全般を行うためのバックエンドプログラムです。
##### my_api.py はAPIのURLごとに関数を用意し my_mysql.py をインポートしCRUD処理を行います。
##### my_mysql.py はMySQLのライブラリ、mysql.connector を利用し AWS RDS へSQLを実行します。