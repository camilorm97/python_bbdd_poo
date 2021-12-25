# python_bbdd_poo
Conectar una base de datos con PyMysql usando POO

Creamos una base de datos, en nuestro caso, usando XAMPP en phpmyadmin

CREATE DATABASE dbPython;
CREATE TABLE `Users`(
  `id` int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8_spanish2_ci NOT NULL,
  `password` varchar(50) COLLATE utf8_spanish2_ci NOT NULL,
  `mail` varchar(100) COLLATE utf8_spanish2_ci NOT NULL,
  `rol` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

ALTER TABLE `Users`
  ADD PRIMARY KEY (`id`);
  
ALTER TABLE `Users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;
COMMIT;
