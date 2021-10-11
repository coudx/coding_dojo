<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html>
<head>
    <!-- for Bootstrap CSS -->
    <link rel="stylesheet" href="/webjars/bootstrap/css/bootstrap.min.css"/>
    <!-- For any Bootstrap that uses JS or jQuery-->
    <script src="/webjars/jquery/jquery.min.js"></script>
    <script src="/webjars/bootstrap/js/bootstrap.min.js"></script>
    <title>Show Expense</title>
</head>
<body>
    <div class="container m-3">
        <div style="display:flex; justify-content: space-between" class="mb-3">
            <h1 class="mb-3 text-success">Expense Details</h1>
            <a href="/expense">Go back</a>
        </div>
        <div class="row">
            <div class="col-5">Expense Name:</div>
            <div class="col-5"><c:out value="${poke.getExpense()}"/></div>
        </div>
        <div class="row">
            <div class="col-5">Expense Description:</div>
            <div class="col-5"><c:out value="${poke.getDescription()}"/></div>
        </div>
        <div class="row">
            <div class="col-5">Vendor:</div>
            <div class="col-5"><c:out value="${poke.getVendor()}"/></div>
        </div>
        <div class="row">
            <div class="col-5">Amount Spent:</div>
            <div class="col-5"><c:out value="${poke.getAmount()}"/></div>
        </div>
    </div>
</body>
</html>
