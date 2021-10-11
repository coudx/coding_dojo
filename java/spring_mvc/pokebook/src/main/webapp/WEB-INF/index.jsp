<%@ page contentType="text/html;charset=UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<html>
<head>
    <!-- for Bootstrap CSS -->
    <link rel="stylesheet" href="/webjars/bootstrap/css/bootstrap.min.css"/>
    <!-- For any Bootstrap that uses JS or jQuery-->
    <script src="/webjars/jquery/jquery.min.js"></script>
    <script src="/webjars/bootstrap/js/bootstrap.min.js"></script>
    <title>Read Shares</title>
</head>
<body>
    <div class="container m-3">
        <h1 class="mb-3 text-primary">PokeBook</h1>
        <table class="table table-striped mb-3">
            <thead>
                <tr>
                    <th scope="col">Expense</th>
                    <th scope="col">Vendor</th>
                    <th scope="col">Amount</th>
                </tr>
            </thead>
            <tbody>
                <c:forEach var="pokebook" items="${pokebooks}">
                    <tr>
                        <td><c:out value="${pokebook.getExpense()}"/></td>
                        <td><c:out value="${pokebook.getVendor()}"/></td>
                        <td><c:out value="${pokebook.getAmount()}"/></td>
                    </tr>
                </c:forEach>
            </tbody>
        </table>
        <div class="container m-3">
            <h1 class="mb-3 text-primary">Track an expense:</h1>
            <form:form action="/expense/add" method="post" modelAttribute="newPoke">
                <div class="mb-3 row form-group">
                    <form:errors path="expense" class="text-danger" />
                    <label class="col-sm-2 col-form-label">Expense Name:</label>
                    <div class="col-sm-10">
                        <form:input path="expense" class="form-control"/>
                    </div>
                </div>
                <div class="mb-3 row form-group">
                    <form:errors path="vendor" class="text-danger" />
                    <label class="col-sm-2 col-form-label">Vendor:</label>
                    <div class="col-sm-10">
                        <form:input path="vendor" class="form-control"/>
                    </div>
                </div>
                <div class="mb-3 row form-group">
                    <form:errors path="amount" class="text-danger" />
                    <label class="col-sm-2 col-form-label">Amount:</label>
                    <div class="col-sm-10">
                        <form:input path="amount" class="form-control"/>
                    </div>
                </div>
                <div class="mb-3 row form-group">
                    <form:errors path="description" class="text-danger" />
                    <label class="col-sm-2 col-form-label">Description:</label>
                    <div class="col-sm-10">
                        <form:input path="description" class="form-control"/>
                    </div>
                </div>
                <input type="submit" value="Submit"  class="btn btn-primary mb-3"/>
            </form:form>
        </div>
    </div>

</body>
</html>
