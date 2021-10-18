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
    <title>Read Share</title>
</head>
<body>
    <div class="container">
        <h1 style="color: purple;">Book Club</h1>
        <p>A place for friends to share thoughts on books.</p>
        <div class="row mt-4">
            <div class="col-4 m-5 p-3 bg-secondary text-white">
                <h1 style="color: rgb(0, 89, 223) !important">Register</h1>
                <form:form action="/register" method="post" modelAttribute="reg">
                    <div class="mb-3">
                        <label class="form-label">First Name:</label>
                        <form:input path="name" class="form-control"/>
                        <form:errors path="name" class="text-danger"/>
                    </div>
                    <div class="mb-3">
                        <label class="form-label">Email:</label>
                        <form:input path="email" class="form-control"/>
                        <form:errors path="email" class="text-danger"/>
                    </div>
                    <div class="mb-3">
                        <label class="form-label">Password:</label>
                        <form:input path="password" class="form-control"/>
                        <form:errors path="password" class="text-danger"/>
                    </div>
                    <div class="mb-3">
                        <label class="form-label">Confirm Password:</label>
                        <form:input path="confirm" class="form-control"/>
                        <form:errors path="confirm" class="text-danger"/>
                    </div>
                    <div class="d-flex justify-content-center">
                        <input type="submit" value="Register" class="btn btn-primary"/>
                    </div>
                </form:form>
            </div>

            <div class="col-4 m-5 p-3 bg-secondary text-white">
                <h1 style="color: rgb(58, 240, 2) !important">Login</h1>
                <form:form action="/login" method="post" modelAttribute="login">
                    <div class="mb-3">
                        <label class="form-label">Username:</label>
                        <form:input path="email" class="form-control"/>
                        <form:errors path="email" class="text-danger"/>
                    </div>
                    <div class="mb-3">
                        <label class="form-label">Password:</label>
                        <form:input path="password" class="form-control"/>
                        <form:errors path="password" class="text-danger"/>
                    </div>
                    <div class="d-flex justify-content-center">
                        <input type="submit" value="Login" class="btn btn-success"/>
                    </div>
                </form:form>
            </div>
        </div>
    </div>
</body>
</html>
