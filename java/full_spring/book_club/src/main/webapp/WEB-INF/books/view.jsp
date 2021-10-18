<%@ page contentType="text/html;charset=UTF-8" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
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
        <header class="d-flex justify-content-between mb-5">
            <h1 style="display: inline-flex;"><i><c:out value="${bookController.getTitle()}"/></i></h1>
            <a href="/books" style="float: right;">back to the shelves</a>
        </header>
        <p class="mb-3"><span style="color: red;">${bookController.getUser().getName()}</span> read <span style="color: purple;">${bookController.getTitle()}</span> by <span style="color: green;">${bookController.getAuthor()}</span></p>
        <p >Here are ${bookController.getUser().getName()}'s thoughts:</p>
        <div class="container m-3">
            <hr class="mb-3">
            <p class="mb-3">${bookController.getThoughts()}</p>
            <hr class="mb-3">
            <c:if test="${bookController.getUser().getId()} == ${uid}">
                <a href="/books/<c:out value="${bookController.getId()}"/>/edit" style="float: right;"><button class="btn">edit</button></a>
            </c:if>
        </div>
    </div>
</body>
</html>
