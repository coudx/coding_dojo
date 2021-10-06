<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html>
<head>
    <!-- for Bootstrap CSS -->
    <link rel="stylesheet" href="/webjars/bootstrap/css/bootstrap.min.css"/>
    <!-- For any Bootstrap that uses JS or jQuery-->
    <script src="/webjars/jquery/jquery.min.js"></script>
    <script src="/webjars/bootstrap/js/bootstrap.min.js"></script>
    <title>Reading Books</title>
</head>
<body>
    <div class="container m-3">
        <h1 class="mb-3">All Books</h1>
        <table class="table table-striped table-bordered border-dark">
            <thead>
                <tr class="table-secondary table-bordered border-dark">
                    <th scope="col">ID</th>
                    <th scope="col">Title</th>
                    <th scope="col">Language</th>
                    <th scope="col"># Pages</th>
                </tr>
            </thead>
            <tbody>
                <c:forEach var="book" items="${books}">
                    <tr>
                        <th scope="row"><c:out value="${book.getId()}"/></th>
                        <td><a href="books/<c:out value="${book.getId()}"/>"><c:out value="${book.getTitle()}"/></a></td>
                        <td><c:out value="${book.getLanguage()}"/></td>
                        <td><c:out value="${book.getNumberOfPages()}"/></td>
                    </tr>
                </c:forEach>
            </tbody>
        </table>
    </div>
</body>
</html>
