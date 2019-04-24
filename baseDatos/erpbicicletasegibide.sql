-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 24-04-2019 a las 20:32:22
-- Versión del servidor: 10.1.38-MariaDB
-- Versión de PHP: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `erpbicicletasegibide`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `nombreCliente` char(20) COLLATE utf8mb4_spanish_ci NOT NULL,
  `telefono` char(30) COLLATE utf8mb4_spanish_ci NOT NULL,
  `mail` char(20) COLLATE utf8mb4_spanish_ci NOT NULL,
  `dni` char(12) COLLATE utf8mb4_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`nombreCliente`, `telefono`, `mail`, `dni`) VALUES
('jorge', '789654', '@jorge', '1599632'),
('lander', '7289', '@lander', '193773'),
('ekaitz', '456', '@ekaitz', '44686144'),
('jose', '741', '@jose', '741258'),
('antonio', '741258', '@antonio', '7899512');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `devoluciones`
--

CREATE TABLE `devoluciones` (
  `fecha` char(20) COLLATE utf8mb4_spanish_ci NOT NULL,
  `informacion` char(50) COLLATE utf8mb4_spanish_ci NOT NULL,
  `devolucion` char(30) COLLATE utf8mb4_spanish_ci NOT NULL,
  `usuario` char(20) COLLATE utf8mb4_spanish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `facturas`
--

CREATE TABLE `facturas` (
  `fecha` char(20) COLLATE utf8mb4_spanish_ci NOT NULL,
  `factura` char(30) COLLATE utf8mb4_spanish_ci NOT NULL,
  `dni_cliente` char(12) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `usuario` char(20) COLLATE utf8mb4_spanish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `facturas`
--

INSERT INTO `facturas` (`fecha`, `factura`, `dni_cliente`, `usuario`) VALUES
('04/24/19', 'facturave4341Apr2019', '7899512', 'ventas'),
('04/23/19', 'facturave5244Apr2019', '1599632', 'ventas'),
('04/23/19', 'facturave7636Apr2019', NULL, NULL),
('04/24/19', 'facturave8868Apr2019', '193773', 'ventas'),
('04/24/19', 'facturave9844Apr2019', '44686144', 'ventas');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `facturascontabilizadas`
--

CREATE TABLE `facturascontabilizadas` (
  `fecha` char(20) COLLATE utf8mb4_spanish_ci NOT NULL,
  `factura` char(30) COLLATE utf8mb4_spanish_ci NOT NULL,
  `usuario` char(20) COLLATE utf8mb4_spanish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ofertasempleo`
--

CREATE TABLE `ofertasempleo` (
  `id` int(11) NOT NULL,
  `fecha` char(20) COLLATE utf8mb4_spanish_ci NOT NULL,
  `puesto` char(20) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `descripcion` char(20) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `sueldo` float DEFAULT NULL,
  `usuario` char(20) COLLATE utf8mb4_spanish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ofertaventas`
--

CREATE TABLE `ofertaventas` (
  `id` int(11) NOT NULL,
  `fecha` char(20) COLLATE utf8mb4_spanish_ci NOT NULL,
  `producto` char(20) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `descripcion` char(20) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `descuento` float DEFAULT NULL,
  `usuario` char(20) COLLATE utf8mb4_spanish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reparaciones`
--

CREATE TABLE `reparaciones` (
  `fecha` char(20) COLLATE utf8mb4_spanish_ci NOT NULL,
  `factura` char(30) COLLATE utf8mb4_spanish_ci NOT NULL,
  `dni_cliente` char(12) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `usuario` char(20) COLLATE utf8mb4_spanish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `reparaciones`
--

INSERT INTO `reparaciones` (`fecha`, `factura`, `dni_cliente`, `usuario`) VALUES
('04/23/19', 'facturata4707Apr2019', '44686144', 'taller'),
('04/23/19', 'facturata4980Apr2019', '44686144', 'taller'),
('04/24/19', 'facturata517Apr2019', '44686144', 'taller'),
('04/24/19', 'facturata6127Apr2019', '44686144', 'taller'),
('04/24/19', 'facturata7962Apr2019', '44686144', 'ventas'),
('04/24/19', 'facturata8462Apr2019', '44686144', 'ventas');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `usuario` char(20) COLLATE utf8mb4_spanish_ci NOT NULL,
  `password` char(30) COLLATE utf8mb4_spanish_ci NOT NULL,
  `departamento` char(20) COLLATE utf8mb4_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`usuario`, `password`, `departamento`) VALUES
('marketing', 'marketing', 'ma'),
('postventa', 'postventa', 'pv'),
('taller', 'taller', 'ta'),
('ventas', 'ventas', 've');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`dni`),
  ADD UNIQUE KEY `nombreCliente` (`nombreCliente`),
  ADD UNIQUE KEY `telefono` (`telefono`),
  ADD UNIQUE KEY `mail` (`mail`);

--
-- Indices de la tabla `devoluciones`
--
ALTER TABLE `devoluciones`
  ADD PRIMARY KEY (`devolucion`),
  ADD KEY `usuario` (`usuario`);

--
-- Indices de la tabla `facturas`
--
ALTER TABLE `facturas`
  ADD PRIMARY KEY (`factura`),
  ADD KEY `dni_cliente` (`dni_cliente`),
  ADD KEY `usuario` (`usuario`);

--
-- Indices de la tabla `facturascontabilizadas`
--
ALTER TABLE `facturascontabilizadas`
  ADD PRIMARY KEY (`factura`),
  ADD KEY `usuario` (`usuario`);

--
-- Indices de la tabla `ofertasempleo`
--
ALTER TABLE `ofertasempleo`
  ADD PRIMARY KEY (`id`),
  ADD KEY `usuario` (`usuario`);

--
-- Indices de la tabla `ofertaventas`
--
ALTER TABLE `ofertaventas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `usuario` (`usuario`);

--
-- Indices de la tabla `reparaciones`
--
ALTER TABLE `reparaciones`
  ADD PRIMARY KEY (`factura`),
  ADD KEY `dni_cliente` (`dni_cliente`),
  ADD KEY `usuario` (`usuario`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`usuario`),
  ADD UNIQUE KEY `password` (`password`),
  ADD UNIQUE KEY `departamento` (`departamento`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `ofertasempleo`
--
ALTER TABLE `ofertasempleo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `ofertaventas`
--
ALTER TABLE `ofertaventas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `devoluciones`
--
ALTER TABLE `devoluciones`
  ADD CONSTRAINT `devoluciones_ibfk_1` FOREIGN KEY (`usuario`) REFERENCES `usuarios` (`usuario`);

--
-- Filtros para la tabla `facturas`
--
ALTER TABLE `facturas`
  ADD CONSTRAINT `facturas_ibfk_1` FOREIGN KEY (`dni_cliente`) REFERENCES `clientes` (`dni`),
  ADD CONSTRAINT `facturas_ibfk_2` FOREIGN KEY (`usuario`) REFERENCES `usuarios` (`usuario`);

--
-- Filtros para la tabla `facturascontabilizadas`
--
ALTER TABLE `facturascontabilizadas`
  ADD CONSTRAINT `facturascontabilizadas_ibfk_1` FOREIGN KEY (`usuario`) REFERENCES `usuarios` (`usuario`);

--
-- Filtros para la tabla `ofertasempleo`
--
ALTER TABLE `ofertasempleo`
  ADD CONSTRAINT `ofertasempleo_ibfk_1` FOREIGN KEY (`usuario`) REFERENCES `usuarios` (`usuario`);

--
-- Filtros para la tabla `ofertaventas`
--
ALTER TABLE `ofertaventas`
  ADD CONSTRAINT `ofertaventas_ibfk_1` FOREIGN KEY (`usuario`) REFERENCES `usuarios` (`usuario`);

--
-- Filtros para la tabla `reparaciones`
--
ALTER TABLE `reparaciones`
  ADD CONSTRAINT `reparaciones_ibfk_1` FOREIGN KEY (`dni_cliente`) REFERENCES `clientes` (`dni`),
  ADD CONSTRAINT `reparaciones_ibfk_2` FOREIGN KEY (`usuario`) REFERENCES `usuarios` (`usuario`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
