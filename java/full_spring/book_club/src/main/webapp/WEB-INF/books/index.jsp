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
        <div class="row justify-content-between mb-3">
            <div class="col">
                <h1>Welcome, <c:out value="${user.getName()}"/></h1>
                <p>Books from everyone's shelves:</p>
            </div>
            <div class="col">
                <a href="/logout" style="display: block; float:right;">logout</a>
                <a href="/books/new" style="float:right;">+ Add a book to my shelf!</a>
            </div>
        </div>
        <table class="table table-striped table-bordered">
            <thead>
                <tr>
                    <th scope="col">ID</th>
                    <th scope="col">Title</th>
                    <th scope="col">Author Name</th>
                    <th scope="col">Posted By</th>
                </tr>
            </thead>
            <tbody>
                <c:forEach var="bookController" items="books">
                    <tr>
                        <th scope="row"><c:out value="${bookController.getId()}"/></th>
                        <td><c:out value="${bookController.getTitle()}"/></td>
                        <td><c:out value="${bookController.getAuthor()}"/></td>
                        <td><c:out value="${bookController.getUser().getName()}"/></td>
                    </tr>
                </c:forEach>
            </tbody>
        </table>

    </div>
</body>
</html>
