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
    <div class="container m-3">
        <div class="d-flex justify-content-between mb-3">
            <h1>Add a Book to Your Shelf!</h1>
            <a href="/books">back to the shelves</a>
        </div>
        <form:form action="/books/new" method="post" modelAttribute="book">
            <form:hidden path="user" value="${uid}"/>
            <form:errors path="title"/>
            <div class="row">
                <div class="col-3">
                    <label>Title</label>
                </div>
                <div class="col">
                    <form:input path="title"/>
                </div>
            </div>
            <form:errors path="author"/>
            <div class="row">
                <div class="col-3">
                    <label>Author</label>
                </div>
                <div class="col">
                    <form:input path="author"/>
                </div>
            </div>
            <form:errors path="thoughts"/>
            <div class="row">
                <div class="col-3">
                    <label>My thoughts</label>
                </div>
                <div class="col">
                    <form:textarea path="thoughts" rows="3"/>
                </div>
            </div>
            <input type="submit" value="Submit" style="float: right;">
        </form:form>
    </div>
</body>
</html>
