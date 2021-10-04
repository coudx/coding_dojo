<%@ page language="java" contentType="text/html;charset=UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html>
<head>
    <!-- for Bootstrap CSS -->
    <link rel="stylesheet" href="/webjars/bootstrap/css/bootstrap.min.css"/>
    <!-- YOUR own local CSS -->
    <link rel="stylesheet" href="/css/main.css"/>
    <!-- For any Bootstrap that uses JS or jQuery-->
    <script src="/webjars/jquery/jquery.min.js"></script>
    <script src="/webjars/bootstrap/js/bootstrap.min.js"></script>
    <title>Fruit Loops</title>
</head>
<body>
    <div class="container">
        <h1 style="color: pink;">Fruit Store</h1>
        <table class="table" style="border: 15px pink solid;">
            <thead>
                <tr>
                    <th scope="col">Name</th>
                    <th scope="col">Price</th>
                </tr>
            </thead>
            <tbody>
                <c:forEach var = "item" items="${items}">
                    <tr>
                        <td><c:out value="${item.getName()}"/></td>
                        <td><c:out value="${item.getPrice()}"/></td>
                    </tr>
                </c:forEach>
            </tbody>
        </table>
    </div>
</body>
</html>
