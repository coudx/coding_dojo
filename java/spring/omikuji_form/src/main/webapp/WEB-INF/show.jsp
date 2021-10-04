<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html>
<head>
    <!-- for Bootstrap CSS -->
    <link rel="stylesheet" href="/webjars/bootstrap/css/bootstrap.min.css"/>
    <!-- YOUR own local CSS -->
    <link rel="stylesheet" href="/css/main.css"/>
    <!-- For any Bootstrap that uses JS or jQuery-->
    <script src="/webjars/jquery/jquery.min.js"></script>
    <script src="/webjars/bootstrap/js/bootstrap.min.js"></script>
    <title>Omikuji</title>
</head>
<body>
    <div class="container">
        <h1 class="mb-3 text-center">Here's Your Omikuji!</h1>
        <div class="border border-3 mb-5 bg-info text-white p-4">
            <h1>In <c:out value="${year}"/> years, you will live in <c:out value="${city}"/> with <c:out value="${name}"/> as your roommate, <c:out value="${hobby}"/> for a living. The next time you see a <c:out value="${type}"/>, you will have good luck. Also, <c:out value="${etc}"/></h1>
        </div>
        <a href="/omikuji"><p class="text-center">Go Back</p></a>
    </div>
</body>
</html>
