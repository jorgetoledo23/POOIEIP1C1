create database VentasPython;
use VentasPython;

create table clientes (
	rut varchar(20) primary key,
    nombre varchar(100) not null,
    apellido varchar(100) not null,
    correo varchar(100) not null
);

create table productos (
	productoid int auto_increment primary key,
    nombre varchar(100) not null,
    precio int not null,
    stock int not null
);

create table ventas (
	ventaid int auto_increment primary key,
    fecha date,
    rutCliente varchar(20),
    totalventa int,
	constraint fk_cliente foreign key (rutCliente) references clientes (rut)
);

create table detalleventa(
	detalleid int auto_increment primary key,
    ventaid int,
    productoid int,
    cantidad int,
    subtotal int,
    constraint fk_ventaid foreign key (ventaid) references ventas (ventaid),
    constraint fk_productoid foreign key (productoid) references productos (productoid)
);


insert into clientes values ('1.111.111-1', 'Jhon', 'Snow', 'jsnow@inacap.cl');
insert into clientes values ('2.222.222-2', 'Vea', 'Stone', 'jsnow@inacap.cl');
insert into clientes values ('3.333.333-3', 'Gon', 'Snake', 'jsnow@inacap.cl');
insert into clientes values ('4.444.444-4', 'Funes', 'Vid', 'jsnow@inacap.cl');
insert into clientes values ('5.555.555-5', 'Rick', 'Trans', 'jsnow@inacap.cl');


insert into productos (nombre, precio, stock) values ('Producto A', 9990, 100);
insert into productos (nombre, precio, stock) values ('Producto B', 299990, 10);
insert into productos (nombre, precio, stock) values ('Producto C', 199990, 56);
insert into productos (nombre, precio, stock) values ('Producto D', 659990, 33);
insert into productos (nombre, precio, stock) values ('Producto F', 79990, 12);
insert into productos (nombre, precio, stock) values ('Producto G', 49990, 45);
insert into productos (nombre, precio, stock) values ('Producto H', 39990, 145);
insert into productos (nombre, precio, stock) values ('Producto I', 29990, 329);
insert into productos (nombre, precio, stock) values ('Producto J', 179990, 12);
insert into productos (nombre, precio, stock) values ('Producto K', 159990, 5);
insert into productos (nombre, precio, stock) values ('Producto L', 19990, 19);