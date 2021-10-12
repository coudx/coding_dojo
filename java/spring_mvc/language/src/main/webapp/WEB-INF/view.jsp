<%@ page contentType="text/html;charset=UTF-8" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
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
        <a href="/languages">Dashboard</a>
    </header>
    <div class="container m-3">
        <p class="mb-5"><c:out value="${lang.getName()}"/></p>
        <p class="mb-5"><c:out value="${lang.getCreator()}"/></p>
        <p class="mb-5"><c:out value="${lang.getVersion()}"/></p>
        <a class="mb-3" href="/languages/${lang.getId()}/edit">Edit</a>
        <form action="/languages/${lang.getId()}" method="post">
            <input type="hidden" name="_method" value="delete">
            <input type="submit" value="Delete" class="button">
        </form>
    </div>
</body>
</html>
