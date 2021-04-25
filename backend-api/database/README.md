URL::

**https://www.liquibase.org/**



Command::


```
liquibase
--driver=com.mysql.cj.jdbc.Driver
--classpath=mysql-connector-java-5.1.21-bin.jar
--url="jdbc:mysql://<IP OR HOSTNAME>:<PORT>/<SCHEMA NAME>?autoReconnect=true&useSSL=FALSE|TRUE"
--changeLogFile=db.changelog-1.0.xml
--username=<MYSQL USERNAME>
--password=<MYSQL PASSWORD>
generateChangeLog


```


1) Create a database and a user on server's machine.
2) liquibase.properties-file, use the same db and credentials

3) log in as root to mysql Aqfp(whYq8Dt

3.1) mysql> CREATE database everly_prod_prov;
3.2) mysql> CREATE database everly_prod_application;
3.3) mysql> CREATE database everly_prod_transaction;
3.4) mysql> CREATE database everly_prod_cards;
3.5) mysql> CREATE database everly_prod_reminder_notification;


CREATE USER 'everlyUser'@'localhost'IDENTIFIED WITH mysql_native_password BY 'Everly@DT12345';
CREATE USER 'everlyUser'@'%'IDENTIFIED WITH mysql_native_password BY 'Everly@DT12345';

CREATE USER 'everlyUser'@'localhost' IDENTIFIED BY 'Everly@DT12345';
GRANT ALL ON everly_prod_prov.* TO 'everlyUser'@'localhost';
GRANT ALL ON everly_prod_application.* TO 'everlyUser'@'localhost';
GRANT ALL ON everly_prod_transaction.* TO 'everlyUser'@'localhost';
GRANT ALL ON everly_prod_cards.* TO 'everlyUser'@'localhost';
GRANT ALL ON everly_prod_prov.* TO 'everlyUser'@'%';
GRANT ALL ON everly_prod_transaction.* TO 'everlyUser'@'%';
GRANT ALL ON everly_prod_cards.* TO 'everlyUser'@'%';
GRANT ALL ON everly_prod_reminder_notification.* TO 'everlyUser'@'%';


GRANT SELECT ON db2.invoice TO 'jeffrey'@'%';
ALTER USER 'jeffrey'@'%' WITH MAX_QUERIES_PER_HOUR 90;


WHERE:

everly_prod_prov = db_name
everlyUser = db_user
Everly@DT12345 = db_password



Mysql connector file download url:

https://dev.mysql.com/downloads/connector/j/

>> Choose platform independent option



For example:

./liquibase-3.8.5/liquibase --defaultsFile=admin-auth/liquibase.properties update

./liquibase-3.8.5/liquibase  --defaultsFile=admin-service/liquibase.properties update


./liquibase-3.8.5/liquibase  --defaultsFile=transation-service/liquibase.properties update

./liquibase-3.8.5/liquibase  --defaultsFile=product-service/liquibase.properties update

./liquibase-3.8.5/liquibase  --defaultsFile=customer-service/liquibase.properties update

./liquibase-3.8.5/liquibase  --defaultsFile=customer-auth/liquibase.properties update

./liquibase-3.8.5/liquibase  --defaultsFile=messaging-service/liquibase.properties update

./liquibase-3.8.5/liquibase  --defaultsFile=menu-management/liquibase.properties update

./liquibase-3.8.5/liquibase  --defaultsFile=payment-service/liquibase.properties update


./liquibase-3.8.5/liquibase  --defaultsFile=order-service-new/liquibase.properties update


liquibase --defaultsFile=



liquibase  --defaultsFile=src/main/resources/liquibase/liquibase.properties \
           --classpath="d:\mysql-connector-java-5.1.6.jar;D:\spring-learning\liquibase-helloworld-demo\target\liquibase-helloworld-demo.jar"  \
           --change




References::

> https://www.liquibase.org/documentation/tutorials/mysql.html
> https://download.liquibase.org/download/
