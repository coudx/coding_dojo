<%@ page contentType="text/html;charset=UTF-8" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<html>
<head>
    <!-- for Bootstrap CSS -->
    <link rel="stylesheet" href="/webjars/bootstrap/css/bootstrap.min.css"/>
    <!-- For any Bootstrap that uses JS or jQuery-->
    <script src="/webjars/jquery/jquery.min.js"></script>
    <script src="/webjars/bootstrap/js/bootstrap.min.js"></script>
    <title>New Ninja</title>
</head>
<body>
    <div class="container m-5">
        <h1>New Ninja</h1>
        <form:form action="/ninjas/new" method="post" modelAttribute="ninja">
            <form:select path="dojo">
                <c:forEach var="dojo" items="${dojos}">
                    <form:option value="${dojo.getId()}">
                        <c:out value="${dojo.getName()}"/>
                    </form:option>
                </c:forEach>
            </form:select>
            <form:errors path="first_name" class="text-danger"/>
            <p>
                <form:label path="first_name">Firstname: </form:label>
                <form:input path="first_name" class="form-control"/>
            </p>
            <form:errors path="last_name" class="text-danger"/>
            <p>
                <form:label path="last_name">Lastname: </form:label>
                <form:input path="last_name" class="form-control"/>
            </p>
            <form:errors path="age" class="text-danger"/>
            <p>
                <form:label path="age">Age: </form:label>
                <form:input path="age" class="form-control"/>
            </p>
            <input type="submit" value="Create" class="btn btn-primary mb-3"/>
        </form:form>
    </div>
</body>
</html>
