<%--
  Created by IntelliJ IDEA.
  User: xuanl
  Date: 10/4/2021
  Time: 9:30 AM
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="css/style.css">
    <title>Date</title>
</head>
<body>
    <p class="date"><c:out value="${date}"/></p>
    <script>alert("This is the date template")</script>
</body>
</html>
