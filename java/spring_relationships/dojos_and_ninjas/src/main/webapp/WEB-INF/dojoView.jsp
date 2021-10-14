<%@ page contentType="text/html;charset=UTF-8" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html>
<head>
    <!-- for Bootstrap CSS -->
    <link rel="stylesheet" href="/webjars/bootstrap/css/bootstrap.min.css"/>
    <!-- For any Bootstrap that uses JS or jQuery-->
    <script src="/webjars/jquery/jquery.min.js"></script>
    <script src="/webjars/bootstrap/js/bootstrap.min.js"></script>
    <title>Dojo Page</title>
</head>
<body>
    <div class="container m-5">
        <h1 class="mb-3">${dojo.getName()} Location Ninjas</h1>
        <table class="table table-striped table-bordered">
            <thead>
                <tr>
                    <th scope="col">First Name</th>
                    <th scope="col">Last Name</th>
                    <th scope="col">Age</th>
                </tr>
            </thead>
            <tbody>
                <c:forEach items="${dojo.getNinjas()}" var="ninja">
                    <tr>
                        <td>${ninja.getFirst_name()}</td>
                        <td>${ninja.getLast_name()}</td>
                        <td>${ninja.getAge()}</td>
                    </tr>
                </c:forEach>
            </tbody>
        </table>
    </div>
</body>
</html>
