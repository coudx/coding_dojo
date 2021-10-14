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
    <title>New Dojo</title>
</head>
<body>
    <div class="container m-5">
        <h1>New Dojo</h1>
        <form:form action="/dojos/new" method="post" modelAttribute="dojo">
            <form:errors path="name" class="text-danger"/>
            <p>
                <form:label path="name">Name: </form:label>
                <form:input path="name" class="form-control"/>
            </p>
            <input type="submit" value="Create" class="btn btn-primary mb-3"/>
        </form:form>
    </div>
</body>
</html>
