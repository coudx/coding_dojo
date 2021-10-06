<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html>
<head>
    <%-- for Bootstrap CSS --%>
    <link rel="stylesheet" href="/webjars/bootstrap/css/bootstrap.min.css"/>
    <%-- For any Bootstrap that uses JS or jQuery--%>
    <script src="/webjars/jquery/jquery.min.js"></script>
    <script src="/webjars/bootstrap/js/bootstrap.min.js"></script>
    <title>Reading Books</title>
</head>
<body>
    <c:choose>
        <c:when test="${book != null}">
            <h1 class="mb-3"><c:out value="${book.getTitle()}"/></h1>
            <p>Description: <c:out value="${book.getDescription()}"/> </p>
            <p>Language: <c:out value="${book.getLanguage()}"/> </p>
            <p>Number of Pages: <c:out value="${book.getNumberOfPages()}"/> </p>
        </c:when>
        <c:otherwise>
            <h1>Book does not exist</h1>
        </c:otherwise>
    </c:choose>
</body>
</html>
