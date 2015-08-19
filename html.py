__author__ = 'zavidan'
startpage = """
<html>
<head>
    <script type="text/javascript" src="/js/jquery-2.1.4.min.js"></script>
</head>
<body>
    <div>
        <a href="/test">Demo page</a>
        <a href="/edit">Make/Edit your house</a>
        <a href="/dataentry">Manual Data entry</a>
    </div>
</body>
</html>
"""
makinghouse = """
<html>
<head>
    <link rel="stylesheet" type="text/css" href="/css/edit.css">
    <script type="text/javascript" src="/js/draw.js"></script>
    <script type="text/javascript" src="/js/jquery-2.1.4.min.js"></script>
</head>
<body onload="house()">
    {edit}
    <table id="tab" cellspacing="0"></table>
    <form action="/edit" method="post">
        <input type="hidden" name="data" value="" id="data">
        <input type="submit" id="submit" value="Save House">
    </form>
</body>
</html>
"""
housemade = """
<html>
<head>
    <link rel="stylesheet" type="text/css" href="/css/edit.css">
    <script type="text/javascript" src="/js/house.js"></script>
    <script type="text/javascript" src="/js/jquery-2.1.4.min.js"></script>
</head>
<body onload="makehouse()">
    <table id="tab" cellspacing="0"></table>
    <form action="/edit" method="post">
        <input type="hidden" name="data" value="{house}" id="data">
        <input type="submit" id="submit" value="Save House">
    </form>
    <input type="button" onclick="toggle()" value"Toggle draw">
    <a href="/">Back to main page</a>
</body>
</html>
"""

dataentry = """
<html>
<head>
    <!--<link rel="stylesheet" type="text/css" href="/css/edit.css">-->
    <script type="text/javascript" src="/js/jquery-2.1.4.min.js"></script>
    <script type="text/javascript" src="/js/dataentry.js"></script>
</head>
<body>
    <div>
        <a href="/">Back to main page</a>
    </div>
    <form action="/dataentry" method="post">
        <table id="name">
        <table id="conductance"></table>
        <table id="area"></table>
        <table id="temps"></table>
        <table id="capacity"></table>
        <input type="submit">
    </form>
</body>
</html>
"""