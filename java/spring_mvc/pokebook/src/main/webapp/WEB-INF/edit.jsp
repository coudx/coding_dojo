<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page isErrorPage="true" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<html>
<head>
    <!-- for Bootstrap CSS -->
    <link rel="stylesheet" href="/webjars/bootstrap/css/bootstrap.min.css"/>
    <!-- For any Bootstrap that uses JS or jQuery-->
    <script src="/webjars/jquery/jquery.min.js"></script>
    <script src="/webjars/bootstrap/js/bootstrap.min.js"></script>
    <title>Edit My Task</title>
</head>
<body>
    <div class="container m-3">
        <div style="display:flex; justify-content: space-between">
            <h1 class="mb-3 text-success">Edit Expense</h1>
            <a href="/expense">Go back</a>
        </div>
        <form:form action="/expense/edit/${poke.getId()}" method="post" modelAttribute="poke">
            <input type="hidden" name="_method" value="put">
            <div class="mb-3 row form-group">
                <form:errors path="expense" class="text-danger" />
                <form:label path="expense" class="col-sm-2 col-form-label">Expense Name:</form:label>
                <div class="col-sm-10">
                    <form:input path="expense" class="form-control"/>
                </div>
            </div>
            <div class="mb-3 row form-group">
                <form:errors path="vendor" class="text-danger" />
                <form:label path="vendor" class="col-sm-2 col-form-label">Vendor:</form:label>
                <div class="col-sm-10">
                    <form:input path="vendor" class="form-control"/>
                </div>
            </div>
            <div class="mb-3 row form-group">
                <form:errors path="amount" class="text-danger" />
                <form:label path="amount" class="col-sm-2 col-form-label">Amount:</form:label>
                <div class="col-sm-10">
                    <form:input path="amount" class="form-control"/>
                </div>
            </div>
            <div class="mb-3 row form-group">
                <form:errors path="description" class="text-danger" />
                <form:label path="description" class="col-sm-2 col-form-label">Description:</form:label>
                <div class="col-sm-10">
                    <form:input path="description" class="form-control"/>
                </div>
            </div>
            <input type="submit" value="Submit"  class="btn btn-primary mb-3"/>
        </form:form>
</div>
</body>
</html>
