<%--
  Created by IntelliJ IDEA.
  User: xuanl
  Date: 10/1/2021
  Time: 3:29 PM
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <title>Simple Receipt</title>
</head>
<body>
    <h2>Customer Name: <c:out value="${name}"/></h2>
    <p>Item name: <c:out value="${itemName}"/></p>
    <p>Price: <c:out value="${price}"/></p>
    <p>Description: <c:out value="${description}"/></p>
    <p>Vendor: <c:out value="${vendor}"/></p>
</body>

