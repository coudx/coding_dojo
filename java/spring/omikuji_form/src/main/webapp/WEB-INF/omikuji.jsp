<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html>
<head>
    <!-- for Bootstrap CSS -->
    <link rel="stylesheet" href="/webjars/bootstrap/css/bootstrap.min.css"/>
    <!-- For any Bootstrap that uses JS or jQuery-->
    <script src="/webjars/jquery/jquery.min.js"></script>
    <script src="/webjars/bootstrap/js/bootstrap.min.js"></script>
    <title>Omikuji</title>
</head>
<body>
    <div class="container">
        <h1 class="text-center mb-3">Send an Omikuji!</h1>
        <form action="" class="form-control" method="post">
            <div class="mb-3">
                <label for="year" class="form-label">Pick any number from 5 to 25</label>
                <input type="number" class="form-control" id="year" name="year">
                <c:if test="${error != null}">
                    <div class="alert alert-danger">
                        <c:out value="${error}"/>
                    </div>
                </c:if>
            </div>
            <div class="mb-3">
                <label for="city" class="form-label">Enter the name of any city.</label>
                <input type="text" class="form-control" id="city" name="city">
            </div>
            <div class="mb-3">
                <label for="name" class="form-label">Enter the name of any real person</label>
                <input type="text" class="form-control" id="name" name="name">
            </div>
            <div class="mb-3">
                <label for="hobby" class="form-label">Enter professional endeavor or hobby</label>
                <input type="text" class="form-control" id="hobby" name="hobby">
            </div>
            <div class="mb-3">
                <label for="type" class="form-label">Enter any type of living thing.</label>
                <input type="text" class="form-control" id="type" name="type">
            </div>
            <div class="mb-3">
                <label for="etc" class="form-label">Say something nice to someone:</label>
                <textarea class="form-control" row="3" id="etc" name="etc"></textarea>
            </div>
            <p class="mb-3">Send and show a friend</p>
            <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                <button type="submit" class="btn btn-primary mb-3" type="button">Send</button>
            </div>
        </form>
    </div>
</body>
</html>
