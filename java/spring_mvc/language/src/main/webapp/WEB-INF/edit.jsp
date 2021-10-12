<%@ page contentType="text/html;charset=UTF-8" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page isErrorPage="true" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<html>
<head>
    <!-- for Bootstrap CSS -->
    <link rel="stylesheet" href="/webjars/bootstrap/css/bootstrap.min.css"/>
    <!-- For any Bootstrap that uses JS or jQuery-->
    <script src="/webjars/jquery/jquery.min.js"></script>
    <script src="/webjars/bootstrap/js/bootstrap.min.js"></script>
    <title><c:out value="${lang.getName()}"/></title>
    <style>
        .button {
            background: none!important;
            border: none;
            padding: 0!important;
            color: #069;
            text-decoration: underline;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <header class="m-3 d-grid gap-2 d-md-flex justify-content-md-end">
        <form action="/languages/${lang.getId()}" method="post" style="display: inline;">
            <input type="hidden" name="_method" value="delete">
            <input type="submit" value="Delete" class="button">
        </form>
        <a href="/languages">Dashboard</a>
    </header>
    <div class="container m-4">
        <form:form action="/languages/edit/${lang.getId()}" method="post" modelAttribute="lang">
            <input type="hidden" name="_method" value="put">
            <form:errors path="name" class="text-danger"/>
            <p class="mb-3">
                <form:label path="name">Name</form:label>
                <form:input path="name" class="form-control"/>
            </p>
            <form:errors path="creator" class="text-danger"/>
            <p class="mb-3">
                <form:label path="creator">Creator</form:label>
                <form:input path="creator" class="form-control"/>
            </p>
            <form:errors path="version" class="text-danger"/>
            <p class="mb-3">
                <form:label path="version">version</form:label>
                <form:input path="version" class="form-control"/>
            </p>
            <input type="submit" value="Submit" class="btn btn-primary mb-3 justify-content-md-end"/>
        </form:form>
    </div>
</body>
</html>
